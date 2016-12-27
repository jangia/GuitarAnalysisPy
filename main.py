from DrawPlots import DrawPlots
from Fft import Fft
from Files import Files

my_dir = '../wav/pick'
audio_data = Files.read_all_files(my_dir)
params = [[1.75, 48000, 16] for audio in audio_data]
audio_files_data = Files.add_params(audio_data, params)
all_fft = Fft.get_all_fft(audio_files_data)
DrawPlots.fft_plot(all_fft, 'log', 'Amplitude', 'Frequency')
print(all_fft)

