from dna_utils import DNAUtils
import random, time

class Polymerase:

    def replicate_leading_strand(self, dna, start, end):
        replication = ''
        for base in dna.strand[start:end]:
            replication += DNAUtils.nitro_bases[base]
        
        return replication
    
    def replicate_lagging_strand(self, dna, positions):
        replication = ''

        for i in range(len(positions)-1):
            print(f'The primer has been detected and it starts the replication process from {positions[i+1]} to {positions[i]}')
            time.sleep(0.3)
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

            print("Leading strand replication process...")
            time.sleep(1)

            print("Helicase unwinds the DNA double helix...")
            print("The unique primer of each the leading strand is placed at the 5' end of the DNA strand in positions: ", self.primers)
            print("----------------------------------------------------------------------------------------------------")
            print("The ADN polymerase enzyme is added to each primer and begins to synthesize the new DNA strand...")
            time.sleep(3)

            for i in range(total_helicases):
                polymerase = Polymerase()
                replicated_fragments.append(polymerase.replicate_leading_strand(self.dna, self.primers[i], self.primers[i+1]))
            
            print("The leading strand replication process is complete.")
            print("----------------------------------------------------------------------------------------------------")
            
            print("Lagging strand replication process...") 
            time.sleep(0.75)
            print("The lagging strand is synthesized in fragments called Okazaki fragments.")
            print("Helicases unwind the DNA double helix at the following positions: ", self.primers)
            print("----------------------------------------------------------------------------------------------------")

            replicated_fragments_lagging = []
            for i,positions in enumerate(self.okazaki_fragment_positions(self.primers, total_helicases)):
                print(f'Lagging strand replication for Helicase {i+1}')
                polymerase = Polymerase()
                replicated_fragments_lagging.append(polymerase.replicate_lagging_strand(self.dna, positions))
                print("----------------------------------------------------------------------------------------------------")
            
            print("Lagging strand's replication process has been completed")

            print("The replication process is complete.")
            return ''.join(replicated_fragments), ''.join(replicated_fragments_lagging)
        

        def okazaki_fragment_positions(self, helicase_positions, total_helicase):

            for i in range(total_helicase):
                lagging_primer_positions = []
                fragment_lenght = helicase_positions[i+1] - helicase_positions[i]
                num_of_fragments = random.randint((fragment_lenght - fragment_lenght/2) // self.scale, fragment_lenght // self.scale)
                okazaki_length = fragment_lenght // num_of_fragments

                for j in range(num_of_fragments):
                    lagging_primer_positions.append(self.primers[i] + okazaki_length * j)

                lagging_primer_positions.append(helicase_positions[i+1])
                yield lagging_primer_positions
                
