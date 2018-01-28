import re
import random
from numpy import *

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

def textParse(filename):
    emailText = open(filename, encoding='utf-8').read()
    regEx = re.compile(r"\W*")
    listOfTokens = regEx.split(emailText)
    wordList = [tok.lower() for tok in listOfTokens if len(tok) > 0]
    return wordList

def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        wordList = textParse("C:\\Users\\JOE\\Downloads\\email\\spam\\%d.txt" % i)
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse("C:\\Users\\JOE\\Downloads\\email\\ham\\%d.txt" % i)
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    vocalList = createVocalList(docList)
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])

    trainingMat = []
    trainingClass = []
    for docIndex in trainingSet:
        trainingMat.append(setOfWords2Vec(vocalList, docList[docIndex]))
        print(trainingMat)
        trainingClass.append(classList[docIndex])
    p0v, p1v, pSpam = trainNB0(array(trainingMat), array(trainingClass))
    errorCount = 0

    for docIndex in testSet:
        wordVec = setOfWords2Vec(vocalList, docList[docIndex])
        if classifyNB(array(wordVec), p0v, p1v, pSpam) != classList[docIndex]:
            errorCount += 1

    print("the error rate is:", float(errorCount) / len(testSet))

if __name__ == '__main__':
    spamTest()
