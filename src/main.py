# ============================================
# !!! ЭКСПЕРИМЕНТАЛЬНЫЙ КОД !!!
# Этот скрипт написан для ознакомления с GitHub API.
# Не используйте в продакшне. Нет гарантий работы.
# ============================================

import requests

def auth(id, secret, redirect_url):
	url = "https://github.com/login/oauth/authorize"
	params = {
		"client_id": id,
		"redirect_url": redirect_url,
		"responce_type": "code",
		"scope": "user"
	}
	responce = requests.get(url, params=params)
	print(f"Follow the link {responce.url} to start authentication")
	code = input("Enter just code:")
	
	url = "https://github.com/login/oauth/access_token"
	params = {
		"client_id": id,
		"client_secret": secret,
		"redirect_url": redirect_url,
		"code": code
	}
	header = {"Accept": "application/json"}
	responce = requests.post(url, params=params, headers=header).json()
	
	try: token = responce["access_token"]
	except KeyError: token = None
	return token

def print_username(token):
	header = {"Authorization": f"Bearer {token}"}
	url = "https://api.github.com/user"
	responce = requests.get(url, headers=header).json()
	print(f"username: {responce['login']}")
	
client_id = "t"
client_secret = "t"
redirect_url = "https://example.com"

token = auth(client_id, client_secret, redirect_url)
print_username(token)
