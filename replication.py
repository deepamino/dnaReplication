from helicase import HelicaseOrchestrator
from polymerase import PolymeraseOrchestrator


class Replication:

    def execute(self, dna, rate=0.005, scale=20):
        helicase_orchestrator = HelicaseOrchestrator(dna, rate=rate)
        helicase_orchestrator.show_number_of_helicases()
        helicase_orchestrator.define_helicases()
    
        primers = self.get_primers_from_helicases(helicase_orchestrator.helicases)
        polymerase_orchestrator = PolymeraseOrchestrator(dna, primers, scale=scale)
        return polymerase_orchestrator.get_dna_replica()

    def get_primers_from_helicases(self, helicases):
        primers = []
        primers.append(helicases[0].start)
        for helicase in helicases:
            primers.append(helicase.end)
        return primers

        
    