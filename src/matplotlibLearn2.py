import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 包含狗，猫，猎豹的最高奔跑速度，对应的可视化颜色
speed_map = {"dog": (48, "#7199cf"),
             "cat": (45, "#4fc4aa"),
             "cheetah": (120, "#e1a7a2")}
# 设置图表的标题
fig = plt.figure("bar chart & pie chart")
# 在整张图中加入一个子图，121表示在一个1行2列的子图中的第一张
ax = fig.add_subplot(121)
ax.set_title("run speed - bar chart")
# 生成x轴的每个元素的位置
xticks = np.arange(3)
# 定义柱状图的每个柱子的宽度
bar_width = 0.5
# 动物名称
animalName = speed_map.keys()
# 动物速度
animalSpeed = [x[0] for x in speed_map.values()]
# 动物颜色
animalColor = [x[1] for x in speed_map.values()]
# 绘画柱状图，横轴是动物标签的位置，纵轴是速度，定义柱的宽度，
bars = ax.bar(xticks, animalSpeed, width=bar_width)
# 设置y轴标题
ax.set_ylabel("Speed(km/h)")
# 设置x轴的标签的位置
ax.set_xticks(xticks)
# 设置x轴每个标签的名字
ax.set_xticklabels(animalName)

# 设置x轴的范围
ax.set_xlim([bar_width / 2 - 1, 3 - bar_width / 2])
# 设置y轴的范围
ax.set_ylim([0, 125])

# 为每一个bar分配颜色(zip函数把两个可迭代对象一一对应打包成元素由元组组成的列表)
for bar, color in zip(bars, animalColor):
    bar.set_color(color)
# 在122位置重新加入一个图
ax = fig.add_subplot(122)
ax.set_title("run speed - pie chart")
labels = ["{}\n{}".format(name, speed) for name, speed in zip(animalName, animalSpeed)]
ax.pie(animalSpeed, labels=labels, colors=animalColor)
plt.show()
