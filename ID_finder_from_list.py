# -*- coding: utf-8 -*- # NAME [ID_finder_from_list]  Version [1.0]
# AUTHOR  Hugo Castelan Sanchez 
# CREATED (2023-01)
# USAGE ID_finfer_from_list.py fasta_file.fasta  id_file.txt output_file.fasta 
# DESCRIPTION
# Obtiene las secuencias a partir de un multifasta 



import argparse
import re

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments for the FASTA file and ID file
parser.add_argument("fasta_file", help="the FASTA file to read")
parser.add_argument("id_file", help="a file with a list of IDs to match")
parser.add_argument("output_file", help="the output file to write the matching sequences to")

# Parse the command-line arguments
args = parser.parse_args()

# Read the IDs from the separate file into a list
with open(args.id_file, "r") as id_file:
  id_list = [line.strip() for line in id_file]

# Initialize a dictionary to store the identifiers and sequences
sequences = {}

# Open the FASTA file in read mode
with open(args.fasta_file, "r") as fasta_file:
  # Initialize variables to store the identifier and sequence
  identifier = ""
  sequence = ""
  # Iterate over the lines in the file
  for line in fasta_file:
    # Check if the line starts with a ">" character
    if line[0] == ">":
      # If this is a new identifier, store the previous identifier and sequence (if they exist)
      if identifier and sequence:
        # Store the identifier and sequence in the dictionary if the identifier is in the list of IDs to match
        if identifier in id_list:
          sequences[identifier] = sequence
      # Store the new identifier by removing the ">" character
      identifier = line[1:].strip()
      # Reset the sequence
      sequence = ""
    else:
      # If this is a sequence line, append it to the current sequence if the identifier is in the list of IDs to match
      if identifier in id_list:
        sequence += line.strip()

# Store the final identifier and sequence if it is in the list of IDs to match
if identifier in id_list:
  sequences[identifier] = sequence

# Open the output file in write mode
with open(args.output_file, "w") as output_file:
  # Iterate over the identifiers and sequences in the dictionary
  for identifier, sequence in sequences.items():
    # Write the identifier and sequence to the output file
    output_file.write(f">{identifier}\n{sequence}\n")
