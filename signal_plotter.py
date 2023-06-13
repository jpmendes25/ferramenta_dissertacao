import matplotlib.pyplot as plt

def signal_plotter(time, signal_name, x_label='Time (ms)', y_label='Amplitude', title='Signal'):
    plt.plot(time, signal_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
