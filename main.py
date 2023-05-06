import os

from combiner import AudioCombiner
from convertor import VoiceConvertor, MODELS, F0_METHODS
from splitter import SongSplitter
from youtube import AudioDownloader


def main():
    project_name = input('Please enter a project name: ')
    if not project_name:
        project_name = 'delilah'
    project_root = f'projects/{project_name}'

    youtube_url = input('Please enter a youtube url: ')
    if not youtube_url:
        youtube_url = 'https://www.youtube.com/watch?v=S6XXDw0Mrck'


    model = input(f'Please choose a model. Available models are {list(MODELS.keys())}: ')
    if not model:
        model = 'kanye'

    auto_predict = input('Auto predict? [y/n]: ') == 'y'
    if auto_predict == '':
        auto_predict = False

    f0_method = input(f'f0 method? {F0_METHODS}: ')
    if not f0_method:
        f0_method = 'all'

    if not os.path.exists(project_root):
        os.makedirs(project_root)


    ad = AudioDownloader(project_root)
    audio_path = ad.download(youtube_url, project_name)

    s = SongSplitter(project_name)
    vocals_path, no_vocals_path = s.split_vocals(audio_path)

    if f0_method == 'all':
        methods = F0_METHODS
    else:
        methods = [f0_method]

    print(f'Running voice converter with f0_methods {methods} and auto predict {auto_predict}')
    for m in methods:
        vc = VoiceConvertor(f0_method=m, auto_predict=auto_predict)
        converted_path = vc.convert(model, vocals_path)

        ac = AudioCombiner()
        combined_path = os.path.join(project_root, f'{project_name}_{model}_{m}{"_na" if not auto_predict else ""}.wav')
        ac.combine(converted_path, no_vocals_path, combined_path)

        print(f'Results saved to {combined_path}')

if __name__ == '__main__':
    main()