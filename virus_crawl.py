#!/usr/local/bin/python3 
import sys

f = open("fucking_virus_rna.txt", "r")
#f = open("fucking_random_rna.txt", "r")

# strings
# refactor this horrible mess
# function(codon_length=6)
# {'CATCAT': 42} use codon as key and store facet under it for faster scans
# GCAT
codons=[]
for one in "GCAT":
    for two in "GCAT":
        for three in "GCAT":
            for four in "GCAT":
                for five in "GCAT":
                    for six in "GCAT":
                        for seven in "GCAT":
                            for eight in "GCAT":
                                codon = ("%s%s%s%s%s%s%s%s" % (one,two,three,four,five,six,seven,eight))		
                                # print(codon)
                                codons.append({'name': codon, 'count': 0})

print("%s condons loaded" % len(codons))
sys.exit()
stack = "UUUUUU" # there are no Us in the virus code (shows phi relationship)
stack = "UUUUU" # there are no Us in the virus code 
stack = "UUUU" # there are no Us in the virus code 
stack = "UUU" # there are no Us in the virus code 
stack = "UUUUUUU" # there are no Us in the virus code (shows phi relationship)
stack = "UUUUUUUU" # there are no Us in the virus code (show phi relationship)

while True:
    char = f.read(1)  
    if char == "": break

    stack = stack[1:] # remove first letter
    stack = "%s%s" % (stack, char.upper()) # add new letter
 
    # print(stack)

    try:
        for i,codon in enumerate(codons):
            # print("%s to s%s" % (codon['name'], stack))
            if codon['name'] == stack:
                codons[i]['count'] = codons[i]['count'] + 1
                # print('%s to %s' % (codon['name'], codons[i]['count']))
    except:
        print('.')

for codon in codons:
    if codon['count'] > 0:
        print("%s,%s" % (codon['name'], codon['count']))


