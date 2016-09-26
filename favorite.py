#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import sys

class Favorite():
	"""Favorite tweet id via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def favorite(self,twitter,id_dic):
		#id_listがなければ終わる
		if not id_dic:
			sys.stdout.write('No_tweet_list press_r_key \n')
			return 0
		#削除IDを入力
		sys.stdout.write('favorite_tweet_No -> ')
		id_favorite		=	raw_input()
		try :
			params	=	{"id":id_dic[id_favorite]}
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

		#ふぁぼるorふぁぼ取り消し
		status	=	json.loads(stat.text)
		if	status["favorited"]	is False:
			#ふぁぼる
			url	=	"https://api.twitter.com/1.1/favorites/create.json"
			res	=	twitter.post(url,params=params)
		else:
			#ふぁぼ取り消す
			url	=	"https://api.twitter.com/1.1/favorites/destroy.json"
			res	=	twitter.post(url,params=params)

