from __future__ import division
import os
import numpy as np
import cv2
import json
from os.path import basename
from helper import File, Compressed

dir = "input/"
header = "Original Image;"
results = ""
formats = ["jpg", "png", "bmp", "webp"]
qualities = ["100", "80", "50"]

for format in formats:
	for quality in qualities:
		header += format + "-" + quality + " Size Diff;"
		header += format + "-" + quality + " Size Diff (%);"
		header += format + "-" + quality + " Error;"

header += "WEBP Size Diff;WEBP Size Diff (%);WEBP Error\n"

for file in os.listdir(dir):
	if not file.startswith('.'):
		size = os.stat(dir + file).st_size
		original = File(file, size)
		file_nonformat = basename(file.split('.')[0])
		dir_output = "output/" + file_nonformat + "/"
		result = file

		for format in formats:
			for quality in qualities:
				output = file_nonformat + "-quality" + quality + "." + format
				size_output = os.stat(dir_output + output).st_size
				compressed = original.addCompressed(Compressed(output, size_output))
				result += ";" + str(compressed.diff) + ";" + str(np.round((compressed.diff / size) * 100, decimals = 2)) + ";" + str(compressed.error)

		output = file_nonformat + ".webp"
		size_output = os.stat(dir_output + output).st_size
		compressed = original.addCompressed(Compressed(output, size_output))
		result += ";" + str(compressed.diff) + ";" + str(np.round((compressed.diff / size) * 100, decimals = 2)) + ";" + str(compressed.error)

		results += result + "\n"
		with open(dir_output + "/results.csv", "w") as text_file:
			text_file.write(header + result)

with open("output/results.csv", "w") as text_file:
	text_file.write(header + results)
