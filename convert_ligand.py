from openbabel import openbabel
import os

# caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C

obConversion = openbabel.OBConversion()
mol = openbabel.OBMol()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Converting ligands to .pdbqt format ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

ligand_folder = input('Path to ligand folder: ')
output_folder = input('Path to output folder: ')


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




