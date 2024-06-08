import requests
import base64
from datetime import datetime
from flask import request, jsonify

CONSUMER_KEY = 'TUa4Nas3Av7hszqYoBhZJcVqB5egDGGt'
CONSUMER_SECRET = '98Yd5Sw60CIPzSAo'
SHORTCODE = "174379"
LIPA_NA_MPESA_ONLINE_ENDPOINT = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
SECURITY_CREDENTIAL = 'pmAOnzSMwm7yJy3Bycf/bzIlhvkIYgdm/52MrNnibIiwdxU7UwlY1VZ78YGIPIvemP94QjG47c9gFIs7qySHOQmHKPaXBuuS4W8edennspZYrSo9M+QSgeG6gwLfnjzeZtbP8PK2/xqZ11LlPyE1XDwaS1EZyLhNqlBccyXzhf0ppvlAjdOX9koVK79CQWt5k8subFusE5QBvYLJc4iH/aSrhcxugyOVEGPfffOuEC+g3kqO8EX87URjCKXcuYwXHrpwC5fYO3L1jLfMR+DyhiqlI+FAymfS28A9jhpxSLqMMq/oZm8mhA0HGX1NiKjrzp7aMJen0ZpezCK3oMOyJw=='
LIPA_NA_MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
INITIATOR_NAME = 'testapi'
INITIATOR_PASSWORD = 'Safaricom999!*!'
PARTY_A = '600977'
PARTY_B = '600000'
PHONE_NUMBER='254719668125'
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
# print(timestamp)

def generate_token():
    token_endpoint = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    credentials = base64.b64encode((CONSUMER_KEY + ':' + CONSUMER_SECRET).encode()).decode('utf-8')
    headers = {
        'Authorization': 'Basic ' + credentials
    }

    try:
        response = requests.get(token_endpoint, headers=headers)
        print(response.json())
        print(response.raise_for_status())
        return response.json().get('access_token')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to generate token: {e}") from e


def sendStkPush():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    token = generate_token()
    shortCode = '174379'
    phone_number = '254719668125'
    amount = '1'
    stk_password = base64.b64encode((shortCode + LIPA_NA_MPESA_PASSKEY + timestamp).encode('utf-8')).decode('utf-8')

    headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
    
    requestBody = {
            "BusinessShortCode": shortCode,
            "Password": stk_password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline", #till "CustomerBuyGoodsOnline"
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": shortCode,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://yourwebsite.co.ke/callbackurl",
            "AccountReference": "account",
            "TransactionDesc": "test"
        }
    
    try:
        response = requests.post(LIPA_NA_MPESA_ONLINE_ENDPOINT, json=requestBody, headers=headers)
        print(response.json())
        return response.json()
    except Exception as e:
        print('Error:', str(e))

def handle_callback():
    callback_data = request.json
sendStkPush()
# print(generate_token())