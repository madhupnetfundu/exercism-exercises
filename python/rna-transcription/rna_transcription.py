def to_rna(dna_strand):
    dna = ['G','C','T','A']
    rna = ['C','G','A','U']
    rna_complement_dict = dict(zip(dna,rna))
    value = ''

    for letter in dna_strand:
        value += rna_complement_dict[letter]
    return value
