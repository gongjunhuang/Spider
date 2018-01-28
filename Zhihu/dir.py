from numpy import *
import os
import operator

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet # 将分类向量拓展到训练集同一个维度，求差
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('E:\\BaiduNetdiskDownload\\源码\\第7周\\traindata')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        filenameStr = trainingFileList[i]
        fileStr = filenameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector("E:\\BaiduNetdiskDownload\\源码\\第7周\\traindata\\%s" % filenameStr)
    testFileList = os.listdir('E:\\BaiduNetdiskDownload\\源码\\第7周\\testdata')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        filenameStr = testFileList[i]
        fileStr = filenameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vecUnderTest = img2vector("E:\\BaiduNetdiskDownload\\源码\\第7周\\testdata\\%s" % filenameStr)
        classifierResult = classify(vecUnderTest, trainingMat, hwLabels, 4)
        print('the classifier came back with: %d, the real answer is: %d' %(classifierResult, classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1
    print('\nthe total number of errors is: %d\n' % errorCount)
    print('the total error rate is: %f'% (errorCount / float(mTest)))

if __name__ == '__main__':
    handwritingClassTest()