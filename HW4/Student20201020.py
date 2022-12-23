import numpy as np
import operator
import os
import sys
import math

fileList = os.listdir(sys.argv[2])

trainingFile = os.listdir(sys.argv[1])

def testToMatrix(filename):
	f = open(filename)
	numberOfLines = len(f.readlines()) 
	mat = np.zeros((1, numberOfLines*32))
	f = open(filename)
	index = 0
	testList = []
	for line in f.readlines():
		a = list(line)
		for i in a:
			if (i != '\n'):
				testList.append(float(i))
	mat[index, :] = testList
	return mat


def fileToMatrix(foldername):
	f = open(foldername+"/"+trainingFile[0])
	numberOfLines = len(f.readlines())
	num = len(trainingFile)
	mat = np.zeros((num, numberOfLines*32))
	classLabel = []
	index = 0
	for i in range(0, num):
		f = open(foldername+"/"+trainingFile[i])
		trainingList = []
		for line in f.readlines():
			a = list(line)
			for j in a:
				if (j != '\n'):
					trainingList.append(float(j))
		mat[index, :] = trainingList
		fileNum = trainingFile[i].split("_")
		classLabel.append(int(fileNum[0]))
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

group, labels = fileToMatrix(sys.argv[1])
error = {}

for i in range(len(fileList)):
	inputData = testToMatrix(sys.argv[2]+"/"+fileList[i])
	real = fileList[i].split("_")
	real = int(real[0])
	for i in range(1, 21):
		predict = classify0(inputData, group, labels, i)
		if (real != int(predict)):
			error[i] = error.get(i, 0) + 1
		else:
			error[i] = error.get(i, 0) + 0
for i in range(1, 21):
	print(math.trunc(int(error[i])/len(fileList)*100))
	
