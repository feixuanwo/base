#!/bin/usr/env python
# -*-coding:utf-8 -*-

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print tup1[0]
print tup2[2:5]

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
#tup1[0] = 'hello'
tup3 = tup1 + tup2  #创建了一个新的元组
print tup3


#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

tup = ('physics', 'chemistry', 1997, 2000);

print tup;
del tup;
print "After deleting tup : "
#print tup;

#元组运算符同列表:len(个数),+(拼接),*(重复),in(元素是否存在),for(迭代)

#元组截取和索引同列表

#任意无符号的对象，以逗号隔开，默认为元组，如下实例：
print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;

#元组内置函数
#cmp
#len
#max
#tuple(seq) 将列表转化为元组

