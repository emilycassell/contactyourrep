import json


import praw
import config
import time
import os
import requests
import urllib.parse

#main_api = 'https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?'
#address = 'California'
#level = 'NATIONAL_LOWER'
#url = main_api + urllib.parse.urlencode({'address': address})+urllib.parse.urlencode({'level': level})
#headers = { 'X-API-KEY': '2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c'}

#json_data = requests.get(url, headers=headers).json()

#data not 100% accruate ??


#for i in range(0,len(json_data['officials'])):
	#if (json_data['officials'][i]['office_details']['position'] == 'Representative') or (json_data['officials'][i]['office_details']['position'] == 'Senator') and json_data['officials'][i]['term_end']:
		#print(json_data['officials'][i]['office_details']['position']+ ' ' + json_data['officials'][i]['first_name'] + ' ' + json_data['officials'][i]['last_name'])
		#print(json_data['officials'][i]['office_location']["phone_1"])


def create_response(data):
	name=[]
	phone=[]
	for i in range(0,len(data['officials'])):
		if (data['officials'][i]['office_details']['position'] == 'Representative') or (data['officials'][i]['office_details']['position'] == 'Senator') and data['officials'][i]['term_end']:
			name.append(data['officials'][i]['office_details']['position']+ ' ' + data['officials'][i]['first_name'] + ' ' + data['officials'][i]['last_name'] + ': '+ ' ' + data['officials'][i]['office_location']["phone_1"] + "\n\n")
			
	return (name)


#contactdict = create_response(json_data)
#print(contactdict)

#print(' '.join(str(x) for x in contactdict))


def ngrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output



def combine_ngrams(thing):
	newlist=[]
	for i in thing:
		s = " ".join(i)
		newlist.append(s)
	return newlist




	


#for official in

