import click

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
    import convert_ligand

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Ligand docking with AutoDock Vina ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import batch



