#!/usr/bin/python
# 数据类型

# #################################################### 标准数据类型
# --------------- 数字类型 Number

# 整数  int python3 中只有 int类型，
a = - 1000000000000000000000000
# type()  函数查询类型
print(a, type(a))
# 浮点数
b = 3.14
# 查询b的类型 isinstance 函数
print(b, isinstance(b, float))

# ##
c = True
print(c, isinstance(c, bool))

#  -- 复数 complex
d = 2 + 3j
print(d, isinstance(d, complex))

# ----- 字符串
e = "你好"
print(e)
# 输出字符串 第一个字符
print(e[0])

# --- 列表
f = ["A", "B", 0, False, 3.14]
# 输出列表
print(f)

print(f[0])
# 取值 【0，3）
print(f[0:3])

g = ["汉字"]
# 列表相加
h = f + g
# 添加元素
h.append("新元素")
print(h)

# ------------Tuple 元组  ，元组创建后只读，不能添加
print("---------------------------------")
i = ("A", "B", True)
j = (3, 4)
k = i + j
print(k)

# ----------------Set （集合）  无需，去重

lSet = {"集合", "Set", 1, 1}
print(lSet)
lSet2 = {"3", False}

# 创建集合方式2
newSet = set("a")

print(newSet)
newSet = set([1,2,3])

print(newSet)

# 遍历集合
for e in newSet:
    print("遍历集合：",e)


# ----------   字典  todo 字典