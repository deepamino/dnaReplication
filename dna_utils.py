class DNAUtils:

    nitro_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    def __init__(self):
        pass

    def get_complementary_strand(self, dna):
        complementary_strand = ''
        for base in dna:
            complementary_strand += DNAUtils.nitro_bases[base]
        return complementary_strandS