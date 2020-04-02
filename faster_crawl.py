#!/usr/local/bin/python3 
import sys

#f = open("sars_rna.txt", "r")
f = open("covid19_rna.txt", "r")
#f = open("random_rna.txt", "r")

# strings
# function(codon_length=6)
# TODO {'CATCAT': 42} use codon as key and store facet under it for faster scans
# GCAT
codons = {}

stack_size = int(sys.argv[1])
limit = int(sys.argv[2])

# create frame 
# size is determined by number of Us
stack = "" # no Us in virus code
for i in range(stack_size):
    stack += "U" 

while True:
    char = f.read(1).upper()
    if char not in "GCAT": 
        break
    if len(stack) < stack_size:
        break

    stack = stack[1:] # remove first letter
    stack = "%s%s" % (stack, char) # add new letter    

    if "U" not in stack and len(stack) == stack_size:
        try:
            codons[stack]['count'] += 1 # found existing codon, increment count
        except:
            codons[stack] = {"count": 1} # found a new codon, set count to 1

limit_count = 0
for codon in codons.items():
    if codon[1]['count'] > limit:
        limit_count += 1
        print("%s,%s" % (codon[0],codon[1]['count']))

print("number of unique strings of length %s: %s" % (len(stack), len(codons.items())))
print("number of unique strings with above limit %s: %s" % (limit, limit_count))
