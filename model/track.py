from dataclasses import dataclass
@dataclass
class Track:
    id: int
    album_id: int
    minuti: float




    def __str__(self):
        return f"{self.id} {self.album_id} {self.minuti}  "

    #Serve per portare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.id)