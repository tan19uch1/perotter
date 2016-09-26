#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import sys

class Retweet():
	"""Retweet tweet id via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def rt(self,twitter,id_dic):
		#id_listがなければ終わる
		if not id_dic:
			sys.stdout.write('No_tweet_list press_r_key \n')
			return 0
		#削除IDを入力
		sys.stdout.write('retweet_tweet_No -> ')
		id_retweet		=	raw_input()
		try :
			params	=	{"include_my_retweet":1,"id":id_dic[id_retweet]}
		except:
			sys.stdout.write('*Warning:No_ID_found\n')
			return 364

		#該当ツイートオブジェクトを取得
		url		=	"https://api.twitter.com/1.1/statuses/show.json"
		stat	=	twitter.get(url,params=params)
		#レスポンス確認
		if stat.status_code == 200:
			pass
		elif stat.status_code == 404:
			print "ERROR:this_ID_is_not_yours"
			return 810
		else:
			print "ERROR:%d" % stat.status_code
			return 810

		#RTorRT取り消し
		print stat.text
		status	=	json.loads(stat.text)
		if	status["retweeted"]	is False:
			#RT
			url	=	"https://api.twitter.com/1.1/statuses/retweet/%s.json" % id_dic[id_retweet]
			params	=	{"id":id_dic[id_retweet]}
			res	=	twitter.post(url,params=params)
			if	res.status_code	==	403: print "*ERROR:this user is protected"
		else:
			#RT取り消す
			url	=	"https://api.twitter.com/1.1/statuses/destroy/%s.json" % status["current_user_retweet"]["id_str"]
			print url
			params	=	{"id":status["current_user_retweet"]["id_str"]}
			res	=	twitter.post(url,params=params)
			if not	res.status_code	==	200: print "*ERROR:cannot remove RT error code %d" % res.status_code

