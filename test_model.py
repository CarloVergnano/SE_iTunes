from model.model import Model
m = Model()
m.build_graph(120)
m.load_album(120)
(dimensione, durata) = m.analizza_componente(141)
print((dimensione, durata))