# 计算给定数据集的信息熵
from math import log


# 创建测试数据集
def createDataSet():
    # 最后一列出现不同标签的数量越高，则熵越大，代表无序程序越高，我们在数据集中添加的分类就越多
    dateSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [0, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']
               ]
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
    # 用所有标签的概率计算信息熵
    shannoEnt = 0.0
    # 计算所有标签出现的频次分别计算出现的概率，然后计算信息熵
    for key in labelCounts.keys():
        # 不同标签出现的概率
        prob = float(labelCounts[key]) / numEntries
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
            reduceFeatVec = featVec[:axis]
            # 把两个列表合并
            reduceFeatVec.extend(featVec[axis + 1:])
            # 把合并后的列表添加到列表中
            retDataSet.append(reduceFeatVec)
    return retDataSet


if __name__ == '__main__':
    dateSet, labels = createDataSet()
    print(calcShannonEnt(dateSet))
    splitDataSet = splitDataSet(dateSet, 0, 1)
    print(splitDataSet, type(splitDataSet))
