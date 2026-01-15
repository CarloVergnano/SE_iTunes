from dataclasses import dataclass
@dataclass
class Playlist:
    playlist_id: int
    track_id: int





    def __str__(self):
        return f"{self.playlist_id} {self.track_id} "

    #Serve per portare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.playlist_id)