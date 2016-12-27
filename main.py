from DrawPlots import DrawPlots
from Fft import Fft
from Files import Files
from Peaks import Peaks
import os
import pprint

my_dir = '../wav/'
dirs = os.listdir(my_dir)

for dir_name in dirs:
    print("Working in " + dir_name)
    audio_data = Files.read_all_files(my_dir + dir_name)
    params = [[1.75, 48000, 16] for audio in audio_data]
    # params = [[1.75, 48000, 16], [1.75, 48000, 16], [1.75, 48000, 16]]
    audio_files_data = Files.add_params(audio_data, params)
    all_fft = Fft.get_all_fft(audio_files_data)
    DrawPlots.fft_plot(all_fft, 'log', 'Amplitude', 'Frequency', my_dir + dir_name)

    params = [0, 2000, 50, 0.1]
    main_freq = Peaks.get_all_main(all_fft, params)

    pprint.pprint(main_freq)

