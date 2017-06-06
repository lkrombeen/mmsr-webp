import os
import numpy as np
import cv2
from os.path import basename

class File():
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.compressed = []

	def addCompressed(self, file):
		dir_output = "output/" + basename(self.name.split('.')[0]) + "/"
		file.diff = self.size - file.size
		image_original = cv2.imread("input/" + self.name)
		image_compressed = cv2.imread(dir_output + file.name)

		file.error = self.compute_error(image_original, image_compressed)
		self.compressed.append(file)

	def compute_error(self, image0, image1):
		number_of_channels = np.shape(image0)[2]
		total_error = 0
		for channel_index in range(number_of_channels):
			error = np.abs(image0[:,:,channel_index] - image1[:,:,channel_index])
			total_error = total_error + (np.average(error)/(np.max(error) - np.min(error)))

		return (total_error/number_of_channels)

class Compressed():
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.diff = 0
		self.error = 0