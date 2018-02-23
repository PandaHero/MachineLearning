from numpy import *


# k近邻算法
# 训练样本数据
def createDataSet():
    # 训练数组
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # 训练标签
    labels = ["A", "A", "B", "B"]
    return group, labels


# knn算法
def classify(int_x, data_set, labels, k):
    '''

    :param int_x:分类数据
    :param data_set: 训练样本集
    :param labels: 标签
    :param k: 选择最近邻居的数目
    :return:
    '''
    # 训练样本的行数
    data_set_size = data_set.shape[0]
    # tile函数把输入数据扩展成和训练数据相同行数的矩阵，计算与训练样本数组的差值
    diffMat = tile(int_x, (data_set_size, 1)) - data_set
    # 计算差值矩阵的平方值
    sqDiffMat = diffMat ** 2
    # 计算差值矩阵中每一行元素的和
    sqDistance = sqDiffMat.sum(axis=1)
    # 计算距离平方矩阵的平方根
    distance = sqDistance ** 0.5
    # 对距离平方根矩阵从小到大排序,获得对应元素的下标
    sortDistanceIndex = distance.argsort()
    # 统计前k个结果的投票数
    classCount = {}
    for i in range(k):
        # 获取排序后的前k个下标值
        index = sortDistanceIndex[i]
        # 对应下标值的标签
        voteLabels = labels[index]
        # 计算求和标签的个数，保存到字典
        classCount[voteLabels] = classCount.get(voteLabels, 0) + 1
    # 对字典中的value进行排序(从大到小)
    sortClassCount = sorted(classCount.items(), key=lambda classCount: classCount[1], reverse=True)
    return sortClassCount[0][0]


if __name__ == '__main__':
    k = 3
    group, labels = createDataSet()
    x = array([0, 0])
    print(classify(x, group, labels, k))
