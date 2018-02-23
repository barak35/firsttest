import json
import requests

secret = 'TwEC1ulGn8AxbFjfKi4JXxosgjJta9NSKdzyrYSsmH7U8G74EMXHIwTzvgTJ2'
apikey = 'rDdI8ZFFLzV3iD9VSeFwMHqdJYYGEIEXgW3FKochVlXRAe9TAgGh3bkIOTzNO'
id = 'barak35@gmail.com'
pw = 'chldudgns1!'

class login:
    headers={'User-Agent': 'Mozilla/5.0','Authorization':'Bearer 12094519051ewhdsofhsoy2ghewekfhse'}
    url = 'https://api.korbit.co.kr/v1/oauth2/access_token'
    params = {'client_id':apikey ,'client_secret':secret,'username':id,'password':pw,'grant_type':'password' }
    response=requests.post(url=url,data=params)
    dataJson=response.json()
    token_type=dataJson['token_type']
    access_token=dataJson['access_token']
    status=response.status_code
