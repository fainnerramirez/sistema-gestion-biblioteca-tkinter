"""
Archivo de prueba para verificar que la migración a grafos funciona correctamente
"""

from modules.biblioteca import GestorBiblioteca

def test_biblioteca():
    """Prueba básica del sistema de biblioteca con grafos"""
    
    print("=" * 60)
    print("PRUEBA DEL SISTEMA DE BIBLIOTECA CON GRAFOS")
    print("=" * 60)
    
    # Crear gestor de biblioteca
    biblioteca = GestorBiblioteca()
    
    # Agregar libros
    print("\n1. AGREGANDO LIBROS...")
    id1 = biblioteca.agregar_libro("El Quijote", "Miguel de Cervantes", 5, "Novela clásica")
    id2 = biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", 3, "Realismo mágico")
    id3 = biblioteca.agregar_libro("1984", "George Orwell", 2, "Distopía")
    print(f"  ✓ Libro 1 ID: {id1}")
    print(f"  ✓ Libro 2 ID: {id2}")
    print(f"  ✓ Libro 3 ID: {id3}")
    
    # Obtener estadísticas
    print("\n2. ESTADÍSTICAS DEL GRAFO DE LIBROS:")
    stats = biblioteca.obtener_estadisticas()
    print(f"  - Total de libros: {stats['total_libros']}")
    print(f"  - Total de copias: {stats['total_copias']}")
    print(f"  - Nodos en grafo: {stats['nodos_libros']}")
    print(f"  - Aristas en grafo: {stats['aristas_libros']}")
    
    # Registrar préstamos
    print("\n3. REGISTRANDO PRÉSTAMOS...")
    prestamo1 = biblioteca.registrar_prestamo("usuario_juan", id1)
    prestamo2 = biblioteca.registrar_prestamo("usuario_maria", id2)
    print(f"  ✓ Préstamo 1 ID: {prestamo1}")
    print(f"  ✓ Préstamo 2 ID: {prestamo2}")
    
    # Verificar copias
    libro1 = biblioteca.obtener_libro(id1)
    print(f"  - Copias de '{libro1['title']}' después del préstamo: {libro1['copies']}")
    
    # Estadísticas de préstamos
    print("\n4. ESTADÍSTICAS DEL GRAFO DE PRÉSTAMOS:")
    stats = biblioteca.obtener_estadisticas()
    print(f"  - Préstamos activos: {stats['prestamos_activos']}")
    print(f"  - Nodos en grafo: {stats['nodos_prestamos']}")
    print(f"  - Aristas en grafo: {stats['aristas_prestamos']}")
    
    # Obtener préstamos activos
    print("\n5. PRÉSTAMOS ACTIVOS:")
    prestamos = biblioteca.obtener_prestamos()
    for i, p in enumerate(prestamos, 1):
        print(f"  {i}. {p['user']} - {p['title']} ({p['loan_date']})")
    
    # Agregar a lista de espera
    print("\n6. AGREGANDO A LISTA DE ESPERA...")
    espera1 = biblioteca.agregar_a_espera("usuario_carlos", id2)
    espera2 = biblioteca.agregar_a_espera("usuario_lucia", id1)
    print(f"  ✓ Entrada 1 ID: {espera1}")
    print(f"  ✓ Entrada 2 ID: {espera2}")
    
    # Estadísticas de espera
    print("\n7. ESTADÍSTICAS DEL GRAFO DE ESPERA:")
    stats = biblioteca.obtener_estadisticas()
    print(f"  - Usuarios en espera: {stats['lista_espera']}")
    print(f"  - Nodos en grafo: {stats['nodos_espera']}")
    print(f"  - Aristas en grafo: {stats['aristas_espera']}")
    
    # Devolver préstamo
    print("\n8. DEVOLVIENDO PRÉSTAMO...")
    biblioteca.devolver_prestamo(prestamo1)
    libro1_actualizado = biblioteca.obtener_libro(id1)
    print(f"  ✓ Préstamo devuelto")
    print(f"  - Copias de '{libro1_actualizado['title']}' después de devolución: {libro1_actualizado['copies']}")
    
    # Estadísticas finales
    print("\n9. ESTADÍSTICAS FINALES:")
    stats = biblioteca.obtener_estadisticas()
    print(f"  - Total de libros: {stats['total_libros']}")
    print(f"  - Préstamos activos: {stats['prestamos_activos']}")
    print(f"  - Usuarios en espera: {stats['lista_espera']}")
    
    # Búsqueda por autor
    print("\n10. BÚSQUEDA POR AUTOR:")
    libros_cervantes = biblioteca.buscar_libros_por_autor("Miguel de Cervantes")
    for libro in libros_cervantes:
        print(f"  - {libro['title']} por {libro['author']} ({libro['copies']} copias disponibles)")
    
    print("\n" + "=" * 60)
    print("PRUEBA COMPLETADA EXITOSAMENTE ✓")
    print("=" * 60)

if __name__ == "__main__":
    test_biblioteca()
