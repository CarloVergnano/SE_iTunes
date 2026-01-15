import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_grafo(self, e):
        """Callback per il pulsante 'Crea Grafo'."""
        try:
            durata = int(self._view.txt_durata.value)
        except:
            self._view.show_alert("Inserisci un numero valido.")
            return


        self._model.build_graph(durata)
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Grafo creato: {self._model.G.number_of_nodes()} nodi, {self._model.G.number_of_edges()} archi")
        )


    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO