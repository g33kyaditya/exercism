def to_rna(dna) :

    if dna == '':
        return ''

    rna = list(dna)
    for i in range(0, len(rna)) :
        strand = rna[i]
        if strand == 'G' :
            rna[i] = 'C'
        elif strand == 'C' :
            rna[i] = 'G'
        elif strand == 'T' :
            rna[i] = 'A'
        elif strand == 'A' :
            rna[i] = 'U'
        else :
            return ''

    ret = ''.join(rna)
    return ret
