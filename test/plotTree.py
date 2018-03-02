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


def createPlot():
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon=False)
    plotNode("决策节点", (0.5, 0.1), (0.1, .5), decisionNode)
    plotNode("叶节点", (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


if __name__ == '__main__':
    createPlot()
