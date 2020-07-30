# -*- coding: utf-8 -*-
from urllib import request, parse
import json
import sys
import time
import datetime,os,aiml

def translate(word,from_lang='AUTO',to_lang='AUTO'):
	req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
	# 创建要提交的数据
	tss1=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
	timeStamp = str(time.mktime(timeArray))
	Form_Date = {}
	Form_Date['i'] = word  
	Form_Date['doctype'] = 'json'
	Form_Date['form'] = from_lang
	Form_Date['to'] = to_lang
	Form_Date['smartresult'] = 'dict'
	Form_Date['client'] = 'fanyideskweb'
	Form_Date['salt'] = timeStamp
	Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
	Form_Date['version'] = '2.1'
	Form_Date['keyform'] = 'fanyi.web'
	Form_Date['action'] = 'FY_BY_REALTIME'
	Form_Date['typoResult'] = 'false'

	data = parse.urlencode(Form_Date).encode('utf-8') #数据转换
	response = request.urlopen(req_url, data) #提交数据并解析
	html = response.read().decode('utf-8')  #服务器返回结果读取
	# 可以看出html是一个json格式
	translate_results = json.loads(html)  #以json格式载入
	translate_results = translate_results['translateResult'][0][0]['tgt']
	return translate_results
  
  
  # 切换到语料库所在工作目录
os.chdir('data')
alice=aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
	alice.bootstrap(brainFile = "bot_brain.brn")
else:
	alice.bootstrap(learnFiles = ["startup.xml"], commands = ["LOAD ALICE"])
	alice.saveBrain("bot_brain.brn")
os.chdir('..')
  
def talk(msg:str,sessionid=12345):
	message = translate(msg,to_lang='en')
	response = alice.respond(message,sessionid)
	if response=='':
		response='...' # 机器人应答
	return translate(response).replace('无名的','小神').replace('无名','小神')

# print(talk('life is short?'))
