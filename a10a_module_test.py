# from a10_module import a,module_fun
# 全部导入
import a10_module
from a10_module import *

print(a)
module_fun()


# dir()函数
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
#
# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：

print(dir(a10_module))