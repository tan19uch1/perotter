#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import sys

class Tweet():
	"""Tweet to Twitter via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def  post(self,twitter):
		# タイムライン取得用のURL
		url = "https://api.twitter.com/1.1/statuses/update.json"
		#ツイート内容
		sys.stdout.write('post_tweet -> ')
		twt		=	raw_input()
		params	=	{"status":twt}
		#ツイートが空白かどうか判定
		identify	=	re.compile('\s',re.IGNORECASE)		#非空白文字正規表現
		twt_exclude_space		=	identify.sub('',twt)		#ツイートの空白を削除してみる
		if	twt_exclude_space:
			#非空白文字があればPOST
			req = twitter.post(url, params = params)
		else:
			#空白文字のみだったら
			return 'cancel'

		# レスポンスを確認
		if req.status_code == 200:
			return None
		else:
			return req.status_code
