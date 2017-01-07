import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor


class DrawPlots:

    @staticmethod
    def fft_plot(abs_fft_list=[], file_names=[], fft_yscale='log', fft_ylabel='y', fft_xlabel='f', dir_name='./', plot_name='plot'):

        fig = plt.figure(figsize=(8, 6))
        layout = int(len(abs_fft_list))*100 + 10 + 1
        i=0;

        for abs_fft in abs_fft_list:

            d = int(round(len(abs_fft) / 10))

            fft_plot = fig.add_subplot(layout, axisbg='#FFFFCC')

            if fft_yscale == 'log':
                fft_plot.semilogy(abs_fft[:(d - 1)], 'r')
            else:
                fft_plot.plot(abs_fft[:(d - 1)], 'r')

            fft_plot.set_ylabel(fft_ylabel)
            fft_plot.set_xlabel(fft_xlabel)
            fft_plot.set_title(file_names[i])
            i += 1
            layout += 1

        cursor = Cursor(fft_plot, useblit=True, color='red', linewidth=1)
        plt.savefig(dir_name + plot_name + '.png')
