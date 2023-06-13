import soundfile as sf

def audio_converter(signal_name, k, f, p, sr, t):
    name = k + "_" + str(f) + "Hz_" + str(p) + "degree_" + str(sr) + "Hz_" + str(t) + "ms.wav"
    sf.write(name, signal_name, sr, subtype='PCM_24')
