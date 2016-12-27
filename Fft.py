from scipy.fftpack import fft


class Fft:

    @staticmethod
    def get_fft(audio_data, start_time=0, sample_fq=48000, bit_rate=16):

        start = int(round(start_time * sample_fq))  # int(3*len(audio_data)/4)
        end = start + sample_fq
        audio = audio_data[start:end]
        norm_audio = [(ele / 2 ** bit_rate) * 2 for ele in audio]
        audio_fft = fft(norm_audio)

        return abs(audio_fft)

    @staticmethod
    def get_all_fft(audio_files_data):
        all_fft = []

        for audio_data in audio_files_data:
            all_fft.append(Fft.get_fft(audio_data[0], audio_data[1], audio_data[2], audio_data[3]))

        return all_fft
