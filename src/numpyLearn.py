import numpy as np

# 创建一维数组
a = np.array([2, 3, 4])
print(a)
b = np.array((2, 3, 4))
print(b)
# 创建二维数组
c = np.array([[1, 2, 3], [3, 4, 5]])
# 创建一个从0到3的数组
d = np.arange(4)
e = np.arange(24).reshape(2, 3, 4)
print(e)
# 创建0数组(3行4列)
zero_arr = np.zeros((3, 4))
print(zero_arr)
# 创建1数组
one_arr = np.ones((2, 3, 4), dtype="int32")
print(one_arr)
# 创建对角数组
eye_arr = np.eye(4)
print(eye_arr)
# 创建随机数组
random_arr = np.random.rand(4, 4)
print(random_arr)
# 数组得行列数
print(b.shape, a.shape)
# 数组得秩
print(b.ndim)
# 数组的列数
print(a.itemsize)
# 数组中元素的个数
print(a.size)
# 数组的类型，数组中元素的类型
print(type(a), a.dtype)
# 将数组转换成矩阵
print(np.matrix(a))
