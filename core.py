from lib import talk
from requests import *
import json,time,random
import os,_thread
import forumConsole
from multiprocessing import Process
from repliesConsole import *

mycookie='你的cookie'

def get_message():
	data={'Cookie':mycookie}
	msg = get(url='https://api.codemao.cn/web/message-record?query_type=COMMENT_REPLY&limit=10&offset=0',headers=data).text
	return msg

def like_work(user_id):
	user_json=get(url='https://api.codemao.cn/api/user/info/detail/'+str(user_id)).text
	user_json=json.loads(user_json)
	work_id=user_json['data']['userInfo']['work']['id']
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	print('给一个作品点了个赞~')

def rpl(msg_json,sessionid=12345):
	reply='.'
	if(msg_json['items'][0]['type']=='POST_COMMENT'):
		msg_json=json.loads(msg_json['items'][0]['content'])
		reply=msg_json['message']['comment']
		reply=reply[3:-4]
		comment_id=msg_json['message']['comment_id']
		print('收到回复',reply)
		reply_main_msg(comment_id,0,talk(reply))
	elif(msg_json['items'][0]['type']=='POST_REPLY_REPLY'):
		print(msg_json['items'][0])
		msg_json=json.loads(msg_json['items'][0]['content'])
		reply=msg_json['message']['reply']
		pr=msg_json['message']['reply_id']
		forum_id=msg_json['message']['business_id']
		forum_json=get('https://api.codemao.cn/web/forums/posts/'+str(forum_id)+'/replies?page=1&limit=10&sort=-created_at')
		forum_json=json.loads(forum_json.text)
		comment_id=forum_json['items'][0]['id']
		print('收到回复',reply)
		reply_reply(comment_id,pr,talk(reply,sessionid))
	elif(msg_json['items'][0]['type']=='POST_REPLY'):#BUG，只能回复第一条留言QWQ
		msg_json=json.loads(msg_json['items'][0]['content'])
		reply=msg_json['message']['reply']
		comment_id=msg_json['message']['replied_id']
		pr=msg_json['message']['reply_id']
		print('收到回复',reply)
		print(comment_id,pr)
		reply_pr(comment_id,pr,talk(reply,sessionid))
	#注意！关于自动回复工作室的！
	#由于无法实现，所以只能在自己的工作室里用，而且只能有一条！
	elif(msg_json['items'][0]['type']=='WORK_SHOP_REPLY'):#工作室的直接回复
		pr=msg_json['items'][0]['reference_id']
		msg_json=json.loads(msg_json['items'][0]['content'])
		url_id=msg_json['message']['replied_id']
		ai_reply=talk(msg_json['message']['reply'])
		print('收到来自工作室的回复！信息：',msg_json['message']['reply'],'  回复：',ai_reply)
		reply_studio_mainmsg(url_id,pr,ai_reply)
	elif(msg_json['items'][0]['type']=='WORK_SHOP_REPLY_REPLY'):#回复了我工作室回复的回复（有点绕
		pr=msg_json['items'][0]['reference_id']
		msg_json=json.loads(msg_json['items'][0]['content'])
		url_id=1499355#这里是因为无法获取，所以只能这样了，于是就有了“一条评论”的限制。
		ai_reply=talk(msg_json['message']['reply'])
		print('收到工作室回复的回复！信息：',msg_json['message']['reply'],'  回复：',ai_reply)
		reply_studio_reply(url_id,pr,ai_reply)

	
	#下面是一些特定功能
	if(reply[0:4]=='goto'):
		forum_id=int(reply[4:])
		user=msg_json['sender']['nickname']
		forumConsole.go(forum_id,user)
	elif(reply[0:4]=='like'):
		user_id=msg_json['sender']['id']
		like_work(user_id)
	elif(reply[0:2]=='dd'):
		forumConsole.dd(int(reply[2:]))


def main():
	last_reply = "0"
	timecnt=0
	while(True):
		# try:
		timecnt+=1
		#1.随时回复
		msg_json=get_message()
		msg_json=json.loads(msg_json)
		if(last_reply==msg_json['items'][0]['id']):
			continue
		last_reply=msg_json['items'][0]['id']
		rpl(msg_json,eval(msg_json['items'][0]['content'])['sender']['id'])

if __name__ == '__main__':
	time.sleep(2)
	os.system('cls')
	main()
	print('info:自动回复已启动')