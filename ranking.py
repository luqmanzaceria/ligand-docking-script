def rank_affinities(ligand, log_file):
    affinity_rankings = {}

    affinity = []
    keep_phrases = ["-----"]

    with open(log_file) as f:
        f = f.readlines()

    phrase_detected = False

    for line in f:
        if phrase_detected:
            affinity.append(line)
            phrase_detected = False
        for phrase in keep_phrases:
            if phrase in line:
                phrase_detected = True
                break

    split_affinity = affinity[0].split(" ")

    while('' in split_affinity):
        split_affinity.remove('')

    top_affinity = split_affinity[1]
    affinity_rankings[ligand]=(top_affinity)
    print(affinity_rankings)
