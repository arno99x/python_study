#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

myD = {1:'a',2:'b',3:'c',4:'d'}
for key, value in dict.items(myD):
    print key,value
    #暂停1秒
    time.sleep(1)


#知识点1： dict类型迭代
#知识点2： 线程睡眠
