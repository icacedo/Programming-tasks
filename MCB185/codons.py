# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

count = 0
for c in range(len(dna)):
	if len(dna[c:c+3]) == 3 and count%3 == 0:
		print(dna[c:c+3])
		count += 1
	else: count += 1
	

	

