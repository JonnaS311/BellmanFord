class Algoritmo:
    def __init__(self, matriz_adyacencia):
        self.num_vertices = len(matriz_adyacencia)
        self.distancia = [float('inf')] * self.num_vertices
        self.predecesor = [None] * self.num_vertices
        self.matriz_adyacencia = matriz_adyacencia

    def bellman_ford(self, ciudad_origen):
        self.distancia[ciudad_origen] = 0

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if self.matriz_adyacencia[u][v] != 0 and self.distancia[v] > self.distancia[u] + \
                            self.matriz_adyacencia[u][v]:
                        self.distancia[v] = self.distancia[u] + self.matriz_adyacencia[u][v]
                        self.predecesor[v] = u

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.matriz_adyacencia[u][v] != 0 and self.distancia[v] > self.distancia[u] + \
                        self.matriz_adyacencia[u][v]:
                    print("Hay ciclo negativo")
                    return False

        return True


