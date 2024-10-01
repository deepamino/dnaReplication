from dna_utils import DNAUtils
import threading
import random

class Polymerase:

    def replicate_leading_strand(self, dna, start, end):
        replication = ''
        for base in dna.strand[start:end]:
            replication += DNAUtils.nitro_bases[base]
        
        return replication
    
    def replicate_lagging_strand(self, dna, positions):
        replication = ''

        for i in range(len(positions)-1):
            fragment = dna.comp[positions[i]:positions[i+1]]
            replicated_fragment = ''
            for base in fragment[::-1]:
                replicated_fragment += DNAUtils.nitro_bases[base]

            replication += replicated_fragment[::-1]
        
        return replication
        

class PolymeraseOrchestrator:
    
        def __init__(self, dna, primers, scale = 20):
            self.dna = dna
            self.primers = primers
            self.scale = scale
        
        def get_dna_replica(self):
            replicated_fragments = []
            total_helicases = len(self.primers) - 1

            for i in range(total_helicases):
                polymerase = Polymerase()
                replicated_fragments.append(polymerase.replicate_leading_strand(self.dna, self.primers[i], self.primers[i+1]))
            
            replicated_fragments_lagging = []
            for i,positions in enumerate(self.okazaki_fragment_positions(self.primers, total_helicases)):
                polymerase = Polymerase()
                replicated_fragments_lagging.append(polymerase.replicate_lagging_strand(self.dna, positions))
            
            return ''.join(replicated_fragments), ''.join(replicated_fragments_lagging)
        

        def okazaki_fragment_positions(self, helicase_positions, total_helicase):

            for i in range(total_helicase):
                lagging_primer_positions = []
                fragment_lenght = helicase_positions[i+1] - helicase_positions[i]
                num_of_fragments = random.randint(total_helicase, fragment_lenght // self.scale)
                okazaki_length = fragment_lenght // num_of_fragments

                for j in range(num_of_fragments):
                    lagging_primer_positions.append(self.primers[i] + okazaki_length * j)

                lagging_primer_positions.append(helicase_positions[i+1])
                yield lagging_primer_positions
                
