
# function to detect mutation

with open("plasmid.txt") as masterfile:
	dna = masterfile.readline().strip()
	print(dna+" (Original AA)")

with open("list.txt") as infile:
	cdna = ()
	cdna = infile.readlines()


count = 0 
for x, y in zip(dna,cdna):
	if x == y:
		count = count + 1
		if count > 49:
			print(cdna + "WT")
			break
	else:
		wt_res = x
		mut_res = y
		count = count + 1
		if count > 49:
			break

		
	

