# Visualizing Covid-19's RNA 
I thought it might be interesting to visualize the code in the Covid-19 virus based on the fact it has sugar proteins stitched into it's outer coating and those have to be forward encoded in its RNA, maybe in a loop or something. I found the virus decoded here:

https://www.ncbi.nlm.nih.gov/nuccore/MN988668

I decided to write code that first counted the number of codons of a particular length in the virus' dataset. In search, we call these words and documents. In search, a facet is a count of words appearing in a set of 'documents' with 'words' being broken by a given character, like a white space.

## How
I used vim to remove all line numbers and whitespace and placed it in *covid19_rna.txt*. I then created a random file of the same length and placed it in *random_rna.txt*.

I used a variety of word lengths, I'll call them *codons* here. Codon lengths of 5, 4 and 3 result in graphs that I consider to be regular in nature, but not necessarly odd. Codon lengths of 6, 7 and 8 result in distribution graphs which appear to follow the golden ratio (phi).

## Running
You'll need to hack around a bit to run this. I'll work on making better later. For now you can see the output in the output folder.

## Graphs
These graphs were generated from the output of the code for various codon lengths using Google Docs (spreadsheets).

For codon length 5 and below, the graphs seem to show a non-smooth curve in distribution. 

![word length is 5](https://github.com/kordless/covid19_viz/blob/master/pics/virus_graph_five.png?raw=true)

In codon lengths 6 and above, they appear to show curves that follow a fibonacci sequence. The number of the items in each unique count appear to be decreasing in size by the golden ratio, again for codon lengths 6 and up.

![word length is 7](https://github.com/kordless/covid19_viz/blob/master/pics/virus_graph_seven.png?raw=true)

Here's the unsorted graph for a codon length of 6 (the graph for 6 ordered looks similar to 7):

![word length is 6](https://github.com/kordless/covid19_viz/blob/master/pics/unsorted_virus_graph_six.png?raw=true)

Here's what random data looks like when you graph it and sort by string occurance:

![random data - word length is 6](https://github.com/kordless/covid19_viz/blob/master/pics/random_graph.png?raw=true)

## More Thoughts
I've found some information about how DNA uses phi:

https://www.goldennumber.net/dna/
