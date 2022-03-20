import os
import subprocess
from ranking import *

vina_path = '/Users/luqmanzaceria/dev/docking/ligand-docking-script/vina/vinax' #input("Path to Vina: ")

conf_path = '/Users/luqmanzaceria/dev/docking/ligand-docking-script/vina/conf_vs.txt' #input("Path to configuration file: ")

batch_path = '/Users/luqmanzaceria/dev/docking/ligand-docking-script/vina/ligands' #input("Path to ligand directory: ")

out_path = '/Users/luqmanzaceria/dev/docking/docking_logs' #input("Desired output directory: ")


for ligand in os.listdir(batch_path):
    f = os.path.join(batch_path, ligand)
    # checking if it is a file
    if os.path.isfile(f):
        print("Docking " + ligand + "...")
        ligand_path  = batch_path + "/" + ligand
        log_name = (out_path+'/'+ligand.split('\\')[-1].split('.')[0]+ "_log.log")
        out_name = (out_path+'/'+ligand.split('\\')[-1].split('.')[0]+ "_out.pdbqt")
        
        args = [vina_path, '--config', conf_path, '--ligand' , ligand_path, '--log', log_name, '--out', out_name]
        subprocess.run(args)

    sorted_affinity = rank_affinities(ligand, log_name)
    
    
def vina_docking(vina_path,conf_path,batch_path,out_path):
    for ligand in os.listdir(batch_path):
        f = os.path.join(batch_path, ligand)
        # checking if it is a file
        if os.path.isfile(f):
            print("Docking " + ligand + "...")
            ligand_path  = batch_path + "/" + ligand
            log_name = (out_path+'/'+ligand.split('\\')[-1].split('.')[0]+ "_log.log")
            out_name = (out_path+'/'+ligand.split('\\')[-1].split('.')[0]+ "_out.pdbqt")
            
            args = [vina_path, '--config', conf_path, '--ligand' , ligand_path, '--log', log_name, '--out', out_name]
            subprocess.run(args)

        rank_affinities(ligand, log_name)
    
    
        

