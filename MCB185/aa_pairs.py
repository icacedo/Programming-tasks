# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

aa_list = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
count1 = 0
count2 = 0
for aa1 in range(len(aa_list)):
	for aa2 in range(count1,len(aa_list)):
		if aa1 == aa2: continue
		print(aa_list[aa1],aa_list[aa2])
		count2 += 1
	count1 += 1
print(count2)


