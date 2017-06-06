import os
import numpy as np
import cv2
import json
from os.path import basename
from helper import File, Compressed

dir = "input/"
metric = []
for file in os.listdir(dir):
	if not file.startswith('.'):
		size = os.stat(dir + file).st_size
		original = File(file, size)
		dir_output = "output/" + basename(file.split('.')[0]) + "/"
		for output in os.listdir(dir_output):
			size_output = os.stat(dir_output + output).st_size
			original.addCompressed(Compressed(output, size_output))

		metric.append(original)

for file in metric:
	print ("Original image: " + file.name)
	for compressed in file.compressed:
		print ("Compressed image: " + compressed.name)
		print ("Size difference: " + str(compressed.diff))
		print ("Lossless error: " + str(compressed.error))
	print ("\n")