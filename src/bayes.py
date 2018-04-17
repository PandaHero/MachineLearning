import numpy as np


def loadDataSset():
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1代表侮辱性文字，0代表正常言论
    return postingList, classVec

# 词汇表
def createVocabList(dataSet):  # 创建一个包含在所有文档中出现的不重复词的列表，使用set数据集合。
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 向量化
def setOfWords2Vec(vocabList, inputSet):
    # 初始化一个和词汇表相同大小的向量
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec


if __name__ == '__main__':
    postingList, classVec = loadDataSset()
    # 词汇表
    myVocabList = createVocabList(postingList)
    returnVec = setOfWords2Vec(myVocabList, postingList[1])
    print(returnVec)
