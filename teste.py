import sys
import numpy as np
import os.path
import librosa
import librosa.display
from os import path
from os import stat
from tinytag import TinyTag
import soundfile as sf
import itertools
import matplotlib.pyplot as plt

if __name__ == '__main__':
	directory = sys.argv[1]
	print(directory)
	names = os.listdir(directory)
	audios = []
	for track in names:
		track_name = directory + os.sep + track
		if path.isdir(track_name):
			continue
		tag = TinyTag.get(track_name)
		y, sr = librosa.load(track_name, sr=tag.samplerate)
		audios.append(y)
	#print(names)
	#print(audios)

	names_no_wav = []
	for i in range(0, len(names)):
		name_no_wav = names[i].replace(".wav", "")
		names_no_wav.append(name_no_wav)
	#print(names_no_wav)

	combnames = []
	for i in range(1, len(names_no_wav) + 1):
		for comb1 in itertools.combinations(names_no_wav, i):
			newname = ' + '.join(comb1)
			combnames.append(newname)
	#print(combnames)

	combaudios = []
	for i in range(1, len(audios) + 1):
		for comb2 in itertools.combinations(audios, i):
			mix = sum(comb2)#/i
			combaudios.append(mix)
	print(combaudios)

	for i in range (0, len(combaudios)):
		size = len(combaudios[i])
		time = np.linspace(0, size, size, False)
		plt.plot(time, combaudios[i])
		plt.xlabel('Time (s)')
		plt.ylabel('Amplitude')
		plt.title(combnames[i])
		plt.show()
	
	
	
	
	
	
	#for i in range(0, len(names_no_wav)):
	#	name_inv = names_no_wav[i] + "_inv"
	#	names_no_wav.append(name_inv)
	#print(names_no_wav)

	#audios_inv = []
	#audios_inv.append(audios)
	#for i in range(0, len(audios)):
	#	audio_inv = np.multiply(audios[i], -1)
	#	audios_inv.append(audio_inv)
	#print(audios_inv)	

	#combnames_all = []
	#for comb3 in itertools.combinations(names_no_wav, len(names)):
	#	#print(comb3)
	#	cont=0
	#	for comb4 in itertools.combinations(comb3, 2):
	#		a = comb4[0]+"_inv"
	#		b = comb4[1]
	#		if a == b:
	#			cont=1
	#	if cont == 0:
	#		name_mix = ' + '.join(comb3)
	#		combnames_all.append(name_mix)
	#print(combnames_all)

	#teste = [[1,1,1],[2,2,2],[-1,-1,-1],[-2,-2,-2]]
	#print(teste)
	#combaudios_all = []
	#for comb5 in itertools.combinations(teste, len(audios)):
	#	#print(comb5)
	#	cont=0
	#	for comb6 in itertools.combinations(comb5, 2):
	#		#print(comb6)
	#		a = np.multiply(comb6[0], -1)
	#		b = comb6[1]
	#		if np.all(a == b):
	#			cont=1
	#		#print(cont)
	#	if cont == 0:
	#		mix = sum(comb5)
	#		combaudios_all.append(mix)
	#print(combaudios_all)

#		for value_tuple in comb3:
#			print(value_tuple)
#		print("---")

#	for i, audio in enumerate(combaudios):
#		filename = combnames[i] + ".wav"
#		sf.write(filename, audio, samplerate=tag.samplerate)

#	rms = []
#	for comb3 in combaudios:
#		rms_extracted = librosa.feature.rms(y=comb3,  hop_length=tag.samplerate)
#		rms.append(rms_extracted[0])
	#print(rms)

#	librosa.display.waveshow(rms[0], sr=tag.samplerate)
#	plt.show()
