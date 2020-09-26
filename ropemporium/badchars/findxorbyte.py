bad_chars = ['x', 'g', 'a', '.']
goal = 'flag.txt'
print('Find a number we can xor the string with to not have bad chars')
for i in range(30):
    encoded = ''
    for letter in goal:
        if(str(chr(i^ord(letter))) not in bad_chars):
            encoded += str(chr(i^ord(letter)))
        else:
            break
    if(len(encoded)==len(goal)):
        print(i, encoded)
print('Without: '+''.join(list(map(lambda x: str(ord(x)), bad_chars))))
print('Using 22: '+ ''.join(list(map(lambda x: hex(ord(x))[2:], [i for i in 'pzwq8bnb']))))