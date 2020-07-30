#这个呢，是一些有趣的东西，
#比如抢前排，顶贴，等等。
import requests
import json
import time, datetime

mycookie='你的cookie'

def getTime():
	# 获得当前时间
	now = datetime.datetime.now()
	# 转换为指定的格式
	otherStyleTime = now.strftime("%Y-%m-%d %H")
	return otherStyleTime

headers = {'Content-Type': 'application/json','Cookie':mycookie}

def qianpai():
	#1.获取首页帖子：
	all_forum_id=requests.get('https://api.codemao.cn/web/forums/posts/hots/all').text
	all_forum_id=json.loads(all_forum_id)
	    #TIP:因为前面几个帖子很有可能是官方或置顶的帖子，所以就忽略了
	forum_id=all_forum_id['items'][5]
	#2.判断帖子是否热乎，不热乎就算了
	#2.1先获取时间戳
	ctime=requests.get(url='https://api.codemao.cn/web/forums/posts/'+str(forum_id)+'/details').text
	ctime=json.loads(ctime)#这里边有时间戳
	ctime=ctime['created_at']
	# ctime=str(ctime)
	# print(ctime)
	#2.2转化时间戳=》日期和时间
	timeArray = time.localtime(ctime)
	otherStyleTime = time.strftime("%Y-%m-%d %H", timeArray)
	if(otherStyleTime!=getTime()):
		#那么就是这个帖子已经不新鲜了，舍去
		print('暂时没找到热乎的帖子呢……')
		return
	# print(otherStyleTime)
	#否则，就赶紧抢前排！
	url='https://api.codemao.cn/web/forums/posts/'+str(forum_id)+'/replies'
	reply_message="赶紧前排（doge<br>(啊哈小神学会抢前排了……"
	data = {"content":reply_message}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = requests.post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)
	print('大功告成！抢到了',forum_id,'的前排！')

def dd(forum_id):
	for i in range(2):
		url='https://api.codemao.cn/web/forums/posts/'+str(forum_id)+'/replies'
		reply_message='小神牌dd'
		data = {"content":reply_message}
		headers = {'Content-Type': 'application/json','Cookie':mycookie}
		response = requests.post(url=url, headers=headers, data=json.dumps(data))
		time.sleep(random.randint(1,10))
	print('dd')

def go(forum_id,user):#召唤小神去其他帖子！
	url='https://api.codemao.cn/web/forums/posts/'+str(forum_id)+'/replies'
	reply_message="哇哇哇！我被"+user+'召唤到了这里凑热闹~<br>可以和我聊天哦~<br>\
	你可以去 https://blog.amazingcode.top/xiaoshen/ 看看我的使用指南哦~<br>TIP:先把我置顶好不好，不然我走了~'
	data = {"content":reply_message}
	headers = {'Content-Type': 'application/json','Cookie':mycookie}
	response = requests.post(url=url, headers=headers, data=json.dumps(data))
	print(response.text)