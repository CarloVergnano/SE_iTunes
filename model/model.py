import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self._album_list = []
        self._playlist_list = []
        self._album_dict = {}
        for o in self._album_list:
            self._album_dict[o.id] = o
        self.G = nx.Graph()
        # TODO

    def build_graph(self, durata: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """


        self._track_list = DAO.readTrack()
        self._album_dict = {a.id: a for a in self._album_list}

        relazione = DAO.read_playlist_track()
        if relazione is None:
            print("Connessione fallita nel caricamento della relazione")
            return
        for row in relazione:
            album_id = row["album_id"]
            playlist_id = row["playlist_id"]
            tour = self.tour_map[id_tour]
            attrazione = self.attrazioni_map[id_attrazione]
            tour.attrazioni.add(attrazione)
            attrazione.tour.add(tour)

            self.G.add_edge(c.id_rifugio1, c.id_rifugio2, id = c.id, weight = peso)

        return self.G

    def get_nodes (self):
        self._album_list = DAO.readAlbum()
        self._track_list = DAO.readTrack()

        self.G.add_nodes_from(self._album_list)

        result = len(self._album_list)
        return result


