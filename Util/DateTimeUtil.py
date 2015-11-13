#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding

import datetime
import time

#日期格式化
def str2datetime(str,debug=False):
	d=datetime.datetime.strptime(str,'%Y-%d-%m %H:%M:%S')
	if debug:
		print '年:%d 月: %d 日: %d, 小时:%d 分:%d 秒: %d' %(d.year,d.month,d.day,d.hour,d.minute,d.second)
		isocalendar = d.isocalendar()
		print '星期%d 今年的第%d周, 今年的第%d天' % (d.weekday(),isocalendar[1],d.timetuple().tm_yday)
	return d;

def datetime2str(date,fmt='%Y-%m-%d'):
	#%Y %m %d %H %M %s
	#%W:一年中的第几周
	#%w:周几
	#%j:一年中的第几天
	str=date.strftime(fmt)
	return str

#当前天是当月中的第几周
def weekofmonth(date):
	end=int(date.strftime('%W'))
	start=int(datetime.datetime(date.year,date.month,1).strftime('%W'))
	return end-start+1

def timestamp():
	return int(time.time())	

def gettimestamp(datestr,fmt):
	timeArray = time.strptime(datestr, fmt)
	return int(time.mktime(timeArray))

#获取当前时间
def current():
	return datetime.datetime.now()

def timestamp2datetime(ts):
	return datetime.datetime.fromtimestamp(ts)

#use timedelta
def getyesterday(date):
	td=datetime.timedelta(days=-1)
	return date-td

def getdiffdays(d1,d2):
	diff=d1-d2
	#diff.days diff.seconds diff.microseconds
	return diff.days
