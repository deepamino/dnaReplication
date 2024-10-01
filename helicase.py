import random

class Helicase:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    
class Orchestrator:

    def __init__(self, dna, rate=0.25):
        self.nucleotides = dna.nucleotides
        self.rate = rate
        self.number_of_helicases = self.nucleotides // int(self.rate * self.nucleotides)
        self.helicases = []

    def define_helicases(self):
        helicase_positions = [self.nucleotides // self.number_of_helicases * i for i in range(1, self.number_of_helicases)]
        helicase_positions.insert(0, 0)

        for i in range(1,self.number_of_helicases-1):
            rand_value = random.randint(0, 50)
            rand_sign = random.randint(1, 2)

            helicase_positions[i] += (-1)**rand_sign * rand_value

        helicase_positions.append(self.nucleotides)
        for i in range(0, len(helicase_positions)-1):
            self.helicases.append(Helicase(helicase_positions[i], helicase_positions[i+1]))
    
    def get_Helicase(self, index):
        return self.helicases[index]

    