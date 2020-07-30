#这个是调试程序时留下来的一些东西，
#如果您要继续开发
#或许在这里调试是个不错的选择~
from requests import *
import json

mycookie='你的cookie'
user_id=3810250
user_json=get(url='https://api.codemao.cn/api/user/info/detail/'+str(user_id)).text
user_json=json.loads(user_json)
work_id=user_json['data']['userInfo']['work']['id']
headers = {'Content-Type': 'application/json','Cookie':mycookie}
print('给一个作品点了个赞~')