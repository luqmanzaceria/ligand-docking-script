import click
from convert import *
from pubchem_similar import *

print('########################################')
print('#     Protein-Ligand Docking Script    #')
print('#          for Drug Discovery          #')
print('########################################')


def receptor_prepped():
    if click.confirm('Is receptor prepared for docking?', default=True):
        return True
    return False

def ligands_prepped():
    if click.confirm('Are ligands prepared for docking?', default=True):
        return True
    return False

if not receptor_prepped():
    print('* Please prepare receptor as .pdbqt file using AutoDockTools *')

if  not ligands_prepped():
    ligand_folder = input('Path to ligand folder: ')
    output_folder = input('Path to output folder: ')

    convert_ligand()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Ligand docking with AutoDock Vina ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

from batch import *

smiles = convert_smiles(sorted_affinity,2)
print(smiles)

similar_path = input("Output path for similar ligands found from Pubchem: ")

for mol in smiles:
    print(mol)
    similar_ligands(mol,similar_path)

converted_pubchem_ligands = input("Desired output path of pubchem ligands converted to .pdbqt: ")
convert_ligand(similar_path, converted_pubchem_ligands)

vina_docking(vina_path,conf_path,converted_pubchem_ligands,out_path)

# gromax







