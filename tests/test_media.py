import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from clipper.media import detect_silence


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg required')
class MediaTests(unittest.TestCase):
    def test_real_silence_detection_and_source_preservation(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'source.wav'
            subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                            'sine=frequency=440:duration=14', '-af',
                            "volume=enable='between(t,4,7)':volume=0", str(source)], check=True)
            original = source.read_bytes()
            duration, spans = detect_silence(source)
            self.assertAlmostEqual(duration, 14, places=2)
            self.assertEqual(len(spans), 1)
            self.assertAlmostEqual(spans[0].start, 4, delta=0.05)
            self.assertAlmostEqual(spans[0].end, 7, delta=0.05)
            transcript = Path(folder) / 'transcript.json'
            transcript.write_text(json.dumps([
                dict(start=0, end=4, text='Why does this experiment fail every single time?'),
                dict(start=7, end=14, text='The explanation is simple and the result is now clear.')]))
            result = subprocess.run([sys.executable, '-m', 'clipper', str(source), str(transcript)],
                                    capture_output=True, text=True, check=True)
            plan = json.loads(result.stdout)['candidates'][0]['edit_plan']
            self.assertEqual(len(plan['removed']), 1)
            self.assertLess(plan['duration'], 14)
            self.assertEqual(source.read_bytes(), original)

    def test_corrupted_media_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'broken.wav'
            source.write_bytes(b'not media')
            with self.assertRaises(subprocess.CalledProcessError):
                detect_silence(source)

    def test_invalid_detector_configuration(self):
        with self.assertRaises(ValueError):
            detect_silence('unused.wav', noise_db=float('nan'))


if __name__ == '__main__':
    unittest.main()
