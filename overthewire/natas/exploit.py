#!/usr/bin/python
import requests
username = 'natas'
password = ''
session = requests.Session()
obj = {'username' : 'natas16'}
url = 'http://' + username + '.natas.labs.overthewire.org/'
response = session.post(url, data = obj, auth = (username, password))
print(response.text)
