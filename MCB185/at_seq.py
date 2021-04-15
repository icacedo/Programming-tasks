import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

nt = 30
AT = 0.60

AT_int = int(AT*100)
GC_int = int(100-AT_int)
nuc = 'AT'*AT_int+'GC'*GC_int
seq = ''

for n in range(nt):
	seq += random.choice(nuc)
	A_frac = seq.count('A')
	T_frac = seq.count('T')
	AT_frac = (A_frac+T_frac)/len(seq)
print(len(seq),'%.2f'%AT_frac, seq)
