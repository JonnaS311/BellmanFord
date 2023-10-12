from algoritmo import Algoritmo
from grafo_ciudades import adyacentes, lista_ciudades

ciudad_origen = 0
ciudades_mapa = Algoritmo(adyacentes)

if ciudades_mapa.bellman_ford(ciudad_origen):
    print("Distancias más cortas desde la ciudad origen:")
    for v in range(1, ciudades_mapa.num_vertices, 1):
        print(
            f"Ciudad {lista_ciudades[v]}: Distancia = {ciudades_mapa.distancia[v]}, Predecesor = {lista_ciudades[ciudades_mapa.predecesor[v]]} ")
