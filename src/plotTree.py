import matplotlib.pyplot as plt

# 设置文本框格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
# 设置箭头格式
arrow_args = dict(arrowstyle="<-")


# 绘制带箭头的注释
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.axl.annotate(nodeTxt, xy=parentPt, xycoords="axes fraction", xytext=centerPt,
                            textcoords='axes fraction', va="center", ha='center', bbox=nodeType, arrowprops=arrow_args)


# 找到父节点和子节点之间的中间位置，放置0或1
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


# 计算所有叶节点的位置，并绘画叶节点以及0和1的位置
def plotTree(myTree, parentPt, nodeTxt):
    # 计算宽和高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys)[0]
    # 计算子节点的位置
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)


def createPlot():
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon=False)
    plotNode("决策节点", (0.5, 0.1), (0.1, .5), decisionNode)
    plotNode("叶节点", (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


# 获取叶节点的数目
def getNumLeafs(myTree):
    # print(myTree)
    # 设置叶节点的初始值
    numLeafs = 0
    # 获取树的第一层内节点
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        # 检查元素数据类型是否是字典
        if isinstance(secondDict[key], dict):
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


# 获取树的层数
def getTreeDepth(myTree):
    print(myTree)
    # 初始化树的层数
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key], dict):
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


# 用于测试的数据集
def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                   ]
    return listOfTrees[i]


if __name__ == '__main__':
    # 获取测试数据集
    myTree01 = retrieveTree(0)
    # 获取数据集中树的层数
    treeDepth = getTreeDepth(myTree01)
    # 获取数据集中叶节点的数目
    numLeafs = getNumLeafs(myTree01)
    print(treeDepth, numLeafs)
