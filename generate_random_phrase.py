import json, random, os, sys

f = open(sys.argv[1], "rb")
wordlist = json.load(f)

def do_random():
	rand = random.choice(wordlist.keys())
	pos = wordlist[rand]
	return rand, pos

def get_random(pos):	
	rand, word_types =  do_random()
	while pos not in word_types or " " in rand:
		rand, word_types = do_random()
	return rand



phrase = get_random("adverb") + " " + get_random("adjective") + " " + get_random("noun")

print phrase