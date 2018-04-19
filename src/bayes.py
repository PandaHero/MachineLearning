# #####################
# naive bayesian model#
# #####################
import numpy as np


# 加载数据
def loadDataSset():
    '''

    :return:
        postingList:输入文本数据
        classVec:输出标签数据
    '''
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1代表侮辱性文字，0代表正常言论
    return postingList, classVec


# 词汇表(创建一个包含所有样本词语的字典)
def createVocabList(dataSet):
    '''

    :param dataSet: 输入文本数据
    :return:
        vacabSet:包含所有无重复文本数据的集合
    '''
    # 创建空集合用来保存文本数据
    vocabSet = set([])
    for document in dataSet:
        # 位运算
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


# 样本数据向量化(0-1)
def setOfWords2Vec(vocabList, inputSet):
    '''

    :param vocabList: 每个文本数据列表
    :param inputSet: 无重复的所有文本数据集合
    :return:
        returnVec:文本向量，向量元素为1或者0
    '''
    # 初始化一个和词汇表相同大小的向量
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec


# 朴素贝叶斯分类器训练函数
def trainNBO(trainMatrix, trainCategory):
    '''

    :param trainMatrix: 训练数据矩阵
    :param trainCategory: 训练数据类标签
    :return:
        p0Vect:分类标签为0的每个特征的概率值
        p1Vect：分类标签为1的每个特征的概率值
        pAbusive：分类的先验概率


    '''
    # 计算文档的个数(矩阵)
    numTrainDocs = len(trainMatrix)
    # 计算垃圾邮件占全部邮件的比例(p(y=1))
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 每个文档的单词数
    numWords = len(trainMatrix[0])
    # 属于分类0的所有文本的词向量
    p0Num = np.ones(numWords)
    # 属于分类1的所有文本的词向量
    p1Num = np.ones(numWords)
    # 分类为0的所有单词数统计(拉普拉斯)
    p0Denom = 2
    # 分类为1的所有单词数统计
    p1Denom = 2
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # print(trainMatrix[i])
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # print(p0Num, p1Num)
    # print(p0Denom, p1Denom)
    # 计算每个单词在不同类标签下的概率值
    p0Vect = np.log(p0Num / p0Denom)
    p1Vect = np.log(p1Num / p1Denom)
    return p0Vect, p1Vect, pAbusive


# 朴素贝叶斯分类器测试函数
def classifyNB(ve2Classify, p0Vect, p1Vect, pAbusive):
    # 分类为0的概率
    p0 = sum(ve2Classify * p0Vect) + np.log(pAbusive)
    # 分类为1的概率
    p1 = sum(ve2Classify * p1Vect) + np.log(pAbusive)
    if p0 > p1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    postingList, classVec = loadDataSset()
    # 词汇表
    myVocabList = createVocabList(postingList)
    # print(myVocabList)
    # 文本数据向量化
    trainMatrix = []
    for postInDoc in postingList:
        returnVec = setOfWords2Vec(myVocabList, postInDoc)
        trainMatrix.append(returnVec)
    p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, classVec)
    testEntry = ["stupid"]
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    testLabel = classifyNB(thisDoc, p0Vect, p1Vect, pAbusive)
    print(testLabel)
