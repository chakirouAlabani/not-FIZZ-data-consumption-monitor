import requests
from bs4 import BeautifulSoup

FIZZ_CA_FR_URL = 'https://fizz.ca/fr'
FIZZ_CA_EN_URL = 'https://fizz.ca/en'
FIZZ_CA_LOGIN_URL = 'https://auth.fizz.ca'

def main():
    print('non official fizz app')

    session = requests.Session()
    payload = get_credentials()
    # print(creds)

    #? 
    login_response = session.get(FIZZ_CA_LOGIN_URL, data=payload)
    print(login_response.status_code)
    # print(login_response.text)

def scrape():
    pass

def get_credentials(): 
    username = input('username: ')
    password = input('password: ')

    return {
        'username': username,
        'password': password
    }

if __name__ == '__main__':
    main()

