import demucs.separate
import os
import shlex

from pathlib import Path

class SongSplitter:
    def __init__(self, project_name, model='htdemucs'):
        self.project_name = project_name
        self.model = model

    def split_vocals(self, song_path):
        song_directory = os.path.dirname(song_path)
        vocals_path = os.path.join(song_directory, self.model, self.project_name, 'vocals.wav')
        no_vocals_path = os.path.join(song_directory, self.model, self.project_name, 'no_vocals.wav')

        print(f'vocals_path: {vocals_path}')
        print(f'no_vocals_path: {no_vocals_path}')
        if os.path.exists(vocals_path) and os.path.exists(no_vocals_path):
            return (vocals_path, no_vocals_path)

        demucs.separate.main(opts=shlex.split(f'--two-stems vocals -n {self.model} -o {song_directory} "{song_path}"'))

        return (vocals_path, no_vocals_path)