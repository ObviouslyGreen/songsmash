from pydub import AudioSegment

def overlay_audio(path_a, path_b, output_path):
    sound_a = AudioSegment.from_mp3(path_a)
    sound_b = AudioSegment.from_mp3(path_b)
    output = sound_a.overlay(sound_b)

    output.export(output_path, format='mp3')


def transpose(audio_path, steps):
    return audio_path