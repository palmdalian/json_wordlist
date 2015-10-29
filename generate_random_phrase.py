import json, random, os, sys

f = open(sys.argv[1], "rb")
wordlist = json.load(f)

def do_random():
	rand = random.choice(wordlist.keys())
	pos = wordlist[rand]
	return rand, pos

def get_random(pos):	
	rand, word_types =  do_random()
	while (pos not in word_types) and (" " in rand):
		rand, word_types = do_random()
	return rand

def get_alliteration(firstLetter, pos):
	rand, word_types =  do_random()
	while rand[0] != firstLetter[0]:
		rand, word_types = do_random()
		while (pos not in word_types) and (" " in rand):
			rand, word_types = do_random()
	return rand

#Alliteration
firstword = get_random("adverb")
secondword = get_alliteration(firstword,"adjective")
thirdword = get_alliteration(firstword,"noun")
print "%s %s %s" % (firstword,secondword,thirdword)

#Straight up random phrase
print "%s %s %s" % (get_random("adverb"),get_random("adjective"),get_random("noun"))
