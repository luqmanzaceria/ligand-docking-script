import pubchempy as pcp

def similar_ligands(smiles, out_path):

    pubchem_similar = pcp.get_compounds(smiles, 'smiles',searchtype='similarity', listkey_count=3)
    print(pubchem_similar)

    for mol in pubchem_similar:
        syn = mol.synonyms[0]
        pcp.download('SDF', out_path+'/'+syn+'.sdf', syn, 'name')

