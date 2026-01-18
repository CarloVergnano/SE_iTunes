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
        self.album = []



    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self.durata_selezionata = int(self._view.txt_durata.value)
        self.popola_dropdown_album()
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
        self._view.dd_album.options.clear()

        valore = self._view.txt_durata.value

        if not valore or not valore.strip().isdigit():
            self._view.show_alert("Inserisci una durata valida")
            return

        self.durata_selezionata = int(valore)

        self.album = self._model.get_album(self.durata_selezionata)

        if self.album:
            for a in self.album:
                self._view.dd_album.options.append(
                    ft.dropdown.Option(key=a.id, text=a.title)
                )
        else:
            self._view.show_alert("Nessun album trovato")

        self._view.update()

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        album_selezionato = int(self._view.dd_album.value)
        componenti = self._model.get_component(album_selezionato)
        self.durata_selezionata = int(self._view.txt_durata.value)
        album_list = self._model.get_album(self.durata_selezionata)
        album_dict = {a.id: a for a in album_list}
        durata_tot = 0
        for c in componenti:
            if c in album_dict:
                durata_tot = album_dict[c].minuti_tot + durata_tot

        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f" Dimensione componente:  {len(componenti)}"))
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f" Durata totale: {durata_tot} minuti"))


        self._view.update()








    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""



