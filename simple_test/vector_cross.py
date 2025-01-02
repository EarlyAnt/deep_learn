import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f"sys path: {sys.path}\n")


from utils.datetime_util import sys_time

# 定义两个矩阵
vector1 = [[1], [2], [3]]
vector2 = [[4, 5, 6]]

# 计算结果矩阵的大小
rows = len(vector1)
cols = len(vector2[0])

# 初始化结果矩阵
result = [[0] * cols for _ in range(rows)]

# 执行矩阵乘法
for i in range(rows):
    for j in range(cols):
        for k in range(len(vector2)):
            result[i][j] += vector1[i][k] * vector2[k][j]

# 打印结果
print(f"[{sys_time()}] ->output result")
for row in result:
    print(row)
