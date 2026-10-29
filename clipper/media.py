"""Bounded local media inspection. Never modifies source media."""
import json
import math
from pathlib import Path
import re
import subprocess
from .engine import Span


def inspect_media(source):
    path = Path(source).resolve(strict=True)
    if not path.is_file():
        raise ValueError('source must be a regular file')
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_format', '-show_streams',
                             '-of', 'json', str(path)], capture_output=True, text=True,
                            check=True, timeout=30)
    metadata = json.loads(result.stdout)
    duration = float(metadata['format']['duration'])
    if not math.isfinite(duration) or not 0 < duration <= 4 * 3600:
        raise ValueError('duration must be positive and at most four hours')
    if not any(s['codec_type'] == 'audio' for s in metadata['streams']):
        raise ValueError('source has no audio stream')
    return path, duration


def detect_silence(source, noise_db=-35.0, minimum=0.5):
    if not math.isfinite(noise_db) or not -100 <= noise_db <= -5:
        raise ValueError('noise threshold outside supported range')
    if not math.isfinite(minimum) or not 0.1 <= minimum <= 30:
        raise ValueError('minimum silence outside supported range')
    path, duration = inspect_media(source)
    result = subprocess.run(['ffmpeg', '-nostdin', '-hide_banner', '-i', str(path),
                             '-map', '0:a:0', '-vn', '-af',
                             f'silencedetect=noise={noise_db}dB:d={minimum}',
                             '-f', 'null', '-'], capture_output=True, text=True,
                            check=True, timeout=600)
    spans, start = [], None
    for event, value in re.findall(r'silence_(start|end):\s*([0-9.eE+-]+)', result.stderr):
        time = max(0.0, min(duration, float(value)))
        if event == 'start':
            start = time
        elif start is not None:
            if time > start:
                spans.append(Span(start, time))
            start = None
    if start is not None and start < duration:
        spans.append(Span(start, duration))
    return duration, spans
