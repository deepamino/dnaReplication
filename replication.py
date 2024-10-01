from helicase import Helicase, Orchestrator
from polymerase import PolymeraseOrchestrator


class Replication:

    def execute(self, dna, rate=0.25):
        helicase_orchestrator = Orchestrator(dna, rate)
        helicase_orchestrator.define_helicases()

        primers = self.get_primers_from_helicases(helicase_orchestrator.helicases)
        polymerase_orchestrator = PolymeraseOrchestrator(dna, primers, scale=20)
        return polymerase_orchestrator.get_dna_replica()

    def get_primers_from_helicases(self, helicases):
        primers = []
        primers.append(helicases[0].start)
        for helicase in helicases:
            primers.append(helicase.end)
        return primers

        
    