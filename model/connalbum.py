from dataclasses import dataclass
@dataclass
class ConnAlbum:
    album1: int
    album2: int





    def __str__(self):
        return f"{self.album1} {self.album2} "

    #Serve per portare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.album1)