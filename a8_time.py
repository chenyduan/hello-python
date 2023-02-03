import time

# 时间戳
print(time.time())
# 本地时间
print(time.localtime(time.time()))

# 格式化时间  Fri Feb  3 10:58:38 2023
print(time.asctime(time.localtime(time.time())))
# 2023-02-03 11:01:17 
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
