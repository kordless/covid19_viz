# Visualizing Covid-19's RNA 
I thought it might be interesting to visualize the code in the Covid-19 virus based on the fact it has sugar proteins stitched into it's outer coating and maybe I could find them with code. To start out, I found the virus' genome decoded here:

https://www.ncbi.nlm.nih.gov/nuccore/MN988668

I wrote code that first counted the number of codons of a particular length in the virus' genomic dataset. In search, we call strings words and the entire data set a document. A facet is a count of strings appearing in a set of 'documents' with 'words' being broken by a given character, like a white space.

In the case of this virus, I'm breaking the words along fixed lengths of nucleotides. I've graphed 3, 4, 5, 6, 7 and 8 character length words so far.

## How
I used vim to remove all line numbers and whitespace and placed it in *covid19_rna.txt*. I then created a random file of the same length and placed it in *random_rna.txt*.

I used a variety of word lengths, I'll call them *codons* here. Codon lengths of 5, 4 and 3 result in graphs that I consider to be regular (ordered) in nature, but not necessarly odd looking. Codon lengths of 6, 7 and 8 result in distribution graphs which appear to follow the golden ratio (phi). My code needs to be refactored to do longer sequences.

## Running
You'll need to hack around a bit to run this. I'll work on making better later. For now you can see the output in the output folder.

## Graphs
These graphs were generated from the output of the code for various codon lengths using Google Docs (spreadsheets).

For codon length 5 and below, the graphs seem to show a non-smooth curve in distribution.  Please note that not all nucleotide sequences are shown in the labeling, but the counts are all there.

![word length is 5](https://github.com/kordless/covid19_viz/blob/master/pics/virus_graph_five.png?raw=true)

In codon lengths 6 and above, they appear to show curves that follow a fibonacci sequence. The number of the items in each unique counts appear to be increasing in size by the golden ratio, while the counts themselves are decreasing. Again, this appears for codon lengths 6 and up.

![word length is 7](https://github.com/kordless/covid19_viz/blob/master/pics/virus_graph_seven.png?raw=true)
![word length is 6](https://github.com/kordless/covid19_viz/blob/master/pics/virus_graph_six.png?raw=true)

Here's the unsorted graph for a codon length of 6:

![word length is 6](https://github.com/kordless/covid19_viz/blob/master/pics/unsorted_virus_graph_six.png?raw=true)

Here's what random data looks like when you graph it and sort by string occurance:

![random data - word length is 6](https://github.com/kordless/covid19_viz/blob/master/pics/random_graph.png?raw=true)

## More Thoughts
I've found some information about how DNA uses phi.

Fluffy: https://www.goldennumber.net/dna/
Hard: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2863758/

Here's stuff I found using the odd flat groupings of sequences in the 5 length words of the virus:

```
66 occurances each
AAAAG https://www.ncbi.nlm.nih.gov/pubmed/264240
AATTG https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5334452/
ACATT https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5778463/
ACTTA https://www.ncbi.nlm.nih.gov/pmc/articles/PMC323787/
ATGCT https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2977869/
CAATT https://www.ncbi.nlm.nih.gov/pubmed/9786894
CTATT https://www.microbiologyresearch.org/docserver/fulltext/jgv/74/12/JV0740122539.pdf?expires=1585808280&id=id&accname=guest&checksum=568B9B26882A4A88F1355CEE1716DE5E
TACTA https://jvi.asm.org/content/jvi/79/11/6918.full.pdf and https://www.sciencedirect.com/science/article/pii/S004268221730048X

65 each
TGCTA https://jvi.asm.org/content/jvi/84/19/10266.full.pdf
TTGAA https://www.microbiologyresearch.org/docserver/fulltext/jgv/98/5/946_vir000758.pdf?expires=1585808671&id=id&accname=guest&checksum=2C2374257B060DA42469D9A1A838A096

64 each
AATGG https://www.nature.com/articles/s41467-018-07944-x
TAAAG https://jvi.asm.org/content/jvi/51/3/754.full.pdf
TAAAT https://pdf.sciencedirectassets.com/272412/1-s2.0-S0042682200X06691/1-s2.0-004268229090513Q/main.pdf
TGACA https://www.researchgate.net/publication/6399009_Plant_lectins_are_potent_inhibitors_of_coronaviruses_by_interfering_with_two_targets_in_the_viral_replication_cycle#pf3
TGTAG https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.0030005
TTCAA https://link.springer.com/content/pdf/10.1007%2F978-1-4684-1280-2_6.pdf
TTGAT https://patents.google.com/patent/CA2953677A1/en

56 each
AAACT https://patentimages.storage.googleapis.com/48/4b/34/400b8f64987e55/US7888102.pdf
AGACA https://virologyj.biomedcentral.com/articles/10.1186/s12985-017-0747-z
AGATG https://www.researchgate.net/publication/7225941_High_expression_level_of_soluble_SARS_spike_protein_mediated_by_adenovirus_in_HEK293_cells
CTAAT https://patents.google.com/patent/CN1815234B/en
CTTCT https://pdf.sciencedirectassets.com/272412/1-s2.0-S0042682200X00530/1-s2.0-S0042682200902186/main.pdf
GAAAA https://www.researchgate.net/publication/232220254_Detection_of_a_novel_human_coronavirus_by_real-time_reverse-transcription_polymerase_chain_reaction
GAAGA https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7087027/
GTTAC https://jvi.asm.org/content/jvi/82/3/1465.full.pdf
TAAAC https://en.wikipedia.org/wiki/Expression_cassette and https://jvi.asm.org/content/jvi/69/12/7851.full.pdf
TATGT https://www.tandfonline.com/doi/pdf/10.1080/03079450120066368
TCAAA https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763971/
TGATT sciencedirect.com/science/article/pii/S0042682208005230 (ACE2 warning)
TGTCT https://www.microbiologyresearch.org/docserver/fulltext/jgv/68/10/JV0680102639.pdf
TTTGA https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6178081/

''''


