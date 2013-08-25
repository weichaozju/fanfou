#spider1.py
#coding=utf-8
import requests
import json
import time
import logging  
logging.basicConfig(filename='D:/log.txt',level=logging.DEBUG)
logging.info('Starting……')

#通过API抓取数据，HTTP Basic验证
url = 'http://api.fanfou.com/statuses/public_timeline.json'
username = ''
password = ''
r=requests.get(url,auth=(username, password))

d=r.json() 

since_id=d[0]['id']
rawid_max=d[0]['rawid']
j=0
outputfile=open('D:/csv.txt','w',encoding='UTF-8')

while True:
	j=j+1
	print (j)
	logging.info(j)
	payload={'since_id':since_id}
	while True:
		try:
			r=requests.get(url,params=payload,auth=(username, password))
		except:
			print ('网络错误，2秒后重试')
			time.sleep(2)
			continue
		break
	e=r.json()
	for i in range(0,len(e)):
		rawid_int=e[i]['rawid']
		
		rawid=str(e[i]['rawid'])
		text=str(e[i]['text'])
		created_at=str(e[i]['created_at'])
		in_reply_to_screen_name=str(e[i]['in_reply_to_screen_name'])
		in_reply_to_user_id=str(e[i]['in_reply_to_user_id'])
		
		u=e[i]['user']
		
		name=str(u['name'])
		statuses_count=str(u['statuses_count'])
		followers_count=str(u['followers_count'])
		favourites_count=str(u['favourites_count'])
		#description=str(u['description'])
		u_created_at=str(u['created_at'])
		u_id=str(u['id'])
		
		if rawid_int>rawid_max:
			outputfile.write(rawid+',')
			outputfile.write(text+',')
			outputfile.write(created_at+',')
			outputfile.write(in_reply_to_screen_name+',')
			outputfile.write(in_reply_to_user_id+',')
			outputfile.write(name+',')
			outputfile.write(statuses_count+',')
			outputfile.write(followers_count+',')
			outputfile.write(favourites_count+',')
			#outputfile.write(description+',')
			outputfile.write(u_created_at+',')
			outputfile.write(u_id+',')
			outputfile.write('\n')
	since_id=e[0]['id']
	rawid_max=e[0]['rawid']
	if j==9000:
		break
	time.sleep(10)
outputfile.close()


