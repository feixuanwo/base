#!/bin/usr/python
# -*-coding:utf-8 -*-

#python的set和其他语言类似, 是一个无序不重复元素集,
#基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交),
#difference(差)和sysmmetric difference(对称差集)等数学运算.
s1 = set('boy')
print s1

#集合add方法：是把要传入的元素做为一个整个添加到集合中
s1.add('python')
print s1

#集合update方法：是把要传入的元素拆分，做为个体传入到集合中
s1 = set('boy')
print s1
s1.update('python')
print s1

#集合删除操作方法：remove
s1 = set(['python', 'b', 'o', 'y'])
print s1
s1.remove('python')
print s1

#a = t | s          # t 和 s的并集
#b = t & s          # t 和 s的交集
#c = t – s          # 求差集（项在t中，但不在s中）
#d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）

len(s)
set 的长度

#x in s
#测试 x 是否是 s 的成员
#
#x not in s
#测试 x 是否不是 s 的成员
#
#s.issubset(t)
#s <= t
#测试是否s中的每一个元素都在t中
#
#s.issuperset(t)
#s >= t
#测试是否t中的每一个元素都在s中
#
#s.union(t)
#s | t
#返回一个新的set包含s和t中的每一个元素
#
#s.intersection(t)
#s & t
#返回一个新的 set 包含 s 和 t 中的公共元素
#
#s.difference(t)
#s - t
#返回一个新的 set 包含 s 中有但是 t 中没有的元素
#
#s.symmetric_difference(t)
#s ^ t
#返回一个新的 set 包含 s 和 t 中不重复的元素
#
#s.copy()
#返回 set “s”的一个浅复制
