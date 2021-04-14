# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

'''
comp = {'A':'T','C':'G','G':'C','T':'A'}
comp_str = ''

for n in dna:
	comp_str += comp[n]
'''

comp_str = ''
for n in dna:
	if n == 'A': comp_str += 'T'
	elif n == 'C': comp_str += 'G'
	elif n == 'G': comp_str += 'C'
	else: comp_str += 'T'

rev = ''
for n in range(len(comp_str)):
	rev += comp_str[len(comp_str)-1-n]
print(rev)

