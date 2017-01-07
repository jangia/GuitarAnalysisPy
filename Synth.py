from wavebender import *


class Synth:

    @staticmethod
    def violin(fq_amp):
        # simulates a violin playing G.
        amplitude = 0.25

        key_max = max(fq_amp, key=fq_amp.get)
        max_ampl = fq_amp[key_max]

        return (damped_wave(key, amplitude=amplitude*value/max_ampl, length=44100 * 5) for key, value in fq_amp.items())

    @staticmethod
    def write_file(fq_amp, file_dir, file_name):
        channels = (Synth.violin(fq_amp),)
        samples = compute_samples(channels, 44100 * 5 * 1)
        write_wavefile(file_dir + file_name + '.wav', samples, 44100 * 5 * 1, nchannels=1)

    @staticmethod
    def write_all(fq_amp_all, file_dir, file_names):
        i = 0
        for var in fq_amp_all:
            Synth.write_file(var, file_dir, file_names[i])
            i += 1

