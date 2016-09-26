#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

class Getmyprof():
	"""Get My Profile from Twitter via Python-Oauth-Session"""
	def __init__(self):
			pass
			
	def  getmyprf(self,twitter):
		# タイムライン取得用のURL
		url = "https://api.twitter.com/1.1/account/verify_credentials.json"
		params = {}
		# OAuthでTLを取得
		req = twitter.get(url, params = params)

		if req.status_code == 200:
			# レスポンスはJSON形式なのでparseする
			prf = json.loads(req.text)
			# プロフィール情報を返す
			return prf
		else:
			# エラーの場合
			sys.stdout.write("profile_error_%d\n" % req.status_code)
