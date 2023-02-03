


# 异常


try:
    a = 1/1
except:
    print("发生异常执行")
    print(a)
else:
    print("不发生异常")
    print(a)
finally:
    print("总是执行")


# 抛出异常
# raise Exception("主动抛出异常")
print("***********")



# 自定义异常

class MyError(RuntimeError):
    def __int__(self,a):
        self.args = a

try:
    raise MyError("aa")
except MyError as e:
    print("自定义异常",e.args)