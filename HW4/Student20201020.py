import kNN
import numpy as np

def fileToMatrix(filename):
    f = open(filename)
    numberOfLines = len(f.readlines())
    returnMat = np.zeros((numberOfLines, 33))
    classLabelVector = []
	f = open(filename)
    index = 0
    for line in f.readlines():
        line = str.strip(line)
        listFromLine = list(line)
        returnMat[index, :] = listFromLine[0:33]
	    classLabelVector.append(listFromLine[-1])
	    index += 1
    return returnMat, classLabelVector

datingDataMat, datingLabels = fileToMatrix('trainingDigits/0_0.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

inputData = input()
inputArray = np.array([float (i) for i in inputData.split()])
for i in range(len(inputArray)):
    inputArray[i] = (inputArray[i] - minVals[i]) / ranges[i]
print(kNN.classify0(inputArray, normMat, datingLabels, 3))
