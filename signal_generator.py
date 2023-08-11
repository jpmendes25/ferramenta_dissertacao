import argparse

import sin_generator
import sqr_generator
import tri_generator
import sth_generator
import signal_plotter
import audio_converter

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

if k == 'sin':
    time, signal = sin_generator.sin_generator(f, p, sr, t)
    signal_name = 'Sine wave'

if k == 'sqr':
    time, signal = sqr_generator.sqr_generator(f, p, sr, t)
    signal_name = 'Square wave'

if k == 'tri':
    time, signal = tri_generator.tri_generator(f, p, sr, t)
    signal_name = 'Triangle wave'

if k == 'sth':
    time, signal = sth_generator.sth_generator(f, p, sr, t)
    signal_name = 'Sawtooth wave'

signal_plotter.signal_plotter(time, signal, signal_name)

audio_converter.audio_converter(signal, k, f, p, sr, t)

