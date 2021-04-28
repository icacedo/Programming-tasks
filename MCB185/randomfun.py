# Write a program that does the following
# 1. generates N random sequences
# 2. each sequence has GC composition S and length L
# 3. calculate GC in a sliding window of size W
# 4. calculate entropy in a sliding window of size W
#
# Parameters N, S, L, and W are command line parameters
# Hint: write functions

import math
import random
import sys

N = 1
S = 0.5
L = 15
W = 7

def seq_gen(N, S, L):
	ranseq = []
	for i in range(N):
		for j in range(1, L+1):
			r = random.random()
			if r <= S: ranseq.append(random.choice('GC'))
			else: ranseq.append(random.choice('AT'))
		yield ''.join(ranseq)
		ranseq = []
		
def gc_comp(seq, W):
	for i in range(len(seq)):
		if len(seq[i:i+W]) == W: 
			W_seq = seq[i:i+W]
			GC = 0
			total = 0
			for n in W_seq:
				if n == 'G' or n == 'C': 
					GC += 1
					total += 1
				else: continue	
			yield f'{GC/len(W_seq):.4f}', W_seq
		else: continue

def entropy
	
	
'''
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
'''	
for seq in seq_gen(N, S, L):
	print(seq)
	for gc, W_seq in gc_comp(seq, W):
		print(gc)
		print(W_seq)
	



