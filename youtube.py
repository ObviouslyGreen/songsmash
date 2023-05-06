import youtube_dl
import os

class AudioDownloader:
    def __init__(self, project_root):
        self.project_root = project_root
        self.ydl_options = {
            'format': 'bestaudio[ext=m4a]',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav'
            }]
        }

    def download(self, url, audio_name):
        opts = self.ydl_options.copy()
        opts['outtmpl'] = f'{os.path.join(self.project_root, audio_name)}.%(ext)s'
        collector = FilenameCollectorPP()

        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.add_post_processor(collector)
            ydl.download([url])

        return collector.filenames[0]

class FilenameCollectorPP(youtube_dl.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information['filepath'])
        return [], information
