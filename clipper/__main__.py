"""Print a reviewable JSON plan; shell redirection can save it separately."""
import argparse
from dataclasses import asdict
import json
import sys
from .engine import Segment, Span, candidates, cut_plan, validate_transcript
from .media import detect_silence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('transcript', help='JSON list: start, end, text in source seconds')
    parser.add_argument('--mode', choices=['conservative', 'balanced', 'aggressive'], default='conservative')
    parser.add_argument('--protected', help='JSON list of intentional pause spans: start, end')
    args = parser.parse_args()
    try:
        with open(args.transcript) as stream:
            segments = [Segment(**s) for s in json.load(stream)]
        validate_transcript(segments)
        protected = []
        if args.protected:
            with open(args.protected) as stream:
                protected = [Span(**s) for s in json.load(stream)]
        duration, silence = detect_silence(args.source)
        if any(s.end > duration for s in [*segments, *protected]):
            raise ValueError('transcript/protected span exceeds media duration')
        ranked = candidates(segments)
        for candidate in ranked:
            candidate['edit_plan'] = cut_plan(Span(candidate['start'], candidate['end']),
                                               segments, silence, args.mode, protected)
        print(json.dumps(dict(duration=duration, silences=[asdict(s) for s in silence],
                              candidates=ranked), indent=2, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'Cannot plan clips: {error}\n')
    except Exception as error:
        # Do not dump FFmpeg stderr or source transcript in a traceback.
        parser.exit(1, f'Media analysis failed: {type(error).__name__}\n')


if __name__ == '__main__':
    main()
