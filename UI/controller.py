from model.model import Model
from UI.view import View
import flet as ft

class Controller:
    def __init__(self, view : View, model : Model):
        self._view = view
        self._model = model

    def handler_crea_grafo(self, e):
        n_bus = self._view._txt_nBus.value
        try:
            num_min_bus = int(n_bus)
            if num_min_bus < 0:
                self._view.show_alert("Inserire un valore positivo")
                return
        except(ValueError, TypeError):
            self._view.show_alert("Inserire un valore valido")
            return

        self._model.build_graph(num_min_bus)
        self._view._lst_result.controls.clear()
        self._view._lst_result.controls.append(ft.Text(f"Grafo creato correttamente: Nodi: {self._model.get_num_nodes()} - Archi: {self._model.get_num_edges()}"))
        self._view._lst_result.update()
        self._view._btnUtentiConnessi.disabled = False
        self._view._ddUtente.disabled = False
        self._view._txtL.disabled = False
        self._view._btnSequenza.disabled = False

        self.populate_dropdown()
        self._view._page.update()



    def handler_utenti_connessi(self, e):
        self._view._lst_result.controls.clear()
        for nodo in self._model.get_sum_weight_per_node():
            self._view._lst_result.controls.append(ft.Text(f" {nodo[0]} ({nodo[1]}) - strenght = {nodo[2]}"))
        self._view._lst_result.update()
        self._view._page.update()

    def populate_dropdown(self):
        for node in self._model._nodes:
            self._view._ddUtente.options.append(ft.dropdown.Option(text =node.name, key = node.user_id))

    def handler_read_utenti(self, e):
        id_utente_iniziale = self._view._ddUtente.value
        self._model.selected_utente = self._model._id_map[id_utente_iniziale]
        print(f"Utente selezionato: {self._model.selected_utente}")

        try:
            lung_sequenza = int(self._view._txtL.value)
        except(ValueError):
            self._view.show_alert("Inserire un valore valido")
            return
        if lung_sequenza < 2 or lung_sequenza > (self._model.get_num_nodes()):
            self._view.show_alert("Inserire un valore valido")







