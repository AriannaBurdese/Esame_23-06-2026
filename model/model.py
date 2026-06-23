from database.dao import Dao
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = None
        self._edges = None
        self._lista_users = []
        self._lista_connessioni = []
        self._id_map = {}
        self.selected_utente = []
        #self._users_list = []
        #self.load_all_users()

    """def load_all_users(self):
        self._users_list = Dao.read_all_users()
        print(f"Users: {self._users_list}")"""

    def load_users(self, n_bus):
        self._lista_users = Dao.get_users(n_bus)
    def load_connessioni(self):
        self._lista_connessioni = Dao.get_connessioni()

    def build_graph(self, n_bus):
        self._graph.clear()
        self._nodes = []
        self._edges = []
        self._id_map = {}
        self.load_users(n_bus)
        print(f"Trovati {len(self._lista_users)} users")
        self.load_connessioni()
        print(f"Trovati {len(self._lista_connessioni)} connessioni")
        #vado a riempirmi i nodi
        for user in self._lista_users:
            self._nodes.append(user)
            self._id_map[user.user_id] = user
        self._graph.add_nodes_from(self._nodes)
        for c in self._lista_connessioni:
            w = c.peso
            if (c.user1 in self._id_map and c.user2 in self._id_map):
                u1 = self._id_map[c.user1]
                u2 = self._id_map[c.user2]
                self._graph.add_edge(u1, u2, weight=w)
                self._edges.append(c)

        print(self._graph)

    def get_num_nodes(self):
        return self._graph.number_of_nodes()

    def get_num_edges(self):
        return self._graph.number_of_edges()

    def get_sum_weight_per_node(self):
        pesi = []
        for nodo in self._graph.nodes():
            sum_w = 0
            for arco in self._graph.edges(nodo, data=True):
                sum_w += arco[2]["weight"]
            pesi.append((nodo.name, nodo.user_id, sum_w))
            pesi.sort(key=lambda x: x[2], reverse = True)
        return pesi




