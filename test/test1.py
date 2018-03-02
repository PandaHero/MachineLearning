from math import log


# 创建数据集（原始）
def createDataSet():
    dataSet = [[1, 1, "yes"], [1, 1, "yes"], [0, 1, "no"], [1, 0, "no"], [0, 1, "no"]]
    labels = ["no surfacing", "flippers"]
    return dataSet, labels


# 计算数据集的信息熵
def calcShannonEnt(dataSet):
    # 获取数据集的长度
    dataSetLen = len(dataSet)
    # 创建字典保存数据集最后一列的数值
    labelCount = {}
    # 遍历数据集
    for featVec in dataSet:
        labelCount[featVec[-1]] = labelCount.get(featVec[-1], 0) + 1
    # 初始化信息熵值
    shannonEnt = 0
    # 计算该数据集的信息熵
    for key in labelCount.keys():
        prob = labelCount[key] / dataSetLen
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    '''

    :param dataSet: 数据集
    :param axis: 数据集的列
    :param value:数据集的列值
    :return:返回指定特征下的数据集
    '''
    # 创建数组保存按指定特征划分后的数据集
    retDataSet = []
    # 遍历给定数据集
    for featVec in dataSet[:]:
        # 如果该值等于给定数据集的列值
        if featVec[axis] == value:
            # 保存该值到数据集中
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
            # # 若featVec中有两个相同元素，则remove删掉第一个元素（慎用）
            # featVec.remove(value)
            # retDataSet.append(featVec)
    return retDataSet


# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    # 获取数据集中的特征个数
    numFeatures = len(dataSet[0]) - 1
    # 计算初始数据集的信息熵
    baseEntropy = calcShannonEnt(dataSet)
    # 最好信息增益
    bestInfoGain = 0
    # 最好的特征
    bestFeature = -1
    # 遍历
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        # 用set去掉重复值
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            # 给定列值划分数据集
            subDataSet = splitDataSet(dataSet, i, value)
            newEntropy += float(len(subDataSet) / len(dataSet)) * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        classCount[vote] = classCount.get(vote, 0) + 1
    sortClassCount = sorted(classCount.items(), key=lambda value: value[1], reverse=True)
    return sortClassCount


if __name__ == '__main__':
    dataSet, labels = createDataSet()
    print(calcShannonEnt(dataSet))
    print(splitDataSet(dataSet, 0, 1))
    print(chooseBestFeatureToSplit(dataSet))
