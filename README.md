# FastaCon

This script will concatenate multiple fasta files into a new one, called "concatenated.fas". 
The samples in the fasta files don't need to be in the same order, and each of them may contain a
subset of the samples. If a sample is missing from a fasta file it will be filled in with "N"s x length 
of the alignment. Additionaly, the original fasta files will be re-ordered in the same way and they will
be stored in the "re-ordered_fasta" directory.

Input files:

1) fasta formated files in the folder "fasta_files" 

2) a list of all taxa names included in the fasta files, called "taxa_order.txt" and it should be placed in the
directory "fasta_files" (check examples for format). The concatenated sequences will be written in the concatenated.fas 
file according to "taxa_order.txt". If "taxa_order.txt" is missing the taxa names will be retrieved from the fasta files 
found in the "fasta_files" folder. The list of taxa will then be written in the "taxa_names_guessed_from_fasta_files.fas"
file in the "Con_V3" directory

Prerequisites:

1) No fasta file should start with the suffix "re-"

2) use Python v.2.7.5 or higher

Instructions:

1) linux: 

	a) retain the folder structure as in the zip file i.e. one directory containing the scripts 
           (reorder.py, fastacon.py,reorder.pyc), the info.txt and two subfolders called "fasta_files", 
           "re-ordered_fasta" and "example_files"

	c) open a terminal and navigate it to the folder containing the "./fastacon.py" script

	d) write in the terminal command line "./fastacon.py"

	if everything worked fine you will get a verifying message telling you that a concatenated fasta file was 
        created in your directory

2) windows:

     a) retain the folder structure as in the zip file i.e. one directory containing the scripts
           (reorder.py, fastacon.py,reorder.pyc), the info.txt and two subfolders called "fasta_files",
           "re-ordered_fasta" and "example_files"

	*c) in "start" type "cmd" and navigate it to the folder containing the "./fastacon.py" script.

	*d) type in the cmd "python fastacon.py"

	if everything worked fine you will get a verifying message telling you that a concatenated fasta file was 
        created in your directory

Example:

To run the example just copy all the files from "example_files" to "fasta_files" and follow the guidlines above.

*** one.fasta --> it does not matter if the sequences are in one or multiple lines

*** two.fasta --> it does not matter if there are empty lines between the entries, or between the taxon name and the sequence 

*** three.fasta --> the letters may be capital or small (any letters are ok)

*** four.fasta --> it is ok if any or all sequences are missing (empty file), they will be replaced with 'N'x alignment length 

*** the sequences may be in whatever order in each fasta file, as long as the same name are used throughout all files
(fasta files and taxa_order.txt file)

For any problems, please contact me at k.pashalia@gmail.com 
