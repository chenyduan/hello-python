#!/usr/bin/python

# while
i = 1
while i < 5:
    print(i)
    i=i+1
    if i>3: break


# for循环

for v in "Abc":
    print(v)
else:
    print("else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。")

# for else

for v in "Abc":
    print(v)
    break
else:
    print("上面是break跳出，则此else 不执行")