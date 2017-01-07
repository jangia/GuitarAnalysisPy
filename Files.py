import scipy.io.wavfile as wav
import os
from os.path import basename


class Files:

    @staticmethod
    def read_all_files(files_dir):

        files = os.listdir(files_dir)

        audio_files_data = []
        file_names = []

        for file in files:
            fs, audio_data = wav.read(files_dir + '/' + file)
            audio_files_data.append(audio_data)
            file_names.append(basename(file))

        return audio_files_data, file_names

    @staticmethod
    def add_params(audio_files_data, params):
        i = 0
        audio_data_params = [[] for i in range(len(params))]
        for param in params:
            all_params = [audio_files_data[i]] + param
            audio_data_params[i] = all_params
            i += 1
        return audio_data_params
