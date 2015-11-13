#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import Util.DateTimeUtil
import Util.StringUtil

if __name__=='__main__':
	#test datetime util function
	datestr='2015-11-11 12:12:12'
	fmt='%Y-%m-%d %H:%M:%S'
	d = Util.DateTimeUtil.str2datetime(datestr,True)
	s=Util.DateTimeUtil.datetime2str(d,'%W %w %j')	
	print s
	print Util.DateTimeUtil.weekofmonth(d)
	print Util.DateTimeUtil.timestamp()
	ts=Util.DateTimeUtil.gettimestamp(datestr,fmt)
	print "timestamp:" + str(ts)
	d1 = Util.DateTimeUtil.timestamp2datetime(ts)
	d2= Util.DateTimeUtil.getyesterday(d1)
	days=Util.DateTimeUtil.getdiffdays(d1,d2)
	print days


	Util.StringUtil.showFormat()
	print Util.StringUtil.trimSymbol('123,1:432""432')
