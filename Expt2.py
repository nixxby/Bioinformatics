#Opening a file in fasta format 
file_mdm2 = open("sequence-mdm2-Homosapiens.txt")  
 
#Skip first line 
headerline = file_mdm2.readline() 
 
#Read rest of the 
gene = file_mdm2.read() 
 
#Remove Newline characters 
gene = gene.replace("\n", "") 
 
#Compute length of the genome 
genlen= len(gene) 
 
#Print the genone 
print(gene) 

#Print Result#1 
print("\n\n1. Number of Base Pairs: "+str(genlen) + " bps") 
 
#Print Result#2
start_codon=gene.count("ATG") 
print("2. Number of Start codons are " + str(start_codon)) 
 
#Print Result#3
stop_codon = gene.count("TAA") 
stop_codon += gene.count("TGA") 
stop_codon += gene.count("TAG") 
print("3. Number of Stop codons are " + str(stop_codon)) 
 
#Count the number of A, T, G, C present in genome
A = gene.count("A") 
T = gene.count("T") 
G = gene.count("G") 
C = gene.count("C") 
 
print("\nNumber of A's : " + str(A)) 
print("Number of T's : " + str(T)) 
print("Number of G's : " + str(G)) 
print("Number of C's : " + str(C)) 
 
#Print Result#4 
print("\n4. a) The GC percentage is " + str(round((G+C)/genlen*100,2))+ " % " ) 
print("4. b) The AT percentage is " + str(round((A+T)/genlen*100,2))+ " % " )
