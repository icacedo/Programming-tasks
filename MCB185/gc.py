# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

GC = 0
for n in dna:
	if n == 'G' or n == 'C': GC += 1
	else: continue
print('%.2f' % (GC/len(dna)))
print('{:.2f}'.format(GC/len(dna)))
print(f'{GC/len(dna):.2f}')
