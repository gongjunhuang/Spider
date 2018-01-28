from numpy import *

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help'],
                   ['maybe', 'not', 'take', 'him', 'to', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

def createVocalList(dataSet):
    # 创建一个空集
    vocalSet = set([])
    # 两个集合的并集
    for document in dataSet:
        vocalSet = vocalSet | set(document)
    return list(vocalSet)

def setOfWords2Vec(vocalList, inputSet):
    # 创建一个全为0的向量
    returnVec = [0]*len(vocalList)
    for word in inputSet:
        if word in vocalList:
            returnVec[vocalList.index(word)] = 1
        else:
            print("the word: %s is not in my vocabulary" % word)
    return returnVec

def trainNB0(trainMat, trainCate):
    numberTrainDocs = len(trainMat)
    numberTrainWords = len(trainMat[0])
    pAbusive = sum(trainCate) / float(numberTrainDocs)
    p0Num = ones(numberTrainWords)
    p1Num = ones(numberTrainWords)
    p0Demon = 2.0
    p1Demon = 2.0
    for i in range(numberTrainDocs):
        if trainCate[i] == 1:
            p1Num += trainMat[i]
            p1Demon += sum(trainMat[i])
        else:
            p0Num += trainMat[i]
            p0Demon += sum(trainMat[i])

    p1Vect = log(p1Num / p1Demon)
    p0Vect = log(p0Num / p0Demon)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2classify, p0Vec, p1Vec, pClass):
    p1 = sum(vec2classify * p1Vec) + log(pClass)
    p0 = sum(vec2classify * p0Vec) + log(1.0 - pClass)
    if p1 > p0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    listPosts, listClasses = loadDataSet()
    myVocalList = createVocalList(listPosts)
    listR = setOfWords2Vec(myVocalList, listPosts[0])

    trainMat = []
    for postInDoc in listPosts:
        trainMat.append(setOfWords2Vec(myVocalList, postInDoc))
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocalList, testEntry))
    print(thisDoc)
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocalList, testEntry))
    print(thisDoc)
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
