"""
Estructura de datos: Grafo
Implementación de un grafo no dirigido para gestionar las relaciones
entre libros, usuarios, préstamos y lista de espera.
"""

class Grafo:
    """
    Clase que representa un grafo no dirigido.
    Los nodos pueden representar libros, usuarios, géneros, autores, etc.
    Las aristas representan relaciones entre ellos.
    """
    
    def __init__(self):
        """Inicializa un grafo vacío"""
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        """
        Agrega un nodo al grafo
        
        Args:
            nodo: Identificador único del nodo
        """
        if nodo not in self.grafo:
            self.grafo[nodo] = []
    
    def agregar_arista(self, a, b, peso=1):
        """
        Agrega una arista entre dos nodos (no dirigida)
        
        Args:
            a: Primer nodo
            b: Segundo nodo
            peso: Peso de la arista (opcional)
        """
        if a not in self.grafo:
            self.grafo[a] = []
        if b not in self.grafo:
            self.grafo[b] = []
        
        # Verificar si la arista ya existe
        if b not in [vecino[0] if isinstance(vecino, tuple) else vecino 
                     for vecino in self.grafo[a]]:
            self.grafo[a].append((b, peso) if peso != 1 else b)
        
        if a not in [vecino[0] if isinstance(vecino, tuple) else vecino 
                     for vecino in self.grafo[b]]:
            self.grafo[b].append((a, peso) if peso != 1 else a)
    
    def eliminar_nodo(self, nodo):
        """
        Elimina un nodo del grafo y todas sus aristas
        
        Args:
            nodo: Nodo a eliminar
        """
        if nodo in self.grafo:
            # Eliminar todas las aristas que apunten a este nodo
            for vecino in self.grafo[nodo]:
                vecino_id = vecino[0] if isinstance(vecino, tuple) else vecino
                if vecino_id in self.grafo:
                    self.grafo[vecino_id] = [
                        v for v in self.grafo[vecino_id] 
                        if (v[0] if isinstance(v, tuple) else v) != nodo
                    ]
            # Eliminar el nodo
            del self.grafo[nodo]
    
    def eliminar_arista(self, a, b):
        """
        Elimina la arista entre dos nodos
        
        Args:
            a: Primer nodo
            b: Segundo nodo
        """
        if a in self.grafo:
            self.grafo[a] = [
                v for v in self.grafo[a] 
                if (v[0] if isinstance(v, tuple) else v) != b
            ]
        
        if b in self.grafo:
            self.grafo[b] = [
                v for v in self.grafo[b] 
                if (v[0] if isinstance(v, tuple) else v) != a
            ]
    
    def obtener_vecinos(self, nodo):
        """
        Obtiene todos los vecinos de un nodo
        
        Args:
            nodo: Nodo a consultar
            
        Returns:
            Lista de vecinos
        """
        if nodo in self.grafo:
            return [v[0] if isinstance(v, tuple) else v for v in self.grafo[nodo]]
        return []
    
    def existe_arista(self, a, b):
        """
        Verifica si existe una arista entre dos nodos
        
        Args:
            a: Primer nodo
            b: Segundo nodo
            
        Returns:
            True si existe la arista, False en caso contrario
        """
        if a in self.grafo:
            return any(
                (v[0] if isinstance(v, tuple) else v) == b 
                for v in self.grafo[a]
            )
        return False
    
    def obtener_nodos(self):
        """
        Obtiene todos los nodos del grafo
        
        Returns:
            Lista de nodos
        """
        return list(self.grafo.keys())
    
    def contar_nodos(self):
        """Retorna la cantidad de nodos en el grafo"""
        return len(self.grafo)
    
    def contar_aristas(self):
        """Retorna la cantidad de aristas en el grafo"""
        count = 0
        for nodo in self.grafo:
            count += len(self.grafo[nodo])
        return count // 2  # Dividir por 2 porque cada arista se cuenta dos veces
    
    def obtener_grado(self, nodo):
        """
        Obtiene el grado (número de aristas) de un nodo
        
        Args:
            nodo: Nodo a consultar
            
        Returns:
            Grado del nodo
        """
        if nodo in self.grafo:
            return len(self.grafo[nodo])
        return 0
    
    def buscar_camino_bfs(self, inicio, fin):
        """
        Busca un camino entre dos nodos usando BFS
        
        Args:
            inicio: Nodo de inicio
            fin: Nodo de destino
            
        Returns:
            Lista con el camino si existe, None en caso contrario
        """
        if inicio not in self.grafo or fin not in self.grafo:
            return None
        
        from collections import deque
        
        visitados = set()
        cola = deque([(inicio, [inicio])])
        visitados.add(inicio)
        
        while cola:
            nodo_actual, camino = cola.popleft()
            
            if nodo_actual == fin:
                return camino
            
            for vecino in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        
        return None
    
    def __repr__(self):
        """Representación string del grafo"""
        return f"Grafo(nodos={self.contar_nodos()}, aristas={self.contar_aristas()})"
