import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self._album_list = []
        self.connessioni = []
        self._album_dict = {}
        for o in self._album_list:
            self._album_dict[o.id] = o
        self.G = nx.Graph()
        # TODO

    def build_graph(self, durata: int):

        self._album_list = DAO.readAlbum(durata)
        self._connessioni = DAO.readConnAlbum()
        self._album_dict = {a.album_id: a for a in self._album_list}

        for c in self._connessioni:
            if c.album1 in self._album_dict and c.album2 in self._album_dict:
                self.G.add_edge(c.album1, c.album2)

        return self.G

    @staticmethod
    def load_album(durata: int):
        print(DAO.readAlbum(durata))
        return DAO.readAlbum(durata)

    def analizza_componente(self, album_id):

        componente = nx.node_connected_component(self.G, album_id)

        dimensione = len(componente)

        durata_totale = 0
        for a in componente:
            durata_totale += self._album_dict[a].durata

        return dimensione, durata_totale


