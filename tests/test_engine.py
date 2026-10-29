import math
import unittest
from clipper.engine import Span, Segment, candidates, cut_plan


class EngineTests(unittest.TestCase):
    def test_invalid_timestamps(self):
        for start, end in [(0, math.inf), (math.nan, 2), (-1, 2), (2, 2)]:
            with self.assertRaises(ValueError):
                Span(start, end)

    def test_context_and_unknown_evidence(self):
        transcript = [Segment(0, 6, 'Why does this simple experiment fail every single time?'),
                      Segment(7, 14, 'The answer is that heat changes the material structure.')]
        result = candidates(transcript)
        self.assertEqual(len(result), 1)
        self.assertEqual((result[0]['start'], result[0]['end']), (0, 14))
        self.assertIsNone(result[0]['scores']['narrative_payoff'])
        self.assertTrue(result[0]['review_required'])

    def test_incomplete_thought_rejected(self):
        self.assertEqual(candidates([Segment(0, 20, 'This is an unfinished thought with enough words but no ending')]), [])

    def test_mid_sentence_start_excluded(self):
        result = candidates([Segment(0, 7, 'Here is the beginning of a sentence'),
                             Segment(8, 20, 'and here is how the whole sentence finally ends.')])
        self.assertEqual([x['start'] for x in result], [0])

    def test_overlap_rejected(self):
        with self.assertRaises(ValueError):
            candidates([Segment(0, 8, 'One.'), Segment(7, 10, 'Two.')])

    def test_silence_never_removes_transcript_speech(self):
        transcript = [Segment(0, 2, 'First.'), Segment(6, 10, 'Last.')]
        plan = cut_plan(Span(0, 10), transcript, [Span(0, 10)])
        self.assertEqual(plan['removed'], [{'start': 2.4, 'end': 5.6}])
        self.assertAlmostEqual(plan['duration'], 6.8)
        self.assertAlmostEqual(plan['timeline'][1]['output_start'], 2.4)

    def test_protected_pause_and_short_gap_preserved(self):
        plan = cut_plan(Span(0, 10), [], [Span(1, 4), Span(7, 8)], protected=[Span(1, 4)])
        self.assertEqual(plan['removed'], [])
        self.assertEqual(plan['duration'], 10)

    def test_merge_clip_and_modes(self):
        for mode in ['conservative', 'balanced', 'aggressive']:
            plan = cut_plan(Span(2, 8), [], [Span(0, 5), Span(4, 10)], mode)
            self.assertEqual(len(plan['removed']), 1)
            self.assertGreater(plan['duration'], 0)
            self.assertLess(plan['duration'], 6)
        with self.assertRaises(ValueError):
            cut_plan(Span(0, 10), [], [], 'unknown')

    def test_empty_transcript_does_not_force_candidates(self):
        self.assertEqual(candidates([]), [])


if __name__ == '__main__':
    unittest.main()
