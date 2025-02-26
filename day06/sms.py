import requests
import hashlib
import hmac
import uuid
from datetime import datetime
import os
from google.colab import userdata

API_KEY = userdata.get('API_KEY')
API_SECRET = userdata.get('API_SECRET')

URL = 'https://api.coolsms.co.kr/messages/v4/send-many/detail'

def generate_signature(api_secret, date_time, salt):
    # Signature 생성
    data = date_time + salt
    signature = hmac.new(api_secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

def send_sms(recipients, text):
    # 현재 시간과 Salt 생성
    date_time = datetime.utcnow().isoformat() + 'Z'
    salt = str(uuid.uuid4()).replace('-', '')[:12]  # 12바이트의 랜덤 문자열 생성

    # Signature 생성
    signature = generate_signature(API_SECRET, date_time, salt)

    # HTTP 헤더 설정
    headers = {
        'Authorization': f'HMAC-SHA256 apiKey={API_KEY}, date={date_time}, salt={salt}, signature={signature}',
        'Content-Type': 'application/json'
    }

    # 요청 데이터 설정
    data = {
        'messages': [
            {
                'to': recipient,  # 수신자 번호
                'from': '029302266',  # 발신자 번호 (유효한 번호로 변경)
                'text': text  # 메시지 내용
            } for recipient in recipients  # 수신자 목록을 반복하여 메시지 생성
        ]
    }

    # SMS 전송 요청
    response = requests.post(URL, headers=headers, json=data)

    # 응답 확인
    if response.status_code == 200:
        print("SMS 전송 성공:", response.json())
    else:
        print("SMS 전송 실패:", response.status_code, response.text)

# 사용 예시
recipients = ['01077287518', '01012345678']  # 수신자 번호 목록
send_sms(recipients, '안녕하세요! SMS 테스트입니다.')  # 수신자 번호를 실제 번호로 변경
