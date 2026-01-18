import flet as ft
from UI.view import View
from model.model import Model
from database.DB_connect import DBConnect

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._connessione_db = DBConnect.get_connection()
        self.durata_selezionata = None


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self.durata_selezionata = int(self._view.txt_durata.value)
        self.grafo = self._model.crea_grafo(int(self.durata_selezionata))
        num_nodi = self.grafo.number_of_nodes()
        num_rami = self.grafo.number_of_edges()

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Grafo creato: {num_nodi} album, {num_rami} archi")
        )
        self._view.update()







    def on_album_change(self, e):
        if e.control.value is None:
            return
        self.album_selezionato = int(e.control.value)

    def popola_dropdown_album(self):
        """Popola il menu a tendina delle regioni."""
        self._view.dd_album.options.clear()
        if self.durata_selezionata is None:
            return
        else:
            self.durata_selezionata = int(self._view.txt_durata.value)
        album = self._model.get_album(self.durata_selezionata)

        if album:
            for a in album:
                self._view.dd_album.options.append(ft.dropdown.Option(key = a.id, text= a.title))
        else:
            self._view.show_alert("Errore nel caricamento album.")

        self._view.update()





    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""






    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""



