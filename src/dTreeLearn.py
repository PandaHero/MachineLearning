# 计算给定数据集的信息熵
from math import log


# 创建测试数据集
def createDataSet():
    # 最后一列出现不同标签的数量越高，则熵越大，代表无序程序越高，我们在数据集中添加的分类就越多
    dateSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dateSet, labels


# 计算信息熵
def calcShannonEnt(dataSet):
    # 获取数据集中的实例个数
    numEntries = len(dataSet)
    # 初始化一个字典用于存储键值和对应出现次数
    labelCounts = {}
    # 遍历数据集
    for featVec in dataSet:
        # 获取每行的最后一个数值,作为键值
        currentLabel = featVec[-1]
        labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1
    # print(labelCounts)
    # 用所有标签的概率计算信息熵
    shannoEnt = 0.0
    # 计算所有标签出现的频次分别计算出现的概率，然后计算信息熵
    for key in labelCounts.keys():
        # 不同标签出现的概率
        prob = float(labelCounts[key] / numEntries)
        # 计算以2为底的对数
        shannoEnt -= prob * log(prob, 2)
    return shannoEnt


# 获取按照不同标签划分后的数据集
def splitDataSet(dateSet, axis, value):
    '''
    :param dateSet: 待划分的数据集
    :param axis: 划分数据集的特征(标签)
    :param value:划分数据集的特征值
    :return:按照不同标签划分的数据集
    '''
    # 创建空列表，用于保存按照不同标签划分后的数据集
    retDataSet = []
    # 遍历待划分的数据集
    for featVec in dateSet:
        # 若待划分的数据集特征值等于给定特征值，则把结果保存到retDataSet中
        if featVec[axis] == value:
            # 当axis为0时,reduceFeatVec为空值
            reduceFeatVec = featVec[:axis]
            # 把两个列表合并
            reduceFeatVec.extend(featVec[axis + 1:])
            # 把合并后的列表添加到列表中
            retDataSet.append(reduceFeatVec)
    return retDataSet


# 计算特征值、划分数据集、计算最好的划分数据集的特征(实现了一层树的最好划分方式)
def chooseBestFeatureToSplit(dataSet):
    # 计算数据集中特征的数量，最后一列是标签值
    numFeatures = len(dataSet[0]) - 1
    # 计算原始数据集的信息熵(原始)
    baseEntropy = calcShannonEnt(dataSet)
    # 初始化最佳信息增益和最佳特征索引
    bestInfoGain = 0.0
    bestFeature = -1
    # 遍历所有特征
    for i in range(numFeatures):
        # 把第i个索引对应的值提取出来
        featList = [example[i] for example in dataSet]
        # 把提出来的值唯一化
        uniqueVals = set(featList)
        # print("--", uniqueVals)
        # 初始化新熵
        newEntropy = 0.0
        # 遍历每一个特征属性中的特征值，对每一个特征划分一次数据集
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # 计算子集占总集的元素数量百分比
            prob = float(len(subDataSet) / len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        # 计算信息增益,信息增益越大，表示用特征属性(i)来划分数据集纯度提升越大
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# 得到每一个类标签出现的次数,返回出现次数最多的分类名称(最后得到的数据子集中类标签依旧不唯一)
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        classCount[vote] = classCount.get(vote, 0) + 1
    # 从大到小排序
    sortedClassCount = sorted(classCount.items(), key=lambda classCount: classCount[1], reverse=True)
    # 返回出现频率最大的那个标签作为子集的标签
    return sortedClassCount[0][0]


# 创建树的函数
def createTree(dataSet, labels):
    # 三种情况会导致递归返回
    # 1、当前结点包含的样本全部属于同一个标记，无需划分
    # 2、当前属性集为空，或者所有样本在所有属性上取值相同，无法划分
    # 3、当前节点包含的样本集合为空，不能划分
    # 提取数据集中的最后一列元素（标记）
    classList = [example[-1] for example in dataSet]
    # 若数据集中的标记完全相同则停止划分
    if classList.count(classList[0]) == len(classList):
        # print("正在调用", classList[0])
        return classList[0]
    # 遍历完所有特征时返回出现次数最多的标签
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # 使用字典存储树的信息
    myTree = {bestFeatLabel: {}}
    # 删除数据集中最好特征值对应的标签值
    del (labels[bestFeat])
    # 获取最好特征对应的那一列数据组成列表
    featValues = [example[bestFeat] for example in dataSet]
    # 唯一化
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # 复制类标签
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


# 获取叶节点的数目
def getNumLeafs(myTree):
    # 设置叶节点的初始值
    numLeafs = 0
    # 获取树的第一层内节点
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key],dict):
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


if __name__ == '__main__':
    dataSet, labels = createDataSet()
    # print(calcShannonEnt(dataSet))
    # # splitDataSet = splitDataSet(dataSet, 0, 1)
    # # print(splitDataSet, type(splitDataSet))
    # print(chooseBestFeatureToSplit(dataSet))
    myTree = createTree(dataSet, labels)
    print(myTree)
    print(getNumLeafs(myTree))
