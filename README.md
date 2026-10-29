# Clip Cutter — local clip-planning engine

Initial implementation of Phase 1 from `master.md`. Python standard library only;
requires Python 3.10+ and installed `ffmpeg` / `ffprobe` (tested on Python 3.14.8,
FFmpeg n9.0.2). No installation, network requests, or model credentials needed.

```bash
python -m unittest discover -s tests -v
python -m clipper /path/to/video.mp4 /path/to/transcript.json
python -m clipper /path/to/video.mp4 /path/to/transcript.json --mode balanced --protected /path/to/pauses.json
```

Transcript JSON is a chronological, nonoverlapping list of objects with `start`,
`end` (seconds in original media), and `text`. Segments should describe sentences
or speech regions accurately. Protected pause JSON contains `start` and `end`.
CLI prints JSON to stdout. Save it separately from original media/transcripts.

The engine ranks contiguous, punctuation-complete transcript windows, suppresses
overlapping suggestions, and produces reversible source-to-output timelines.
Only detector-confirmed silence outside transcript speech and protected pauses
is shortened. Modes vary minimum gap and retained padding. Intentional silence
cannot be inferred reliably from amplitude; supply protected pause spans.

All suggestions require human review. Scores are simple documented heuristics;
semantic understanding, narrative payoff, visual quality and audio quality are
not verified. Missing signals are null. Transcription, preview, rendering,
captions, GUI, face tracking and project persistence are not implemented.
No source media is modified. No claim of publishable output is made.
