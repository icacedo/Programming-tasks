# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorithm vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

count = 0
for i in range(len(seq)):
	if len(seq[i:i+w]) == w:
		C = seq[i:i+w].count('C')
		G = seq[i:i+w].count('G')
		print(count, seq[i:i+w], f'{(G+C)/w:.4f}')
		count += 1
	else: continue

# nested loops seems a bit faster
# one loop is more compact
# GCs in the nested loop are counted once per inner loop
# GCs in the single loop are all counted at the same time every loop
