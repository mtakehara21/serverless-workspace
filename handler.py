import json
import urllib.request
import os
import xml.etree.ElementTree as ET

def post_slack(event, context):

    url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=f096f90662cd839e&lat=35.726&lng=139.66&range=5&order=4&count=1'
    
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        message = response.read()
        
    message = ET.fromstring(message)      
    message = "お家の近くのおすすめのお店 \n" + message[4][1].text + '\n' + message[4][4].text + '\n' + message[4][22][0].text

    send_data = {
        "username": "近所のオススメのお店",
        "icon_emoji": ":beer:",
        "text": message,
    }
    
    send_text = "payload=" + json.dumps(send_data)
    request = urllib.request.Request(
        os.environ['slack_api'],
        data=send_text.encode("utf-8"), 
        method="POST"
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")    