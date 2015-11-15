import os
import json
import sys
import random

wordfile = open(sys.argv[1], "rb")
wordlist = json.load(wordfile)

def lookup_word(word):
	try:
		pos = wordlist[word]
		return pos
	except:
		pass

def do_random():
	rand = random.choice(collected.keys())
	pos = collected[rand]
	return rand, pos

def get_random(pos):	
	rand, word_types =  do_random()
	while (pos not in word_types):
		rand, word_types = do_random()
	return rand

f = open ("/tmp/twitch.tv/#twitch.log", "rb")
log = f.read()
lines = log.split("\n")

collected = {}
count = 0
#last line in log [-2]
for line in reversed(lines):
	if count < 1000:
		words = line.split()
		for word in words:
			if not "<" in word:
				pos = lookup_word(word)
				if pos:
					if "noun" in pos or "adjective" in pos or 'adverb' in pos:
						collected[word] = pos
						count +=1
	else:
		# print collected
		print get_random('adverb'), get_random('adjective'), get_random('noun')
		break

#TODO implement a flag to distinguish from normal chat
#Send words to arduino through serial port