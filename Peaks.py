from scipy.signal import find_peaks_cwt
import numpy as np


class Peaks:

    @staticmethod
    def get_main_frequencies(abs_fft, start=0, end=10000, width=50, threshold=0.1):
        peaks = find_peaks_cwt(abs_fft[start:end], np.arange(1, width))
        max_a = max(abs_fft)
        th = max_a * threshold
        main_fqs = {}
        for peak in peaks:
            if abs_fft[peak] >= th:
                main_fqs[peak] = abs_fft[peak]

        return main_fqs

    @staticmethod
    def get_all_main(all_fft, params):
        all_main_fqs = [{} for i in range(len(all_fft))]
        j = 0
        for fft in all_fft:
            all_main_fqs[j] = Peaks.get_main_frequencies(fft, params[0], params[1], params[2], params[3])
            j += 1

        return all_main_fqs
