#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import sys
import relative_time
import textwrap

class Detail():
	"""See the detail of user"""
	def __init__(self):
			pass
			
	def  detail(self,twitter):
		#表示幅
		width	=	40
		# タイムライン取得用のURL
		url_twt	=	"https://api.twitter.com/1.1/statuses/user_timeline.json"
		url_prf	=	"https://api.twitter.com/1.1/users/show.json"
		# screen_name取得
		sys.stdout.write("search_detail_screen_name -> ")
		screen_name	=	raw_input()
		#screen_nameが空白かどうか判定
		identify	=	re.compile('\s',re.IGNORECASE)		#非空白文字正規表現
		name_exclude_space		=	identify.sub('',screen_name)		#ツイートの空白を削除してみる
		params = {"screen_name":name_exclude_space,"count":5}
		if	name_exclude_space:
			#非空白文字があれば検索
			twt = twitter.get(url_twt, params = params)
			prf = twitter.get(url_prf, params = params)
		else:
			#空白文字のみだったら
			return 'cancel'

		# レスポンスを確認
		if twt.status_code == 200:
			# レスポンスはJSON形式なのでparseする
			timeline	=	json.loads(twt.text)
			profile	=	json.loads(prf.text)
			# 各@IDの本文を表示
			print '   >%s(@%s)' % (profile["name"],profile["screen_name"])
			print '   >Follows:%d, Followers:%d, Favorites:%d' % (profile["friends_count"],profile["followers_count"],profile["favourites_count"])
			if	profile["description"]:
				print '   >Description:%s' % profile["description"]
			if	profile["location"]:
				print '   >Location:%s'%profile["location"]
			for tweet in timeline:
				time_txt=	relative_time.get(tweet["created_at"])
				prof	=	'%s@%s' % (profile["screen_name"],time_txt)
				text	=	textwrap.wrap(tweet["text"],width)
				print	"   >>%s:~/%s" % (prof.ljust(21),text[0])
				if len(text) > 1:
					for	txt in text[1:]:
						print	"     %s:~/%s" % ("".ljust(21),txt)
			return None
		elif twt.status_code == 404:
			return 'invalid'
		elif twt.status_code == 401:
			return 'protected'
		else:
			return req.status_code

