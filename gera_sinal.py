import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--kind_of_wave', type=str)
parser.add_argument('-f', '--frequency', type=float)
parser.add_argument('-p', '--phase', type=float)
parser.add_argument('-sr', '--sample_rate', type=int)
parser.add_argument('-t', '--duration_time', type=float)

args = parser.parse_args()

k = args.kind_of_wave
f = args.frequency
p = args.phase
sr = args.sample_rate
t = args.duration_time

time = np.linspace(0, t/1000, int(t/1000 * sr), False)

name = k+"_"+str(f)+"Hz_"+str(p)+"degree_"+str(sr)+"Hz_"+str(t)+"ms"+".wav"

if k == "sin":

    sin = np.sin(2 * np.pi * f * time + np.deg2rad(p))

    plt.plot(time, sin)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sine wave')
    plt.show()

    sf.write(name, sin, sr, subtype='PCM_24')

if k == "sqr":

    square = 0.5 * signal.square(2 * np.pi * f * time + p) + 0.5

    plt.plot(time, square)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Square wave')
    plt.show()

    sf.write(name, sqr, sr, subtype='PCM_24')

if k == "tri":

    triangle = signal.sawtooth(2 * np.pi * f * time + p, 0.5)

    plt.plot(time, triangle)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Triangle wave')
    plt.show()

    sf.write(name, tri, sr, subtype='PCM_24')

if k == "sth":

    sawtooth = signal.sawtooth(2 * np.pi * f * time + p)

    plt.plot(time, sawtooth)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Triangle wave')
    plt.show()

    sf.write(name, sth, sr, subtype='PCM_24')
