import os
import subprocess

vina_path = input("Path to Vina: ")

conf_path = input("Path to configuration file: ")

batch_path = input("Path to ligand directory: ")


for ligand in os.listdir(batch_path):
    f = os.path.join(batch_path, ligand)
    # checking if it is a file
    if os.path.isfile(f):
        print("Docking " + ligand + "...")
        ligand_path  = batch_path + "/" + ligand
        log_name = (ligand.split('\\')[-1].split('.')[0]+ "_log.log")
        
        args = [vina_path, '--config', conf_path, '--ligand' , ligand_path, '--log', log_name]
        subprocess.run(args)