
#forma de uso python remove_sequences.py input.fasta IDs.txt output.fasta
import sys
from Bio import SeqIO

# Parse the multi-FASTA file
sequences = list(SeqIO.parse(sys.argv[1], 'fasta'))

# Read the list of IDs to remove
with open(sys.argv[2]) as f:
    ids_to_remove = f.read().splitlines()

# Remove the sequences with the specified IDs
filtered_sequences = [s for s in sequences if s.id not in ids_to_remove]

# Write the filtered sequences to a new FASTA file
SeqIO.write(filtered_sequences, sys.argv[3], 'fasta')