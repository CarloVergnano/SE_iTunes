import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.album = []
        self.connessione = []

    def get_album (self, durata):
        self.album = DAO.get_album(durata)
        return self.album

    def crea_grafo(self, durata):
        self.album = DAO.get_album(durata)
        self.connessione = DAO.get_connessione(durata)
        for c in self.connessione:
            self.G.add_edge(c.album1, c.album2)
        return self.G

    def get_component(self, album):
        """Restituisce la componente connessa di un album"""
        componente = list(nx.node_connected_component(self.G, int(album)))

        # componente.remove(int(album))

        return componente