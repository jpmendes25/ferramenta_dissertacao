import numpy as np
from scipy import signal

def sth_generator(f, p, sr, t):
    time = np.linspace(0, t/1000, int(t/1000 * sr), False)
    sawtooth = signal.sawtooth(2 * np.pi * f * time + p - 90)
    return time, sawtooth
