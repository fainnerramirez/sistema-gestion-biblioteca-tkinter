"""
Gestión de la Biblioteca usando Grafos
Estructura basada en grafos para manejar libros, usuarios, préstamos y lista de espera
"""

import uuid
from modules.grafo import Grafo
from datetime import datetime

class GestorBiblioteca:
    """
    Gestor de biblioteca que utiliza grafos para manejar las relaciones
    entre libros, usuarios, préstamos y lista de espera
    """
    
    def __init__(self):
        """Inicializa la estructura de datos del gestor"""
        # Grafo de libros: conecta libros con autores y géneros
        self.grafo_libros = Grafo()
        
        # Grafo de préstamos: conecta usuarios con libros prestados
        self.grafo_prestamos = Grafo()
        
        # Grafo de lista de espera: conecta usuarios que esperan libros
        self.grafo_espera = Grafo()
        
        # Diccionarios para almacenar los datos de los nodos
        self.libros = {}  # {id_libro: {datos}}
        self.usuarios = {}  # {id_usuario: {datos}}
        self.prestamos_activos = {}  # {id_prestamo: {datos}}
        self.lista_espera = {}  # {id_espera: {datos}}
    
    # ===================== GESTIÓN DE LIBROS =====================
    
    def agregar_libro(self, titulo, autor, copias, descripcion=""):
        """
        Agrega un nuevo libro al sistema
        
        Args:
            titulo: Título del libro
            autor: Autor del libro
            copias: Número de copias disponibles
            descripcion: Descripción del libro
            
        Returns:
            ID del libro creado
        """
        id_libro = str(uuid.uuid4())
        
        # Crear nodo de libro
        self.grafo_libros.agregar_nodo(id_libro)
        
        # Crear nodo del autor si no existe
        id_autor = f"autor_{autor.lower().replace(' ', '_')}"
        self.grafo_libros.agregar_nodo(id_autor)
        
        # Conectar libro con autor
        self.grafo_libros.agregar_arista(id_libro, id_autor)
        
        # Almacenar datos del libro
        self.libros[id_libro] = {
            'id': id_libro,
            'title': titulo,
            'author': autor,
            'copies': copias,
            'description': descripcion,
            'created_at': datetime.now()
        }
        
        return id_libro
    
    def obtener_libros(self):
        """
        Obtiene todos los libros del sistema
        
        Returns:
            Lista de libros
        """
        return list(self.libros.values())
    
    def obtener_libro(self, id_libro):
        """
        Obtiene un libro específico
        
        Args:
            id_libro: ID del libro
            
        Returns:
            Datos del libro
        """
        return self.libros.get(id_libro)
    
    def actualizar_libro(self, id_libro, titulo=None, autor=None, copias=None, descripcion=None):
        """
        Actualiza un libro existente
        
        Args:
            id_libro: ID del libro
            titulo: Nuevo título (opcional)
            autor: Nuevo autor (opcional)
            copias: Nuevo número de copias (opcional)
            descripcion: Nueva descripción (opcional)
            
        Returns:
            True si se actualizó, False en caso contrario
        """
        if id_libro not in self.libros:
            return False
        
        if titulo:
            self.libros[id_libro]['title'] = titulo
        if autor:
            self.libros[id_libro]['author'] = autor
        if copias is not None:
            self.libros[id_libro]['copies'] = copias
        if descripcion:
            self.libros[id_libro]['description'] = descripcion
        
        return True
    
    def eliminar_libro(self, id_libro):
        """
        Elimina un libro del sistema
        
        Args:
            id_libro: ID del libro
            
        Returns:
            True si se eliminó, False en caso contrario
        """
        if id_libro in self.libros:
            # Eliminar el nodo del grafo
            self.grafo_libros.eliminar_nodo(id_libro)
            # Eliminar el libro
            del self.libros[id_libro]
            return True
        return False
    
    def buscar_libros_por_autor(self, autor):
        """
        Busca todos los libros de un autor
        
        Args:
            autor: Nombre del autor
            
        Returns:
            Lista de libros del autor
        """
        id_autor = f"autor_{autor.lower().replace(' ', '_')}"
        libros_del_autor = []
        
        # Obtener todos los vecinos del nodo de autor
        vecinos = self.grafo_libros.obtener_vecinos(id_autor)
        
        for vecino in vecinos:
            if vecino in self.libros:
                libros_del_autor.append(self.libros[vecino])
        
        return libros_del_autor
    
    # ===================== GESTIÓN DE PRÉSTAMOS =====================
    
    def registrar_prestamo(self, id_usuario, id_libro):
        """
        Registra un nuevo préstamo
        
        Args:
            id_usuario: ID del usuario
            id_libro: ID del libro
            
        Returns:
            ID del préstamo si es exitoso, None en caso contrario
        """
        libro = self.libros.get(id_libro)
        if not libro or libro['copies'] <= 0:
            return None
        
        # Crear ID de préstamo
        id_prestamo = str(uuid.uuid4())
        
        # Agregar nodos si no existen
        self.grafo_prestamos.agregar_nodo(f"usuario_{id_usuario}")
        self.grafo_prestamos.agregar_nodo(f"libro_{id_libro}")
        
        # Conectar usuario con libro en el grafo de préstamos
        self.grafo_prestamos.agregar_arista(f"usuario_{id_usuario}", f"libro_{id_libro}")
        
        # Actualizar copias disponibles
        self.libros[id_libro]['copies'] -= 1
        
        # Registrar el préstamo
        self.prestamos_activos[id_prestamo] = {
            'id': id_prestamo,
            'user': id_usuario,
            'book_id': id_libro,
            'title': libro['title'],
            'author': libro['author'],
            'loan_date': datetime.now().strftime("%Y-%m-%d"),
            'status': 'activo'
        }
        
        return id_prestamo
    
    def obtener_prestamos(self):
        """
        Obtiene todos los préstamos activos
        
        Returns:
            Lista de préstamos
        """
        return [p for p in self.prestamos_activos.values() if p['status'] == 'activo']
    
    def obtener_prestamos_usuario(self, id_usuario):
        """
        Obtiene todos los préstamos de un usuario
        
        Args:
            id_usuario: ID del usuario
            
        Returns:
            Lista de préstamos del usuario
        """
        nodo_usuario = f"usuario_{id_usuario}"
        vecinos = self.grafo_prestamos.obtener_vecinos(nodo_usuario)
        
        prestamos_user = []
        for prestamo in self.prestamos_activos.values():
            if prestamo['user'] == id_usuario and prestamo['status'] == 'activo':
                prestamos_user.append(prestamo)
        
        return prestamos_user
    
    def devolver_prestamo(self, id_prestamo):
        """
        Registra la devolución de un préstamo
        
        Args:
            id_prestamo: ID del préstamo
            
        Returns:
            True si se devolvió, False en caso contrario
        """
        if id_prestamo not in self.prestamos_activos:
            return False
        
        prestamo = self.prestamos_activos[id_prestamo]
        id_libro = prestamo['book_id']
        id_usuario = prestamo['user']
        
        # Actualizar copias disponibles
        if id_libro in self.libros:
            self.libros[id_libro]['copies'] += 1
        
        # Eliminar la arista entre usuario y libro
        self.grafo_prestamos.eliminar_arista(f"usuario_{id_usuario}", f"libro_{id_libro}")
        
        # Marcar como inactivo
        prestamo['status'] = 'devuelto'
        
        return True
    
    # ===================== GESTIÓN DE LISTA DE ESPERA =====================
    
    def agregar_a_espera(self, id_usuario, id_libro):
        """
        Agrega un usuario a la lista de espera de un libro
        
        Args:
            id_usuario: ID del usuario
            id_libro: ID del libro
            
        Returns:
            ID de la entrada en la lista de espera
        """
        id_espera = str(uuid.uuid4())
        
        # Agregar nodos si no existen
        self.grafo_espera.agregar_nodo(f"usuario_{id_usuario}")
        self.grafo_espera.agregar_nodo(f"libro_{id_libro}")
        
        # Conectar usuario con libro en el grafo de espera
        self.grafo_espera.agregar_arista(f"usuario_{id_usuario}", f"libro_{id_libro}")
        
        libro = self.libros.get(id_libro)
        
        # Registrar en lista de espera
        self.lista_espera[id_espera] = {
            'id': id_espera,
            'user': id_usuario,
            'book_id': id_libro,
            'title': libro['title'] if libro else 'Desconocido',
            'added_date': datetime.now().strftime("%Y-%m-%d"),
            'status': 'esperando'
        }
        
        return id_espera
    
    def obtener_lista_espera(self):
        """
        Obtiene toda la lista de espera
        
        Returns:
            Lista de entradas en espera
        """
        return [e for e in self.lista_espera.values() if e['status'] == 'esperando']
    
    def obtener_espera_libro(self, id_libro):
        """
        Obtiene todos los usuarios esperando un libro específico
        
        Args:
            id_libro: ID del libro
            
        Returns:
            Lista de usuarios en espera
        """
        nodo_libro = f"libro_{id_libro}"
        vecinos = self.grafo_espera.obtener_vecinos(nodo_libro)
        
        usuarios_esperando = []
        for entrada in self.lista_espera.values():
            if entrada['book_id'] == id_libro and entrada['status'] == 'esperando':
                usuarios_esperando.append(entrada)
        
        return usuarios_esperando
    
    def eliminar_de_espera(self, id_espera):
        """
        Elimina una entrada de la lista de espera
        
        Args:
            id_espera: ID de la entrada
            
        Returns:
            True si se eliminó, False en caso contrario
        """
        if id_espera in self.lista_espera:
            self.lista_espera[id_espera]['status'] = 'procesado'
            return True
        return False
    
    # ===================== ESTADÍSTICAS =====================
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas generales de la biblioteca
        
        Returns:
            Diccionario con estadísticas
        """
        return {
            'total_libros': len(self.libros),
            'total_copias': sum(libro['copies'] for libro in self.libros.values()),
            'prestamos_activos': len([p for p in self.prestamos_activos.values() if p['status'] == 'activo']),
            'lista_espera': len(self.obtener_lista_espera()),
            'nodos_libros': self.grafo_libros.contar_nodos(),
            'aristas_libros': self.grafo_libros.contar_aristas(),
            'nodos_prestamos': self.grafo_prestamos.contar_nodos(),
            'aristas_prestamos': self.grafo_prestamos.contar_aristas(),
            'nodos_espera': self.grafo_espera.contar_nodos(),
            'aristas_espera': self.grafo_espera.contar_aristas()
        }
