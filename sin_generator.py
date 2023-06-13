import numpy as np

def sin_generator(f, p, sr, t):
   time = np.linspace(0, t/1000, int(t/1000 * sr), False)
   sine = np.sin(2 * np.pi * f * time + np.deg2rad(p))
   return time, sine
