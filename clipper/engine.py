"""Explainable heuristics; scores are not measures of virality or factual quality."""
from dataclasses import asdict, dataclass
import math
import re


@dataclass(frozen=True)
class Span:
    start: float
    end: float

    def __post_init__(self):
        if not all(math.isfinite(v) for v in (self.start, self.end)):
            raise ValueError('timestamps must be finite')
        if self.start < 0 or self.end <= self.start:
            raise ValueError('expected 0 <= start < end')


@dataclass(frozen=True)
class Segment(Span):
    text: str

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError('transcript text must be nonempty')


def validate_transcript(segments):
    for a, b in zip(segments, segments[1:]):
        if a.end > b.start:
            raise ValueError('transcript must be chronological and nonoverlapping')


def complete(text):
    return bool(re.search(r'[.!?][\"\u201d\u2019\x27)]*$', text.strip()))


def candidates(segments, min_duration=10.0, max_duration=60.0, limit=5):
    """Rank contiguous, sentence-complete windows without rearranging speech.

    No semantic model is present: dependent openings are flagged for review.
    Missing visual/audio evidence stays unknown, rather than being fabricated.
    """
    validate_transcript(segments)
    if not 0 < min_duration <= max_duration or limit < 1:
        raise ValueError('invalid duration bounds or limit')
    ranked = []
    for i, first in enumerate(segments):
        if i and not complete(segments[i - 1].text):
            continue
        for j in range(i, len(segments)):
            last = segments[j]
            duration = last.end - first.start
            if duration > max_duration:
                break
            if duration < min_duration or not complete(last.text):
                continue
            text = ' '.join(s.text for s in segments[i:j + 1])
            words = re.findall(r'\b\w+\b', text)
            if len(words) < 8:
                continue
            dependent = bool(re.match(r'^(and|but|so|because|this|that|it|they|he|she)\b', first.text, re.I))
            hook = 0.7 if '?' in first.text else 0.4
            context = 0.3 if dependent else 0.6
            clarity = min(1.0, len(words) / max(duration, 1) / 2.5)
            # Terminal punctuation is only a boundary signal, not proof of payoff.
            scores = dict(hook=hook, context=context, clarity=round(clarity, 3),
                          narrative_payoff=None, visual_suitability=None, audio_suitability=None)
            score = round((hook + context + clarity) / 3, 3)
            ranked.append(dict(start=first.start, end=last.end, text=text, scores=scores,
                               overall=score, review_required=True,
                               reasons=['Complete transcript boundaries; semantic coherence and payoff need human review.'] +
                               (['Opening may depend on earlier context.'] if dependent else [])))
    ranked.sort(key=lambda x: (-x['overall'], x['start'], x['end']))
    selected = []
    for item in ranked:
        if all(item['end'] <= c['start'] or item['start'] >= c['end'] for c in selected):
            selected.append(item)
            if len(selected) == limit:
                break
    return selected


def cut_plan(clip, segments, silences, mode='conservative', protected=()):
    """Only shorten detector-confirmed silence outside transcript speech.

    Transcript segments are conservative protected speech bounds. Additional
    protected spans preserve intentional pauses/reactions supplied by a human.
    All decisions retain source timestamps; omission is reversible.
    """
    settings = {'conservative': (1.5, 0.4), 'balanced': (1.0, 0.25), 'aggressive': (0.6, 0.15)}
    if mode not in settings:
        raise ValueError('unknown cutting mode')
    validate_transcript(segments)
    threshold, padding = settings[mode]
    # Merge overlapping detector intervals before computing edits.
    merged = []
    for span in sorted(silences, key=lambda s: s.start):
        start, end = max(clip.start, span.start), min(clip.end, span.end)
        if end <= start:
            continue
        if merged and start <= merged[-1].end:
            merged[-1] = Span(merged[-1].start, max(end, merged[-1].end))
        else:
            merged.append(Span(start, end))
    remove = []
    blockers = [*segments, *protected]
    for silence in merged:
        pieces = [(silence.start, silence.end)]
        for block in blockers:
            next_pieces = []
            for start, end in pieces:
                if block.end <= start or block.start >= end:
                    next_pieces.append((start, end))
                else:
                    if start < block.start:
                        next_pieces.append((start, block.start))
                    if block.end < end:
                        next_pieces.append((block.end, end))
            pieces = next_pieces
        for start, end in pieces:
            if end - start >= threshold and end - start > padding * 2:
                remove.append(Span(start + padding, end - padding))
    keep, cursor = [], clip.start
    for span in remove:
        if cursor < span.start:
            keep.append(Span(cursor, span.start))
        cursor = span.end
    if cursor < clip.end:
        keep.append(Span(cursor, clip.end))
    offset = 0.0
    timeline = []
    for span in keep:
        timeline.append(dict(source_start=span.start, source_end=span.end,
                             output_start=offset, output_end=offset + span.end - span.start))
        offset += span.end - span.start
    return dict(version=1, mode=mode, clip=asdict(clip), removed=[asdict(s) for s in remove],
                timeline=timeline, duration=offset, review_required=True)
