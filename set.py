#!/bin/usr/python
# -*-coding:utf-8 -*-

#python的set和其他语言类似, 是一个无序不重复元素集,
#基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交),
#difference(差)和sysmmetric difference(对称差集)等数学运算.

s = set()
s = {11,22,33,44}
#注意在创建空集合的时候只能使用s=set()，因为s={}创建的是空字典
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

#len(s)
#set 的长度

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

se = {11, 22, 33}
be = {22, 55}
temp1 = se.difference(be)        #找到se中存在，be中不存在的集合，返回新值
print(temp1)                     #{33, 11}
print(se)                        #{33, 11, 22}

temp2 = se.difference_update(be) #找到se中存在，be中不存在的集合，覆盖掉se
print(temp2)                     #None
print(se)                        #{33, 11},


#删除
#discard()、remove()、pop()
print "删除。。。。"
se = {11, 22, 33}
se.discard(11)
se.discard(44)     # 移除不存的元素不会报错
print "不会报错"
print(se)

se = {11, 22, 33}
se.remove(11)
#se.remove(44)      # 移除不存的元素会报错
print(se)

se = {11, 22, 33}  # 移除末尾元素并把移除的元素赋给新值
temp = se.pop()
print(temp)        # 33
print(se)          # {11, 22}
print type(se)

#取交集
se = {11, 22, 33}
be = {22, 55}

temp1 = se.intersection(be)             #取交集，赋给新值
print(temp1)                            # 22
print(se)                               # {11, 22, 33}

temp2 = se.intersection_update(be)      #取交集并更新自己
print(temp2)                            # None
print(se)                               # 22

#判断
se = {11, 22, 33}
be = {22}

print(se.isdisjoint(be))        #False，判断是否不存在交集（有交集False，无交集True）
print(se.issubset(be))          #False，判断se是否是be的子集合
print(se.issuperset(be))        #True，判断se是否是be的父集合

#合并
se = {11, 22, 33}
be = {22}

temp1 = se.symmetric_difference(be)  # 合并不同项，并赋新值
print(temp1)                         #{33, 11}
print(se)                            #{33, 11, 22}

temp2 = se.symmetric_difference_update(be)  # 合并不同项，并更新自己
print(temp2)                                #None
print(se)                                   #{33, 11}

#取并集
se = {11, 22, 33}
be = {22,44,55}

temp=se.union(be)   #取并集，并赋新值
print(se)       #{33, 11, 22}
print(temp)     #{33, 22, 55, 11, 44}

#更新
se = {11, 22, 33}
be = {22,44,55}

se.update(be)  # 把se和be合并，得出的值覆盖se
print "==================="
print(se)
se.update([66, 77])  # 可增加迭代项
print(se)

#集合的转换
se = set(range(4))
li = list(se)
tu = tuple(se)
st = str(se)
print(li,type(li))
print(tu,type(tu))
print(st,type(st))
