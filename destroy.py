#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import sys

class Destroy():
	"""Delete tweet id via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def delete(self,twitter,id_dic):
		#id_listがなければ終わる
		if not id_dic:
			sys.stdout.write('No_tweet_list press_r_key \n')
			return 0
		#削除IDを入力
		sys.stdout.write('delete_tweet_No -> ')
		id_delete		=	raw_input()
		try :
			# ツイート削除用のURL
			url = "https://api.twitter.com/1.1/statuses/destroy/%s.json" % id_dic[id_delete]
		except:
			sys.stdout.write('*Warning:No_ID_found\n')
			return 364
		#削除してみる
		params	=	{}
		req = twitter.post(url, params = params)

		#レスポンス確認
		if req.status_code == 200:
			return 0
		elif req.status_code == 403:
			print "ERROR:this_ID_is_not_yours"
			return 810
		else:
			print "ERROR:%d" % req.status_code
			return 810

