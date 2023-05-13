import os
import sox

from pathlib import Path
from pydub import AudioSegment


def overlay_audio(path_a, path_b, output_path):
    sound_a = AudioSegment.from_mp3(path_a)
    sound_b = AudioSegment.from_mp3(path_b)
    output = sound_a.overlay(sound_b)

    output.export(output_path, format='mp3')


def transpose(audio_path, steps):
    tfm = sox.Transformer()
    tfm.pitch(steps)

    directory = os.path.dirname(audio_path)
    path = Path(audio_path)
    transposed_path = f'{directory}/{path.stem}_t{steps}{path.suffix}'
    tfm.build_file(audio_path, transposed_path)

    return transposed_path