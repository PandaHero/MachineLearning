from numpy import *
import matplotlib.pyplot   as plt


def loadDateSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1
    dataMat = []
    labelMat = []
    for line in open(fileName).readlines():
        lineArr = []
        # 切分的每一个元素类型为str
        curLineList = line.strip().split("\t")
        for num in range(numFeat):
            # 把字符串转换成浮点数
            lineArr.append(float(curLineList[num]))
        dataMat.append(lineArr)
        labelMat.append(float(curLineList[-1]))
    return dataMat, labelMat


# 计算普通回归参数
def standRegres(dataMat, labelMat):
    xMat = mat(dataMat)
    # 矩阵转置
    yMat = mat(labelMat).T
    xTx = xMat.T * xMat
    # 计算xTx的行列式是否为0，不为0则可逆
    if linalg.det(xTx) == 0.0:
        print("xMat cannot do inverse")
        return
    # 最小二乘法计算w(矩阵的逆)
    w = xTx.I * (xMat.T * yMat)
    # w = linalg.solve(xTx, xMat.T * yMat)
    return w


# 局部加权线性回归函数
def lwlr(testPoint,xArr,yArr,k=1):
    xMat=mat(xArr)
    yMat=mat(yArr).T
    # 获取样本个数
    sampleNum=shape(xMat)[0]


if __name__ == '__main__':
    dataMat, labelMat = loadDateSet(r"C:\Users\chen\Desktop\ex0.txt")
    w = standRegres(dataMat, labelMat)
    xMat = mat(dataMat)
    # y的真实值
    yMat = mat(labelMat)
    # y的估计值
    yHat = xMat * w
    # 获取图形对象,绘制数据散点图
    figure = plt.figure()
    ax = figure.add_subplot(111)
    print(type(xMat[:, 1].flatten().A[0]), yMat.T[:, 0].flatten().A[0].shape)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    # ax.plot(xMat[:, 1], yHat)
    # plt.show()
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * w
    ax.plot(xCopy[:, 1], yHat)
    plt.show()
