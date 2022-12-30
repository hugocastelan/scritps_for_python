# -*- coding: utf-8 -*- # NAME [split_names.py]	Version [1.0]
# AUTHOR  Hugo Castelan Sanchez 
# CREATED (2022-12)
# USAGE  python split_nfasta.py -f fasta or multifasta with can change the names 
# DESCRIPTION
# Change los headers 

import argparse
import re

#Para parsear el archivo 
parser=argparse.ArgumentParser()
requiredNamed=parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-f', '--file', help='Input multifasta or fasta')

args=parser.parse_args()
file=open(args.file)
lines=file.readlines()

outfile = open('headers_and_seqs.fasta', 'w')
headers = []
seqs = []
curr_seq = ''
for line in lines:
    line = line.rstrip('\n')
    if line.startswith('>'):
        headers.append(line.replace('/', '/').rpartition('/')[0])
        seqs.append(curr_seq)
        curr_seq = ''
    else:
        curr_seq += line.strip()
seqs.append(curr_seq)

for i in range(len(headers)):
    outfile.write(headers[i] + '\n' + seqs[i] + '\n')
outfile.close()
file.close()
