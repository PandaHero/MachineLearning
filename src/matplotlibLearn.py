import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距离的取出50个值
x = np.linspace(-1, 1, 50)
# print(x)
y_1 = x * 2 + 1
# x:横坐标值
# y:纵坐标值
# plt.plot(x, y_1)
# 显示对象
# plt.show()
# '''''''''''''''
y_2 = x ** 2 + 1
# 从新获取一个图像对象，用于画图(第一个值表示编号，第二个值表示图标的宽度)
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y_2)
# 设置线条颜色，线条宽度，线条样式
plt.plot(x, y_1, color="red", linewidth=1.0, linestyle="--")
# 生成两张图
# 设置横纵坐标标签
plt.xlabel("i am x")
plt.ylabel("i am y")
# 绘制多条曲线
# 设置横纵取值参数范围
plt.xlim((-1, 2))
plt.ylim((1, 3))
# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.show()
