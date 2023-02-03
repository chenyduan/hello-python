
# 函数

def max(a, b):
    if a > b:
        return a
    else:
        return b


c = max(1, 2)
print(c)


# 不定长参数
def max2(a, *b):
    print(a)
    for v in b:
        print("b=", b)


print(max2(1, 2, 3))
