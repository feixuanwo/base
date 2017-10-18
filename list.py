#!/bin/bash/env python
# -*-coding:utf-8 -*-

#[]列表
#()元组
#{}字典
#set集合

#列表
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print len(l1)

#列表拼接
print l1 + l2
#重复
print l1 * 3
#判断元素是否在列表中
print 3 in l1
#迭代
for x in l2:
    print x

#取列表元素
print l1[1]
print l1[-1]
#截取
print l1[1:]
print l1[:-1]
print l1[:-2]

#列表方法
print cmp(l1, l2)
print max(l1)
print min(l1)

#元组转化列表
print list((1, 2, 3))

#修改原来的list，返回值为none
print l1.append(1)
print l1

#元素出现的次数
print l1.count(1)
#追加另一个序列
print l1.extend(l2)
print l1

#找出某个值第一次匹配的索引
print l1.index(1)

#插入对象 (修改原来的list，返回值为none)
print l1.insert(0, 10)
print l1

#移除元素
print l1.pop(6)
print l1.pop()

#按值删除第一个匹配的元素
l1.remove(1)
print l1
#反向
l1.reverse()
print l1
#排序
l1.sort()
print l1
