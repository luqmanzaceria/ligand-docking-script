import operator

affinity_rankings = {}
sorted_affinity = {}

def rank_affinities(ligand, log_file):

    affinity = []
    keep_phrases = ["-----"]

    with open(log_file) as f:
        f = f.readlines()

    phrase_detected = False

    found_affinity = False

    for line in f:
        if not found_affinity:
            if phrase_detected:
                affinity.append(line)
                found_affinity = True
            for phrase in keep_phrases:
                if phrase in line:
                    phrase_detected = True
                    break
    
    print(affinity)
    split_affinity = affinity[0].split(" ")

    while('' in split_affinity):
        split_affinity.remove('')

    top_affinity = split_affinity[1]
    affinity_rankings[ligand]=float(top_affinity)
    
    sorted_affinity = dict(sorted(affinity_rankings.items(), key=operator.itemgetter(1),reverse=False))
    print(sorted_affinity)
    return sorted_affinity

