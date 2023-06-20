import urllib.request
from Bio.PDB import PDBParser
import csv
import numpy as np
import datetime
import sys
now = datetime.datetime.now()

#Code takes in a PDB ID, downloads it from RCSB and outputs 2 files. The first file is a csv file containing all atoms that are part of the desired structure,
#the file is formatted as [chain][residue_number][residue_name][atom_name][x][y][z]. The second file is also in csv format, that contains all sites of Glycosylation
#and the plausible AA positions that are associated with them. These occasionally need to be checked manually. Overall, this code can be used as a prelude to a
#distance matrix calculation pipeline for all atoms in a structure.

# Define the directory and filenames
PDBID = '6ZGI'
file_dir = r'C:\Users\rojaschavez\Documents\\'
file_name = '6ZGI_test_3.csv'
link_file_name = '6MYY_link_info_3.csv'


# Download PDB file
pdb_url = "https://files.rcsb.org/download/"+PDBID+".pdb"  # Replace with the actual PDB file URL
pdb_file = PDBID+".pdb"  # Replace with the desired file name
urllib.request.urlretrieve(pdb_url, pdb_file)



# Parse PDB file
parser = PDBParser()
structure = parser.get_structure(PDBID, pdb_file)

# Extract atom coordinates and link information
atom_coordinates = []
link_information = []

for model in structure:
    for chain in model:
        for residue in chain:
            residue_name = residue.resname.strip()
            if residue_name == 'NAG':
                linked_residue_number = None
                linked_chain_id = None
                min_distance = float('inf')
                closest_residue = None
                nag_coords = None
                for atom in residue:
                    if atom.name == 'C1' and atom.element == 'C':
                        nag_coords = atom.coord
                        break
                if nag_coords is None:
                    continue
                for amino_chain in model:
                    for amino_residue in amino_chain:
                        if amino_residue.resname.strip() == 'ASN':
                            for amino_atom in amino_residue:
                                if amino_atom.name == 'ND2' and amino_atom.element == 'N':
                                    distance = np.linalg.norm(nag_coords - amino_atom.coord)
                                    if distance < min_distance:
                                        min_distance = distance
                                        closest_residue = amino_residue
                if closest_residue:
                    linked_residue_number = closest_residue.id[1]
                    linked_chain_id = closest_residue.parent.id
                link_information.append({
                    "chain": chain.id,
                    "residue_number": residue.id[1],
                    "residue_name": residue_name,
                    "linked_residue_number": linked_residue_number,
                    "linked_chain_id": linked_chain_id
                })
            for atom in residue:
                atom_coordinates.append({
                    "chain": chain.id,
                    "residue_number": residue.id[1],
                    "residue_name": residue_name,
                    "atom_name": atom.name,
                    "x": atom.coord[0],
                    "y": atom.coord[1],
                    "z": atom.coord[2]
                })

# Save coordinates to CSV
csv_file = file_dir + file_name
fieldnames = ["chain", "residue_number", "residue_name", "atom_name", "x", "y", "z"]
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(atom_coordinates)

# Save link information to separate CSV
link_fieldnames = ["chain", "residue_number", "residue_name", "linked_residue_number", "linked_chain_id"]
with open(file_dir + link_file_name, "w", newline="") as link_file:
    link_writer = csv.DictWriter(link_file, fieldnames=link_fieldnames)
    link_writer.writeheader()
    link_writer.writerows(link_information)

print("Atom coordinates saved to", csv_file)
print("Link information file name", link_file_name)
print("Start Date and Time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
now = datetime.datetime.now()
print("Finish Date and Time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
sys.exit()
