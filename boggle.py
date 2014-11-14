'''
need:
-suffix tree of scrabble dictionary (actually i'm using unix words)
-parrelize code, make sure union operation on a set is parrelizable
-ocr package. needs to be able to observe spatial relationships as well, and return what it finds in a way so that i can put them into the boggle board.
'''

'''oh well it is fast enough.
 I don't feel the need to optimize it more'''


 '''
 if there is a square that has two letters write it as #ab
 '''
def makeBoard():
	stuff='wdgjee'+'ietdvf'+'nb#andef'+'srcdef'+'abclef'+'akcdef'
	i=0
	letters=[]
	while i<len(stuff):
		if stuff[i]=='#':
			letters.append(stuff[i+1:i+3])
			i=i+3
		else:
			letters.append(stuff[i])
			i=i+1
	return letters
letters=makeBoard()


#global variable:
foundSoFar= set()

f = open('/usr/share/dict/words', 'r')
words= f.read()
f.close()
words=words.split()
words= filter(lambda w: len(w)>2, words)
words=set(words)

import itertools as it
def recursiveSearch(ss,touched):
	#unfortunately this will wait until after i test with scrabble
	#if outsidetree(ss): return
	if validWord(ss): foundSoFar.add(makeString(ss))
	if len(ss) >6: return #don't want to take too long
	for square in untouchedNeighbors(ss,touched):
		recursiveSearch(ss+[square],touched+[square])

#right now it is a slow find. 
#but if i get the suffix tree implementation this will spead up a lot.
def validWord(ss):
	#return ss.nodeofsuffixtree
	return makeString(ss) in words

def untouchedNeighbors(ss,touched):
	untouched=[]
	for i,j in it.product((-1,0,1),(-1,0,1)):
		newSquare= (ss[-1][0]+i,ss[-1][1]+j)
		if -1 in newSquare or 6 in newSquare or newSquare in touched:
			continue
		else:
			untouched.append(newSquare)
	return untouched

def makeString(ss):
	string=""
	for square in ss:
		string += letters[square[0]+square[1]*6]
	return string

for start in it.product(range(6),range(6)):
	recursiveSearch([start],[start])
print foundSoFar

