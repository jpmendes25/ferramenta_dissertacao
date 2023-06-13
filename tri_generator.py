import numpy as np
from scipy import signal

def tri_generator(f, p, sr, t):
    time = np.linspace(0, t/1000, int(t/1000 * sr), False)
    triangle = signal.sawtooth(2 * np.pi * f * time + p, 0.5)
    return time, triangle
