#!/usr/bin/python
#coding=utf-8
import sys
#大括号的功能演示

#大括号 ：代表dict字典数据类型，字典是由键对值组组成。冒号':'分开键和值，逗号','隔开组。
#字典的组成：字典是由大括号{  }来包含其数据的，大括号内包含键和其对应的值，一对键和值成为一个项。键和值用冒号:隔开，项和项之间用逗号,号隔开。空字典就是不包含任何项的大括号，像{ }这样就是一个空字典。

reload(sys)
sys.setdefaultencoding('utf8')

##创建字典
a = {"name":"arno","sex":"男","age":33}
print a
#修改字典的值
a["age"] = 18
print a

#坊问字典中的项
print a["sex"]


#删除字典项
del a["name"]
print a

#清除字典内容
a.clear()
print a
