import os
import subprocess
import shlex

from collections import namedtuple


Model = namedtuple('Model', 'speaker path')
MODEL_PATH = 'models'
MODELS = {
    'kanye': Model('aimodel', os.path.join(MODEL_PATH, 'kanye')),
    'obama': Model('Obama', os.path.join(MODEL_PATH, 'obama')),
    'trump': Model('trump', os.path.join(MODEL_PATH, 'trump')),
    'biden': Model('Biden', os.path.join(MODEL_PATH, 'biden')),
    'tswift': Model('taylor', os.path.join(MODEL_PATH, 'tswift'))
}
F0_METHODS = ['dio', 'parselmouth', 'harvest']
SVC_BIN_PATH = '/Users/shibo/.pyenv/shims/svc'

class VoiceConvertor:
    def __init__(self, f0_method='dio', auto_predict=False):
        self.models = MODELS
        self.auto_predict = auto_predict
        self.f0_method = f0_method if f0_method else 'dio'

    def convert(self, model, vocals_path):
        if model not in self.models:
            raise ValueError(f'model {model} not found')

        path_split = vocals_path.split('.')
        default_converted_path = f'{path_split[0]}.out.{path_split[1]}'
        path, filename = os.path.split(default_converted_path)
        if not self.auto_predict:
            filename = 'na_' + filename
        if self.f0_method != 'dio':
            filename = f'{self.f0_method}_{filename}'
        converted_path = os.path.join(path, f'{model}_{filename}')
        if os.path.exists(converted_path):
            return converted_path

        m = self.models[model]
        env = {
            'PYTORCH_ENABLE_MPS_FALLBACK': '1'
        }
        subprocess.run(shlex.split(f'{SVC_BIN_PATH} infer {"-na" if not self.auto_predict else ""} -fm {self.f0_method} -s {m.speaker} -m {m.path} -c {os.path.join(m.path, "config.json")} {vocals_path}'), env=env)
        os.rename(default_converted_path, converted_path)

        return converted_path
