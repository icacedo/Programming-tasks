# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

count = 0
for i in range(len(seq)):
	wn = seq[i:i+w]
	if len(wn) == w:
		GC = 0 
		for nt in wn:
			if nt == 'G' or nt == 'C': GC += 1
			else: continue
		print(count, wn, f'{GC/w:.4f}')
		count += 1
	else: continue
