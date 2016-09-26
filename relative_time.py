#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt

def get(str_t):
	#相対時刻（秒）を取り出す
	t_post		=	dt.datetime.strptime(str_t,'%a %b %d %H:%M:%S +0000 %Y')
	t_now	=	dt.datetime.utcnow()
	delta	=	t_now	-	t_post
	total_seconds	=	delta.total_seconds()
	#相対時刻をテキストで返す
	year	=	0
	day		=	0
	hour	=	0
	minute	=	0
	while	total_seconds	>=	60*60*24*365:	#年判定
		year	+=	1
		total_seconds	-=	60*60*24*365
	while	total_seconds	>=	60*60*24:	#日判定
		day	+=	1
		total_seconds	-=	60*60*24
	while	total_seconds	>=	60*60:	#時判定
		hour	+=	1
		total_seconds	-=	60*60
	while	total_seconds	>=	60:	#分判定
		minute	+=	1
		total_seconds	-=	60
	second	=	total_seconds
	if	year	>=	1:
		text	=	'%dy%dd' % (year,day)
		return text
	elif	day	>=	1:
		text	=	'%dd%dh' % (day,hour)
		return text
	elif	hour	>=	1:
		text	=	'%dh%dm' % (hour,minute)
		return text
	elif	minute	>=	1:
		text	=	'%dm%ds' % (minute,second)
		return text
	elif	second	>=	1:
		text	=	'%dsec' % second
		return text
