#!/usr/bin/python
# -*-coding:utf-8-*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

dict['Age'] = 10
print dict['Age']

#删除单一元素
del dict['Age']
print dict

#清空字典
#dict.clear()
print dict
#删除字典
#del dict

#字典键的特性
#1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

#字典内置函数或方法
#cmp
#len
#str
print "Equivalent String : %s" % str (dict)
#type
print type(dict)

#copy浅复制
dict1 = {'Name': 'Zara', 'Age': 7};

dict2 = dict1.copy()
print "New Dictinary : %s" %  str(dict2)


#直接赋值和 copy 的区别
#可以通过以下实例说明：
dict1 =  {'user':'runoob','num':[1,2,3]}

dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   #浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)

#dict.get(key, default=None)
#返回指定键的值，如果值不在字典中返回default值
dict1 = {'Name': 'Zara', 'Age': 7};
print dict1.get('Name')
print dict1.get('name', -1)

#dict.fromkeys(seq[, val]))
#创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict)

#   dict.has_key(key)
#如果键在字典dict里返回true，否则返回false

print dict.has_key('name')

#   dict.items()
#以列表返回可遍历的(键, 值) 元组数组
for k, v in dict.items():
    print k, v

#dict.keys()
#以列表返回一个字典所有的键
print dict.keys()

#dict.setdefault(key, default=None)
#和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

print "Value : %s" %  dict.setdefault('runoob', None)
print "Value : %s" %  dict.setdefault('Taobao', '淘宝')

#dict.update(dict2)
#把字典dict2的键/值对更新到dict里

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}

dict.update(dict2)
print "Value : %s" %  dict

#dict.values()
#以列表返回字典中的所有值

print dict.values()

#   pop(key[,default])
#删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。
#否则，返回default值。

print dict.pop('Name')
print dict.pop('name', 100)


#popitem()
#随机返回并删除字典中的一对键和值。
print dict.popitem()
