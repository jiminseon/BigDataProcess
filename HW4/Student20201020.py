import numpy as np
import operator
import os
import sys

fileList = os.listdir(sys.argv[2])

trainingFolder = os.listdir(sys.argv[1])

def trainingToMatrix(filename):
	f = open(filename)
	numberOfLines = len(f.readlines())-1 
	mat = np.zeros((1, numberOfLines*32))
	f = open(filename)
	index = 0
	trainingList = []
	for line in f.readlines():
		a = list(line)
		for i in a:
			if (i != '\n'):
				trainingList.append(float(i))
	mat[index, :] = trainingList
	return mat


def fileToMatrix(foldername):
	f = open(foldername+"/"+fileList[0])
	numberOfLines = len(f.readlines())-1 
	num = len(fileList)
	mat = np.zeros((num, numberOfLines*32))
	classLabel = []
	index = 0
	for i in range(0, num):
		f = open(foldername+"/"+fileList[i])
		trainingList = []
		for line in f.readlines():
			a = list(line)
			for j in a:
				if (j != '\n'):
					trainingList.append(float(j))
		mat[index, :] = trainingList
		classLabel = fileList[i]
		index += 1
	return mat, classLabel

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
		sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

group, labels = fileToMatrix(sys.argv[2])
error = {}

for i in range(len(trainingFolder)):
	inputData = trainingToMatrix(sys.argv[1]+"/"+trainingFolder[i])
	real = trainingFolder[i].split("_")
	real = int(real[0])
	for i in range(1, 21):
		predict = classify0(inputData, group, labels, i)
		if (real != int(predict)):
			error[i] = error.get(i, 0) + 1
for i in range(1, 21):
	print(int(error[i])/len(trainingFolder)*100)
