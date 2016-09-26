#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import relative_time
import textwrap

class Gettl():
	"""Get your TL from Twitter via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def  readtl(self,twitter,id_list):
		# タイムライン取得用のURL
		url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
		# とくにパラメータは無い
		params = {"count":8}
		# OAuthでTLを取得
		sys.stdout.write('reflesh_TL\n')
		req = twitter.get(url, params = params)

		if req.status_code == 200:
			# レスポンスはJSON形式なのでparseする
			timeline = json.loads(req.text)
			# 各ツイートの本文を表示&リストに格納
			id_dic	=	{}
			width	=	40
			num		=	1
			print	""
			print	"   %s %s    %s" % ("No".ljust(3),"user@time".ljust(21),"tweet".ljust(width))
			print	"   %s" % "".ljust(21+3+12+width,"-")
			for tweet in timeline:
				#taniguchi 32m24s:~/部分を作成
				timetxt	=	relative_time.get(tweet["created_at"])
				#もし取得ツイートが前回更新分にあれば
				if str(tweet["id"])	in str(id_list.values()) or not id_list:
					user	=	tweet["user"]["screen_name"] +"@"+timetxt
				else:
					user	=	"*" + tweet["user"]["screen_name"] +"@"+timetxt
				#折り返し付きで本文を表示
				text	=	textwrap.wrap(tweet["text"],width)
				print	"   >%s %s:~/%s" % (str(num).ljust(3),user.ljust(21),text[0])
				if len(text) > 1:
					for	txt in text[1:]:
						print	"        %s:~/%s" % ("".ljust(21),txt)
				#ナンバリング
				id_dic.update({str(num):tweet["id_str"]})
				num		+=	1
			print	"   %s" % "".ljust(21+3+12+width,"-")
			print ''
			return {"api":req.headers['x-rate-limit-remaining'],"id_dic":id_dic}
		else:
			# エラーの場合
			return req.status_code
