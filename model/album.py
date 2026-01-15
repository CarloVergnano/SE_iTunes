from dataclasses import dataclass
@dataclass
class Album:
    album_id: int
    title: str
    minuti_totali: float

    def __str__(self):
        return f"{self.album_id} {self.title} {self.minuti_totali}  "

    #Serve per portare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.album_id)
