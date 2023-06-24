import time
from datetime import datetime
import requests
import sms

while(True):
    current_time = datetime.now()
    week_day = datetime.today().weekday()
    print(current_time.strftime('%H:%M:%S'))

    if week_day != 6:
        if current_time.strftime('%H:%M') == "18:00":
            url = "<http://api.coolsms.co.kr/messages/v4/send>"
            headers = sms.get_headers("API 공개키","API 비밀키")  
            data = '{"message":{"to":"수신자 전화번호","from":"발신자 전화번호","text":"조명이 켜졌습니다"}}'
            
            response = requests.post(url, headers=headers, data=data)
            print(response.status_code)
            print(response.text)

    time.sleep(60)