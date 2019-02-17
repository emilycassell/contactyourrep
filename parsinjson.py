import json


import praw
import config
import time
import os
import requests
import urllib.parse

main_api = 'https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?'
address = 'California'
level = 'NATIONAL_LOWER'
url = main_api + urllib.parse.urlencode({'address': address})+urllib.parse.urlencode({'level': level})
headers = { 'X-API-KEY': '2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c'}

json_data = requests.get(url, headers=headers).json()
#parsed_json_data = json.loads(json_data)

#print(json_data['officials'][0]['office_location']["phone_1"])
#print(json_data['officials'][0]['first_name'] + ' ' + json_data['officials'][0]['last_name'])
#print(json_data['officials'][0]['first_name'] + ' ' + json_data['officials'][0]['last_name'] +': '+ json_data['officials'][0]['office_location']["phone_1"])
#print(json_data['officials'][1]['first_name'] + ' ' + json_data['officials'][1]['last_name'] +': '+ json_data['officials'][1]['office_location']["phone_1"])

#data not 100% accruate ??


for i in range(0,len(json_data['officials'])):
	if (json_data['officials'][i]['office_details']['position'] == 'Representative') or (json_data['officials'][i]['office_details']['position'] == 'Senator') and json_data['officials'][i]['term_end']>"2019-01-01 00:00:00" :
		print(json_data['officials'][i]['office_details']['position']+ ' ' + json_data['officials'][i]['first_name'] + ' ' + json_data['officials'][i]['last_name'])
		print(json_data['officials'][i]['office_location']["phone_1"])


def create_response(data):
	name=[]
	phone=[]
	for i in range(0,len(json_data['officials'])):
		if (data['officials'][i]['office_details']['position'] == 'Representative') or (json_data['officials'][i]['office_details']['position'] == 'Senator') and json_data['officials'][i]['term_end']>"2019-01-01 00:00:00" :
			name.append(json_data['officials'][i]['office_details']['position']+ ' ' + json_data['officials'][i]['first_name'] + ' ' + json_data['officials'][i]['last_name'] + ': '+ ' ' + json_data['officials'][i]['office_location']["phone_1"] + "\n\n")
			
			
	#print(name)
	return (name)


contactdict = create_response(json_data)
#print(contactdict)

print(' '.join(str(x) for x in contactdict))
#replytext = ("call your senator:" + " ".join(str(x) for x in contactdict))
#print(replytext)

#newfile = create_response(json_data)
#newfilename = json.dumps(newfile["name_position"][2])
#newfilenumber = json.dumps(newfile["phonenumber"][2])

#for i in contact

#print("call your representatives today:" + newfilename[] + ' ' + newfilenumber)
#print("call your senator")



	


#for official in

