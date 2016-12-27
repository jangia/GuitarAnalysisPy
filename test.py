import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks_cwt
from DrawPlots import DrawPlots
from Fft import Fft
import scipy.io.wavfile as wav

# fs, audio_data = wav.read('../wav/pick/normal_pick_4.wav')
# fft = Fft.get_fft(audio_data, 2.75)
#DrawPlots.fft_plot((fft, ), 'log', 'Amplitude', 'Frequency')

# d = int(round(len(abs_fft)/2))
#
# fig = plt.figure(figsize=(8, 6))
# fft_plot = fig.add_subplot(111, axisbg='#FFFFCC')
#
# fft_plot.semilogy(abs_fft[:(d-1)], 'r')
# # plt.plot(audio)
# fft_plot.set_ylabel('Audio time plot')
# # plt.show()
# # set useblit = True on gtkagg for enhanced performance
# cursor = Cursor(fft_plot, useblit=True, color='red', linewidth=2)
# plt.show()
# peaks = find_peaks_cwt(abs_fft[0:2000], np.arange(1, 50))
# max_a = max(abs_fft)
# th = max_a/100
# main_fqs = {}
# for peak in peaks:
#     if abs_fft[peak] >= th:
#         main_fqs[peak] = abs_fft[peak]
#
# print(main_fqs)



