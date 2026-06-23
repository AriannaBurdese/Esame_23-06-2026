from model.model import Model

model = Model()
n_bus = 35
model.load_users(n_bus)
model.build_graph(n_bus)