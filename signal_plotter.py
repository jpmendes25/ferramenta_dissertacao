import matplotlib.pyplot as plt

def signal_plotter(time, signal, signal_name):
    plt.plot(time, signal)
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.title(signal_name)
    plt.show()
