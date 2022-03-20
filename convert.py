from openbabel import openbabel
import os
from batch import batch_path

def convert_ligand(ligand_folder, output_folder):
    obConversion = openbabel.OBConversion()
    mol = openbabel.OBMol()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Converting ligands to .pdbqt format ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    for ligand in os.listdir(ligand_folder):
        f = os.path.join(ligand_folder, ligand)
        # checking if it is a file
        if os.path.isfile(f):
            ligand_path = ligand_folder + "/" + ligand
            print("Reading " + ligand + "...")
            obConversion.ReadFile(mol, ligand_path)

            ligand_root, ligand_tail = os.path.split(ligand_folder)
            out_name = output_folder + '/' + os.path.splitext(ligand)[0] + ".pdbqt"

            obConversion.WriteFile(mol, out_name)

            print('Converted ' + ligand + ' to ' + ligand + '.pdbqt')


def convert_smiles(top_ligands, num):
    smiles_array = []

    iterator = iter(top_ligands.items())

    for i in range(num):
        ligand = batch_path+'/'+(next(iterator)[0])
        #print(ligand)
        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("pdbqt", "smi")

        mol = openbabel.OBMol()
        obConversion.ReadFile(mol, ligand) 

        #out_name = os.path.splitext(ligand)[0] + ".smi"

        converted_smiles = obConversion.WriteString(mol)
        sep = '\t'
        smiles = converted_smiles.split(sep, 1)[0]
        smiles_array.append(smiles)
        
    return smiles_array
        



