#! /usr/bin/env python
import os 

def list_of_taxa():
	if os.path.exists('./fasta_files/taxa_order.txt') == True:
		f2 = open(os.path.join('./fasta_files', 'taxa_order.txt'), 'r')
		taxa = f2.readlines()
		taxa_list = []
		for i in range(len(taxa)):
			taxa_list.append(taxa[i].rstrip())
	else:
		taxa_list = []
		for i in os.listdir('./fasta_files'):
			list_tmp=[]
			if ".fasta" in i:
				list_tmp = parse_fasta(i)
				taxa_list += list_tmp[0]
		taxa_list = sorted(set(taxa_list))
		f_taxa_names=open('taxa_names_guessed_from_fasta_files.fas', 'w')
		for i in taxa_list:
			f_taxa_names.write(i + '\n')
	return taxa_list

def read_fasta_filenames():
	fasta_files=[]
	for i in os.listdir('./fasta_files'):
		if ".fasta" in i:
			fasta_files.append(i)
	return fasta_files

def parse_fasta(file_name):
	f = open(os.path.join("./fasta_files", file_name), 'r')
	new = [l for l in (line.strip() for line in f) if l]
	seq_names = []
	seqs = []
	temp_seq=''
	count=0
	fasta_list=[]
	for i in range(len(new)):
		if '>' in new[i]:
			seq_names.append(new[i])
			if count>0:
				seqs.append(temp_seq)
				temp_seq=''
		else:
			temp_seq=temp_seq + new[i]
			count = count +1
	seqs.append(temp_seq) # for the last sequence 
	fasta_list=[seq_names, seqs]
	return fasta_list

def reorder_fasta(fasta):
	reordered_names=[]
	reordered_seqs=[]
	count=0
	alignment_len=0
	taxa_list=list_of_taxa() # reading from list_of_taxa() definition
	for i in range(len(taxa_list)):
		for j in range(len(fasta[0])):
			count=0
			if taxa_list[i] == fasta[0][j]:
				reordered_names.append(taxa_list[i])
				reordered_seqs.append(fasta[1][j])
				count=1
				break
			alignment_len=len(fasta[1][j])
		if count==0 and alignment_len!=0:
			reordered_names.append(taxa_list[i])
			reordered_seqs.append("N"*int(alignment_len)) 
		if count==0 and alignment_len==0:
			reordered_names.append(taxa_list[i])
			reordered_seqs.append("N"*10)
	return reordered_names, reordered_seqs

def write_reordered_fasta():
	for i in read_fasta_filenames():
		f1 = open(os.path.join("./re-ordered_fasta", "re-"+str(i)), 'w')
		names, seqs = reorder_fasta(parse_fasta(i))
		for i in range(len(names)):
			f1.write(names[i] + '\n')
			f1.write(seqs[i] + '\n')
		f1.close()

