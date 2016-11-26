#! /usr/bin/env python
import os
from reorder import write_reordered_fasta

def read_fasta_filenames():
	fasta_files=[]
	for i in os.listdir('./re-ordered_fasta'):
		if "re-" in i:
			fasta_files.append(i)
	return fasta_files

def parse_fasta(file_name):
	f = open(os.path.join("./re-ordered_fasta", file_name), 'r')
	new = [l for l in (line.strip() for line in f) if l]
	seq_names = []
	seqs = []
	temp_seq=''
	count=0
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
	return seq_names, seqs

def check_names(list_of_names):
	check = ''
	name_test=''
	for i in range(1, len(list_of_names)):
		if list_of_names[0]==list_of_names[i]:
			check = 'names are ok'
		else:
			check = 'Problem'
			name_test='WARNING: There is a problem with the names! Please, check and re-run the script'
	return name_test

def write_concatenated_fasta(seq_names, con_sequences):
	f = open('concatenated.fas', 'w')
	for i in range(len(seq_names)):
		f.write(str(seq_names[i])+'\n')
		f.write(str(con_sequences[i]) +'\n')
	f.close()

def all_fasta_content():
	all_taxa_names = []
	all_sequences = []
	for i in read_fasta_filenames():
		taxa, sequences = parse_fasta(i)
		all_taxa_names.append(taxa)
		all_sequences.append(sequences)
	return all_taxa_names, all_sequences, taxa

if __name__== "__main__":
	if os.listdir('re-ordered_fasta')!="":
		os.system('rm re-ordered_fasta/*' )
	if os.path.exists('./fasta_files/taxa_order.txt') == False:
		print "\nWARNING: No file \"taxa_order.txt\" was found in the \"fasta_files\" folder. The taxa names were retrieved from the fasta files.\n"
		print "A list of the taxa names is written in \"taxa_names_guessed_from_fasta_files.fas\" in your current directory"
	write_reordered_fasta()
	concatenated_sequences=[]
	temp_seq=''
	count=0
	all_taxa_names, all_sequences, taxa = all_fasta_content()
	print check_names(all_taxa_names)
	if check_names(all_taxa_names) == '':
		for j in range(len(all_sequences[0])):
			for i in range(len(all_sequences)):
				count=count+1
				temp_seq = temp_seq + all_sequences[i][j]
				'''print count'''
				if count >= len(all_sequences):
					count=0
					concatenated_sequences.append(temp_seq)
					temp_seq=''
					break
		write_concatenated_fasta(taxa, concatenated_sequences)
		print 'The fasta files processed were: '+ ', '.join(read_fasta_filenames()) + '. \nA concatenated fasta file is written in your current directory\n'
		
