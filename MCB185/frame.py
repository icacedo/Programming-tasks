# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

count = 0
for n in range(len(dna)):
	if count == 0: 
		print(n, '0', dna[n])
		count += 1
	elif count == 1: 
		print(n, '1', dna[n])
		count += 1
	elif count == 2: 
		print(n, '2', dna[n])
		count = 0

