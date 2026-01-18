from dataclasses import dataclass

@dataclass()
class Album:
    id: int
    title: str
    minuti_tot: int



    def __str__(self):
        return f"Album({self.id}, {self.title}, {self.minuti_tot})"


    def __hash__(self):
        return hash(self.id)