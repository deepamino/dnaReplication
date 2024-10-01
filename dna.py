from dna_utils import DNAUtils

class DNA:
    dna_utils = DNAUtils()

    def __init__(self, dna):
        self.strand = dna
        self.comp = DNA.dna_utils.get_complementary_strand(dna)
        self.nucleotides = len(dna)
    
    def show_nucleotides(self):
        print(f"Number of nucleotides: {self.nucleotides}")