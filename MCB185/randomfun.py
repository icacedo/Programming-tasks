# Write a program that does the following
# 1. generates N random sequences
# 2. each sequence has GC composition S and length L
# 3. calculate GC in a sliding window of size W
# 4. calculate entropy in a sliding window of size W
#
# Parameters N, S, L, and W are command line parameters
# Hint: write functions
#

import math
import random
import sys

'''
N = 1
S = 0.5
L = 15
W = 7
'''

def seq_gen(N, S, L):
	ranseq = []
	for i in range(N):
		for j in range(1, L+1):
			r = random.random()
			if r <= S: ranseq.append(random.choice('GC'))
			else: ranseq.append(random.choice('AT'))
		yield ''.join(ranseq)
		ranseq = []
		
def win_seq(seq, W):
	for i in range(len(seq)):
		if len(seq[i:i+W]) == W: 
			yield f'{seq[i:i+W]}'
		else: continue
			
def gc_comp(W_seq):
	GC = 0
	for n in W_seq:
		if n == 'G' or n == 'C': GC += 1
		else: continue	
	yield f'{GC/len(W_seq):.4f}'

# this code will fail if a window has a nucleotide frequency of 0
# added 0.0001 to get rid of 0s
def entropy(W_seq):
	A = 0
	C = 0
	G = 0
	T = 0
	for n in W_seq:
		if n == 'A': A += 1
		elif n == 'C': C += 1
		elif n == 'G': G += 1
		else: T += 1
	if A == 0: A += 0.0001
	if C == 0: C += 0.0001
	if G == 0: G += 0.0001
	if T == 0: T += 0.0001
	freq = []
	freq.append(A/len(W_seq))
	freq.append(C/len(W_seq))
	freq.append(G/len(W_seq))
	freq.append(T/len(W_seq))
	ent = 0
	for f in freq:
		ent += -f * math.log(f,2)
	yield f'{ent:.4f}'
	
N = sys.argv[1]
S = sys.argv[2]
L = sys.argv[3]
W = sys.argv[4]

print('N='+N,'S='+S,'L='+L,'W='+W)
yn = input('yes or no? ')

if yn == 'yes':
	N = int(N)
	S = float(S)
	L = int(L)
	W = int(W)

for seq in seq_gen(N, S, L):
	print(seq)
	print('gc')
	for W_seq in win_seq(seq, W):
		for gc in gc_comp(W_seq):
			print(gc)
	print('entropy')
	for W_seq in win_seq(seq, W):
		for e in entropy(W_seq):
			print(e)




