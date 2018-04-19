import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 从[-1,1]中等距离的取出50个值
x = np.linspace(-1, 1, 50)
y_1 = x * 2 + 1
# x:横坐标值,y:纵坐标值
# plt.plot(x, y_1)
# 显示对象
# plt.show()

# y_2 = x ** 2 + 1
# # 从新获取一个图像对象，用于画图(第一个值表示编号，第二个值表示图标的宽度)
# plt.figure(num=3, figsize=(8, 5))
# plt.plot(x, y_2)
# # 设置线条颜色，线条宽度，线条样式
# plt.plot(x, y_1, color="red", linewidth=1.0, linestyle="--")
# # 生成两张图
# # 设置横纵坐标标签
# plt.xlabel("i am x")
# plt.ylabel("i am y")
# # 绘制多条曲线
# # 设置横纵取值参数范围
# plt.xlim((-1, 2))
# plt.ylim((1, 3))
# # 设置点的位置
# new_ticks = np.linspace(-1, 2, 5)
# plt.xticks(new_ticks)
# plt.show()
# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
# x采样，等差数列
x = np.linspace(0, 5, 100)
# 生成y的样本数据
y = np.sin(x) * 2 + 0.3 * x ** 2
y_data = y + np.random.normal(scale=0.3, size=100)

# 设置图表名称
plt.figure("data")
# "."标明画散点图，每个散点的形状是圆
plt.plot(x, y_data,".")

# 画模型的图，plot函数默认画连线图
plt.figure("model")
plt.plot(x, y)

# 两个图画在一起
plt.figure("data & model")
# 通过K指定线条的颜色，lw指定线的宽度
plt.plot(x,y,color="black",linewidth=3,linestyle="--")
# scatter生成散点图
plt.scatter(x,y_data)
# 保存当前图片
plt.savefig(r"C:\Users\chen\Desktop\save.png")
plt.show()

