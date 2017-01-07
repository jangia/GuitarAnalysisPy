import os
import pprint
from DrawPlots import DrawPlots
from Fft import Fft
from Files import Files
from Peaks import Peaks
from Synth import Synth

my_dir = '../wav/'
plot_dir = '../plot/'
synth_dir = '../synth/'
dirs = os.listdir(my_dir)

for dir_name in dirs:
    print("Working in " + dir_name)
    audio_data, file_names = Files.read_all_files(my_dir + dir_name)
    params = [[1.75, 48000, 16] for audio in audio_data]
    # params = [[1.75, 48000, 16], [1.75, 48000, 16], [1.75, 48000, 16]]
    audio_files_data = Files.add_params(audio_data, params)
    all_fft = Fft.get_all_fft(audio_files_data)
    DrawPlots.fft_plot(all_fft, file_names, 'log', 'Amplitude', 'Frequency', plot_dir, dir_name)

    if dir_name != 'noise':
        params = [0, 2000, 40, 0.005]
        main_freq = Peaks.get_all_main(all_fft, params)
        Synth.write_all(main_freq, synth_dir, file_names)
        pprint.pprint(main_freq)



