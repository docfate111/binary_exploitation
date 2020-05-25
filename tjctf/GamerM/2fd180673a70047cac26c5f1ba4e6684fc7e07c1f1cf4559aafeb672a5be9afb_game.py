import random

def shuffle(s):
	for i in range(len(s)):
		j = random.randint(0, len(s) - 1)
		s[i], s[j] = s[j], s[i]
	return s


def combat(level):
	rps = ['rock', 'paper', 'scissors']
	crit = rps[random.randint(0, 2)]
	if crit == 'rock':
		print('A disciple stands in your way! Take your action!')
	elif crit == 'paper':
		print('A disciple blocks your way! Take your action!')
	elif crit == 'scissors':
		print('A disciple stalls your advance! Take your action!')

	print('\tChoose your weapon (\'rock\', \'paper\', \'scissors\')')
	if input('\tChoice: ').lower().strip() == crit:
		print('Sucess!')
		for name, c in level:
			print('%s dropped: %s' % (name, c))
		print('You rest and continue your journey.\n')
		return 1
	else:
		print('It wasn\'t very effective! The disciple counters with a seven page combo of punches and you die.')
		print('Try again when you reincarnate.')
		return 0


def game():
	flag = open('flag.txt').read().strip()
	names = shuffle([i.strip() for i in open('names.txt').readlines()])
	match = [(names[i], flag[i]) for i in range(len(flag))]

	levels = shuffle([shuffle(match[::5]), shuffle(match[1::5]), shuffle(match[2::5]), shuffle(match[3::5]), shuffle(match[4::5])])

	print('Welcome to the temple.\n' + \
		'\n' + \
		'You will face five tests.\n' + \
		'Each test involves combat against five disciples.\n' + \
		'Each disciple holds a key.\n' + \
		'Combine the keys to unlock the scroll\'s message.')

	for n, level in enumerate(levels):
		print()
		print('- = - Level %i - = - ' % (n + 1))
		if not combat(level):
			return

	print('You triumphed over all trials!')


if __name__ == "__main__": 
	game()