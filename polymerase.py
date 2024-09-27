class Polymerase:
    def __init__(self):
        self.nitro_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    def replication_leading_strand(self, start, end, dna_seq):
        replication = dna_seq[start:end]
        print(replication)

        for base in dna_seq:
            replication += self.nitro_bases[base]
        return replication