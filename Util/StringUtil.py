#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import string


class Person:
	def __init__(self,name,age):
		self.name,self.age=name,age
	def __str__(self):
		return 'name:{self.name},age:{self.age}'.format(self=self)

 
#string.format用法展示
def showFormat():
	print '{}##{}'.format(1,'lalala')
	print '{0},,{1}'.format(1,'lalala')
	print '{1}{0},,{1}'.format(1,'lalala')
	print '{arg1}..{arg2}'.format(arg1='123',arg2=23)
	print str(Person('John',23))

	arr=[1,2,'3']
	print 'arr:{0[0]},{0[2]}'.format(arr)

	print '{:>8}'.format('111')
	print '{:0>8}'.format('111')
	print '{:a<8}'.format('111')
	print '{:*^10}'.format('111')
	print '{:.2f}'.format(321.33345)
	print '{:,}'.format(1234567890)


#去掉所有符号,translate表示
def trimSymbol(s):
	#maketrans:生成一个映射表
	return s.translate(string.maketrans("",""),string.punctuation)
