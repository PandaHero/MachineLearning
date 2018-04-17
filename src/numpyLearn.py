import numpy as np
import numpy.random as random

# 创建一维数组
a = np.array([1, 2, 3, 4])  # [2 3 4]
b = np.array((2, 3, 4))  # [2 3 4]
# 创建二维数组
c = np.array([[1, 2, 3], [4, 5, 6]])  # [[1 2 3] [3 4 5]]
# 创建一个从0到3的数组
d = np.arange(4)  # [0 1 2 3]
e = np.arange(24).reshape(2, 3, 4)  # [[[0 1 2 3] [4 5 6 7] [8 9 10 11]] [[12 13 14 15] [16 17 18 19] [20 21 22 23]]]

# 3*4的二维数组，初始化所有元素的值为0
zero_arr = np.zeros((3, 4))  # [[0  0  0  0][0 0 0 0][0 0 0 0]]
# 2*3的整数型二维数组，初始化所有元素的值为1
one_arr = np.ones((2, 3), dtype="int32")  # [[1 1 1][1 1 1]]
# 4*4二维数组，主对角元素的值均为1，其它元素值为0
eye_arr = np.eye(4)  # [[1 0 0 0][0 1 0 0][0 0 1 0][0 0 0 1]]
# 创建一个一维数组，元素值为3重复4次
print(np.repeat(3, 4))  # [3 3 3 3]
# 创建一个等差数组，0到6之间取5个值
print(np.linspace(0, 6, 5))

# 创建随机数组(4*4)
random_arr = np.random.rand(4, 4)
print(random_arr)
# 将数组转换成矩阵
aMat = np.matrix(a)

# 数组的行列数
print(b.shape, a.shape)
# 数组的秩
print(b.ndim)
# 数组的列数
print(a.itemsize)
# 数组中元素的个数
print(a.size)
# 数组的类型，数组中元素的类型
print(type(a), a.dtype)

# 数组中按照行的最大值
print(c.max(axis=1))
# 数组中按照列的最大值
print(c.max(axis=0))
# 按照行的均值
print(c.mean(axis=1))
# 按照列的均值
print(c.mean(axis=0))
print(np.abs(-1))  # 绝对值
print(np.sin(np.pi / 2))  # sin函数
print(np.arctan(1))  # 逆函数
print(np.exp(3))  # 指数函数
print(np.power(2, 3))  # 幂函数
print(np.dot(a, d))  # 点积
print(np.sqrt(25))  # 开方函数
print(np.sum(a))  # 求和函数
print(np.mean(a))  # 平均值函数
print(np.std(a))  # 方差函数

# 展开一个numpy数组为1维数组(返回结果为拷贝，不影响原始数组)
print(c.flatten())
# 展开一个可解析的结构为1维数组(返回结果为视图，修改视图会改变原始数组)
print(np.ravel(c))
# 更改数组的元素类型
print(c.astype(np.float), c.astype(np.float))

# 读取与保存
np.save(r"C:\Users\chen\Desktop\save.npy", c)
np.load(r"C:\Users\chen\Desktop\save.npy")

# 数组操作(e = np.arange(24).reshape(2, 3, 4))
print(e[1][1][1])  # 17
print(e[:, 2, :])  # [[8 9 10 11][20 21 22 23]]
print(e[:, :, 1])  # [[1 5 9][13 17 21]]
print(e[..., 1])  # [[1 5 9][13 17 21]]
print(e[:, 1:, 1:-1])  # [[[5 6][9 10]][[17 18][21 22]]]
print(np.split(e, 2))  # 把数组平均划分为2份
print(np.vstack((d, a)))  # 数组按照纵轴拼接[[0 1 2 3][1 2 3 4]]
print(np.hstack((d, a)))  # 数组按照横轴拼接[0 1 2 3 1 2 3 4]
print(np.concatenate((d, a), axis=0))
print(np.stack((a, d)))
print(e.transpose((2, 0, 1)))  # 转置
print(e[0].transpose())  # 指定楼层转置
print(np.rot90(c, 3))  # [[4 1][5 2][6 3]](逆时针旋转3次)
print(np.fliplr(c))  # 按照纵轴左右翻转
print(np.flipud(c))  # 按照水平轴上下翻转

# 数组运算(a=[0,1,2,3],d=[1,2,3,4])
print(a + d, a - d, a * d, a ** 2)  # 对应位置元素运算
print(c + b)  # 广播机制(c=[[1 2 3][4  5 6]],b=[2 3 4])

# 设置随机数种子
num = 8
while num > 5:
    randSeed = random.seed(1)
    print(random.rand(2, 4))
    num -= 1
print(random.random())  # 产生一个0~1之间的随机数
randArr = random.rand(1, 3)  # 1*3的随机数数组
print(random.random((2, 2)))  # 2*2的随机数数组
print(random.sample((2, 2)))  # 2*2的随机数数组
print(random.random_sample((2, 2)))  # 2*2的随机数数组
print(random.ranf((2, 2)))  # 2*2的随机数数组
print(5 * random.random(10) + 1)  # 产生长度为10的随机数数组
print(random.uniform(1, 6, 10))  # 产生长度为10取值范围[1,6)的随机数数组
