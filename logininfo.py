import auth
import requests

class userinfo:
    token_type=auth.login.token_type
    access_token=auth.login.access_token

    headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': token_type+' '+access_token}
    url = 'https://api.korbit.co.kr/v1/user/info'

    response = requests.get(url=url, headers=headers)
    dataJson = response.text
    status = response.status_code
