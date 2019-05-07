import random
import re

v = [{'october': 'the first movie we watched together'}, {'anabelle': 'doll movie that is scary as shit'}, {'the nun': 'we thought it would be scary but it anything but scary'}]
rand = random.choice(v)
movie = rand.keys()[0]

print 'it is a ' + str(movie.count(' ') + (1)) + ' word movie' 
print 'Hint : ' + rand.values()[0]

count = 15
c = 15
print 'you have ' + str(count) + ' turns' 
g = []
for i in range(count):
	v = raw_input('enter a letter : ')
	if len(v) == 1:
		if v in movie:
			inde = []
			for ind in re.finditer(v, movie):
				inde.append(ind.start())
			if c == 15 or g==[]:
				for i in xrange(len(movie)):
					if i in inde:
						g.append(v)
					elif movie[i]== ' ':
						g.append(' ')
					else:
						g.append('+')
			else:
				for i in xrange(len(movie)):
					if i in inde:
						g[i] = v
		else:
			print 'your letter is not present in the name'
		c -= 1
		print 'you have ' + str(c) + ' turns left'
	else:
		print 'please dont waste your turn doing follish things'
		print 'you have ' + str(c) + ' turns left' 
	guess = ''.join(g)
	print guess
	if movie==guess:
		break
if guess!=movie:
	print '15 tries what more do you want'
else:
	print 'congratulations you did it'
