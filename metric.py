from __future__ import division
import os
import numpy as np
import cv2
import json
from os.path import basename
from helper import File, Compressed

dir = "input/"
header = "Original Image;JPEG-100 Size Diff;JPEG-100 Size Diff (%);JPEG-100 Error;JPEG-80 Size Diff;JPEG-80 Size Diff (%);JPEG-80 Error;JPEG-50 Size Diff;JPEG-50 Size Diff (%);JPEG-50 Error;PNG-100 Size Diff;PNG-100 Size Diff (%);PNG-100 Error;PNG-80 Size Diff;PNG-80 Size Diff (%);PNG-80 Error;PNG-50 Size Diff;PNG-50 Size Diff (%);PNG-50 Error;BMP-100 Size Diff;BMP-100 Size Diff (%);BMP-100 Error;BMP-80 Size Diff;BMP-80 Size Diff (%);BMP-80 Error;BMP-50 Size Diff;BMP-50 Size Diff (%);BMP-50 Error;WEBP Size Diff;WEBP Size Diff (%);WEBP Error\n"
results = ""

for file in os.listdir(dir):
	if not file.startswith('.'):
		size = os.stat(dir + file).st_size
		original = File(file, size)
		file_nonformat = basename(file.split('.')[0])
		dir_output = "output/" + file_nonformat + "/"
		result = file

		for format in ["jpg", "png", "bmp"]:
			for quality in ["100", "80", "50"]:
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