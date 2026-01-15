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

    def popola_dropdown_album(self, durata: int):
        """Popola il menu a tendina delle regioni."""
        self._view.dd_album.options.clear()

        album = self._model.load_album(durata) # Ogni regione (id, nome_regione)

        if album:
            for regione in sorted(album):
                self._view.dd_album.options.append(ft.dropdown.Option(key=regione.album_id,text=regione.title))
        else:
            self._view.show_alert("Errore nel caricamento degli album.")

        self._view.update()


    def handle_analisi_comp(self, e):
        a1 = self._view.dd_album

        dimensione, durata = self._model.analizza_componente(a1.album_id)

        self._view.lista_visualizzazione_3.controls.append(
            ft.Text(f"Dimensione componente: {dimensione}"),
            ft.Text(f"Durata minuti: {durata}"))

        self._view.update()



    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO