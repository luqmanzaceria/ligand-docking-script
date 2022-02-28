from vina import Vina
import os

v = Vina(sf_name='vina')

batch_path = input("Path to ligand directory: ")

receptor = input("Receptor file name: ")
v.set_receptor(receptor)

custom_conf = input("Customize docking configuration? (y/n) ")
if input == 'y':
    v.compute_vina_maps(center=[center_x, center_y, center_z], box_size=[size_x, size_y, size_z])
elif input == 'n':
    print("Will perform blind docking.")
else:
    custom_conf
    



for ligand in os.listdir(batch_path):
    f = os.path.join(batch_path, ligand)
    # checking if it is a file
    if os.path.isfile(f):
        v.set_ligand_from_file(ligand)
        
        # Dock the ligand
        v.dock(exhaustiveness=32, n_poses=20)
        v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=5, overwrite=True)