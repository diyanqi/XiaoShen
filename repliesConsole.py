from requests import *
import json

mycookie='你的cookie'

def reply_main_msg(comment_id,pr,reply_message):
	reply_message+='(另：你应该回复我的那条置顶留言来聊天，不然我不理你了😕~'
	url='https://api.codemao.cn/web/forums/replies/'+str(comment_id)+'/comments'
	data = {"parent_id":pr,"content":reply_message}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)

def reply_reply(replied_id,pr,reply_message):    #只允许回复以自己为父亲节点评论的评论
	url='https://api.codemao.cn/web/forums/replies/'+str(replied_id)+'/comments'
	data = {"parent_id":pr,"content":reply_message}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)

def reply_pr(replied_id,pr,reply_message):
	url='https://api.codemao.cn/web/forums/replies/'+str(replied_id)+'/comments'
	data = {"parent_id":pr,"content":reply_message}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)

def reply_studio_mainmsg(url_id,pr,reply_message):
	url='https://api.codemao.cn/web/discussions/585/comments/'+str(url_id)+'/reply'
	data={"parent_id":pr,"content":reply_message,"source":"WORK_SHOP"}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)

def reply_studio_reply(url_id,pr,reply_message):
	url='https://api.codemao.cn/web/discussions/585/comments/'+str(url_id)+'/reply'
	data={"parent_id":pr,"content":reply_message,"source":"WORK_SHOP"}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)