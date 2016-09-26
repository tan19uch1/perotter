#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from getch import _Getch
from requests_oauthlib import OAuth1Session
from getmyprof import Getmyprof
from gettl import Gettl
from tweet import Tweet
from detail import Detail
from config import Config
from destroy import Destroy
from favorite import Favorite
from retweet import Retweet

#名前
client	=	'labotter'
id_dic	=	{}

# OAuth認証で POST method で投稿
CK = 'j0sxMnIdbHwVuwgVho1Lgm7ig'							# Consumer Key
CS = 'JQLHDBZJo0g2MqaAvFtXmNklzD0P4CRMSLHwTpQ2RmubMIKr8h'	# Consumer Secret
AT = '3279767120-Czh7PTPIWAa3gPCH1VkFUvSB92i72nAUoUiZDhc'	# Access Token
AS = 'jFtYEGxc9TZor05JnH9wndsiKdgsqLOIHXeiBNDxORPNj'		# Accesss Token Secert
twitter = OAuth1Session(CK, CS, AT, AS)

#各機能のインスタンス作成
getprf	=	Getmyprof()
gettl	=	Gettl()
tweet	=	Tweet()
detail	=	Detail()
cfg		=	Config()
destroy	=	Destroy()
favorite=	Favorite()
retweet=	Retweet()

#プロフィール情報取得
account	=	getprf.getmyprf(twitter)

#とりあえず挨拶
print '> > > > HELLO WORLD!! %s (ver.114514) < < < <' % client

#入力待機
sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))

while True:
	getch = _Getch()
	x = getch()

	#各機能
	if x=='w' or x=='t':
		#ツイート機能
		error	=	tweet.post(twitter)
		#レスポンス確認
		if error is None:		#ツイート成功
			#sys.stdout.write('%s@%s:~/post_tweet/success\n' % (client,account["screen_name"]))
			pass
		elif error is 'cancel':	#ツイートキャンセル
			sys.stdout.write('%s@%s:~/post_tweet/cancel\n' % (client,account["screen_name"]))			
		else:						#ツイート失敗
			sys.stdout.write('%s@%s:~/post_tweet/failure_error_%s\n' % (client,account["screen_name"],error))
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))
	elif x=='r':
		#TL取得機能
		error	=	gettl.readtl(twitter,id_dic)
		id_dic	=	error["id_dic"]
		#レスポンス確認
		if isinstance(error,dict):	#取得成功
			sys.stdout.write('%s@%s:~/reflesh_TL/API_remains_%s/15\n' % (client,account["screen_name"],error['api']))
		else:					#取得失敗
			sys.stdout.write('%s@%s:~/reflesh_TL/failure_error_%s\n' % (client,account["screen_name"],error))
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))
	elif x=='s':
		#@scree_nameの詳細取得
		error	=	detail.detail(twitter)
		#レスポンス確認
		if error is None:			#取得成功
			#sys.stdout.write('%s@%s:~/search_detail/success\n' % (client,account["screen_name"]))
			pass
		elif error is 'cancel':		#取得キャンセル
			sys.stdout.write('%s@%s:~/search_detail/cancel\n' % (client,account["screen_name"]))			
		elif error is 'invalid':		#取得失敗（無効な名前）
			sys.stdout.write('%s@%s:~/search_detail/invalid_user\n' % (client,account["screen_name"]))			
		elif error is 'protected':	#取得失敗（鍵垢）
			sys.stdout.write('%s@%s:~/search_detail/protected_user\n' % (client,account["screen_name"]))			
		else:							#取得失敗
			sys.stdout.write('%s@%s:~/search_detail/failure_error_%s\n' % (client,account["screen_name"],error))
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))
	elif x=='e' or x=='q':
		print 'exit'
		sys.stdout.write('really? (y/n)')
		while True:
			getch = _Getch()
			ext = getch()
			if ext=='y':
				print ''
				exit()
			elif ext=='n':
				sys.stdout.write('\n%s@%s:~/' % (client,account["screen_name"]))
				break
	elif x=='d':
		destroy.delete(twitter,id_dic)
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))		
	elif x=='f':
		favorite.favorite(twitter,id_dic)
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))		
	elif x=='v':
		retweet.rt(twitter,id_dic)
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))		
	elif x=='c':
		cfg.config	=	cfg.setting(cfg.config)
		sys.stdout.write('%s@%s:~/' % (client,account["screen_name"]))

