#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy

a = [1,2,3]

#切片方式
# b = a[:]
# print b

##使用copy   好像python 2.x用不了。。。################
# b = a.copy()
# print b

##使用循环复制法
# b = []
# for i in a:
#     b.append(i)
# print b

##使用copy功能
#如果数组中还有数组，上面的三种方式是不可以的，需使用copy功能做
b = copy.copy(a)
print b

##注解########################
# 1. 使用切片
# 　　切片在python中的作用是非常大的，可用作于所有的可迭代对象。使用:
# list2 = list1[:]
# 2.使用copy
# 　　copy在python中可以实现拷贝一个对象。使用:
# list2 = list1.copy()
# 3. 使用循环复制法
# 　可以循环遍历list1，将值插入到list2中.使用:
# list2 = [for i in list1]
