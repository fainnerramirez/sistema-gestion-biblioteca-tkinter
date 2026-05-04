import customtkinter as ctk
from tkinter import messagebox

class BooksScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, role="usuario", biblioteca=None):
        super().__init__(parent)
        self.on_back = on_back
        self.role = role
        self.biblioteca = biblioteca
        self.parent = parent  
        self.book_widgets = {}  
        
        # Título con el rol del usuario
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=10, fill="x", padx=20)
        
        title_label = ctk.CTkLabel(title_frame, text="Gestión de Libros (Sistema de Grafos)", font=("Arial", 24, "bold"))
        title_label.pack(side="left")
        
        role_label = ctk.CTkLabel(title_frame, text=f"Rol: {role.upper()}", font=("Arial", 12), text_color="#888888")
        role_label.pack(side="right")
        
        # Frame para búsqueda
        search_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        search_frame.pack(padx=20, pady=10, fill="x")
        
        search_label = ctk.CTkLabel(search_frame, text="Buscar libro:", font=("Arial", 12))
        search_label.pack(side="left", padx=10, pady=10)
        
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Ingresa título o autor...")
        self.search_entry.pack(side="left", padx=5, pady=10, fill="x", expand=True)
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_books())
        
        search_button = ctk.CTkButton(search_frame, text="Buscar", command=self.search_books)
        search_button.pack(side="left", padx=5, pady=10)
        
        # Mostrar botón "Crear Libro" solo si es admin
        if self.role == "admin":
            create_button = ctk.CTkButton(search_frame, text="+ Crear Libro", fg_color="#2b5f2b", hover_color="#1e4620", command=self.create_book)
            create_button.pack(side="left", padx=5, pady=10)
        
        # Frame para lista de libros
        self.books_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.books_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        books_title = ctk.CTkLabel(self.books_frame, text="Libros Disponibles", font=("Arial", 14, "bold"))
        books_title.pack(pady=10)
        
        # Cargar y mostrar los libros
        self.actualizar_lista_libros()
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)
    
    def actualizar_lista_libros(self):
        """Actualiza la lista de libros mostrada en la UI"""
        # Limpiar widgets anteriores
        for widget_info in self.book_widgets.values():
            widget_info['frame'].destroy()
        self.book_widgets.clear()
        
        # Obtener libros del grafo
        libros = self.biblioteca.obtener_libros()
        
        for libro in libros:
            self.agregar_widget_libro(libro)
    
    def agregar_widget_libro(self, libro):
        """Agrega un widget visual para un libro"""
        book_item_frame = ctk.CTkFrame(self.books_frame, fg_color="#1a1a1a", corner_radius=5)
        book_item_frame.pack(pady=8, padx=10, fill="x")
        
        book_label = ctk.CTkLabel(book_item_frame, text=f"{libro['title']} - {libro['author']}", font=("Arial", 11))
        book_label.pack(side="left", padx=10, pady=10)
        
        copies_label = ctk.CTkLabel(book_item_frame, text=f"{libro['copies']} copias", font=("Arial", 11, "bold"), text_color="#aaaaaa")
        copies_label.pack(side="right", padx=10, pady=10)
        
        self.book_widgets[libro['id']] = {
            'book_label': book_label,
            'copies_label': copies_label,
            'frame': book_item_frame
        }
        
        # Botones según el rol
        if self.role == "admin":
            edit_btn = ctk.CTkButton(book_item_frame, text="Editar", width=70, fg_color="#2b5f7f", hover_color="#1e4660", 
                                     command=lambda b=libro: self.edit_book(b))
            edit_btn.pack(side="right", padx=5, pady=10)
            
            delete_btn = ctk.CTkButton(book_item_frame, text="Eliminar", width=70, fg_color="#7f2b2b", hover_color="#601a1a", 
                                       command=lambda b=libro: self.delete_book(b))
            delete_btn.pack(side="right", padx=5, pady=10)
        else:
            loan_btn = ctk.CTkButton(book_item_frame, text="Prestar", width=70, fg_color="#2b5f2b", hover_color="#1e4620", 
                                     command=lambda b=libro: self.loan_book(b))
            loan_btn.pack(side="right", padx=5, pady=10)
    
    def search_books(self):
        """Busca libros por título o autor"""
        if not self.biblioteca:
            return
        
        search_text = self.search_entry.get().lower()
        
        if not search_text:
            self.actualizar_lista_libros()
            return
        
        # Obtener todos los libros
        libros = self.biblioteca.obtener_libros()
        
        # Limpiar widgets anteriores
        for widget_info in self.book_widgets.values():
            widget_info['frame'].destroy()
        self.book_widgets.clear()
        
        # Filtrar y mostrar
        for libro in libros:
            if search_text in libro['title'].lower() or search_text in libro['author'].lower():
                self.agregar_widget_libro(libro)
    
    def create_book(self):
        """Abre un formulario para crear un nuevo libro"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Crear Nuevo Libro")
        dialog.geometry("400x500")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.transient(self.master)
        
        # Título del formulario
        title_label = ctk.CTkLabel(dialog, text="Ingrese los datos del libro", font=("Arial", 14, "bold"))
        title_label.pack(pady=15)
        
        # Frame para campos
        form_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Campos del formulario
        fields = {}
        
        # Título
        ctk.CTkLabel(form_frame, text="Título:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        fields['titulo'] = ctk.CTkEntry(form_frame, placeholder_text="Ej: El Quijote")
        fields['titulo'].pack(fill="x", pady=(0, 10))
        
        # Autor
        ctk.CTkLabel(form_frame, text="Autor:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        fields['autor'] = ctk.CTkEntry(form_frame, placeholder_text="Ej: Miguel de Cervantes")
        fields['autor'].pack(fill="x", pady=(0, 10))
                
        # Cantidad de copias
        ctk.CTkLabel(form_frame, text="Cantidad de copias:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        fields['cantidad'] = ctk.CTkEntry(form_frame, placeholder_text="Ej: 5")
        fields['cantidad'].pack(fill="x", pady=(0, 10))
        
        # Descripción
        ctk.CTkLabel(form_frame, text="Descripción:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        fields['descripcion'] = ctk.CTkTextbox(form_frame, height=80, corner_radius=5)
        fields['descripcion'].pack(fill="both", expand=True, pady=(0, 10))
        
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=15, fill="x", padx=20)
        
        def guardar_libro():
            """Guarda los datos del libro usando el grafo"""
            titulo = fields['titulo'].get()
            autor = fields['autor'].get()
            cantidad_str = fields['cantidad'].get()
            descripcion = fields['descripcion'].get("1.0", "end-1c")
            
            if not titulo or not autor:
                messagebox.showerror("Error", "Título y Autor son requeridos")
                return
            
            if not cantidad_str.isdigit() or int(cantidad_str) < 0:
                messagebox.showerror("Error", "Cantidad debe ser un número válido")
                return
            
            # Agregar libro usando el grafo
            id_libro = self.biblioteca.agregar_libro(titulo, autor, int(cantidad_str), descripcion)
            
            # Actualizar UI
            self.actualizar_lista_libros()
            dialog.destroy()
            messagebox.showinfo("Éxito", f"'{titulo}' ha sido agregado al sistema")
        
        # Botón Guardar
        save_btn = ctk.CTkButton(button_frame, text="Guardar", fg_color="#2b5f2b", 
                                 hover_color="#1e4620", command=guardar_libro)
        save_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón Cancelar
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def edit_book(self, libro):
        """Abre un formulario para editar un libro"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Editar Libro")
        dialog.geometry("400x500")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.transient(self.master)
        
        title_label = ctk.CTkLabel(dialog, text="Editar los datos del libro", font=("Arial", 14, "bold"))
        title_label.pack(pady=15)
        
        # Frame para campos
        form_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Título
        ctk.CTkLabel(form_frame, text="Título:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        title_entry = ctk.CTkEntry(form_frame)
        title_entry.insert(0, libro['title'])
        title_entry.pack(fill="x", pady=(0, 10))
        
        # Autor
        ctk.CTkLabel(form_frame, text="Autor:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        author_entry = ctk.CTkEntry(form_frame)
        author_entry.insert(0, libro['author'])
        author_entry.pack(fill="x", pady=(0, 10))
        
        # Cantidad
        ctk.CTkLabel(form_frame, text="Cantidad de copias:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        quantity_entry = ctk.CTkEntry(form_frame)
        quantity_entry.insert(0, str(libro['copies']))
        quantity_entry.pack(fill="x", pady=(0, 10))
        
        # Descripción
        ctk.CTkLabel(form_frame, text="Descripción:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        description_text = ctk.CTkTextbox(form_frame, height=80, corner_radius=5)
        description_text.insert("1.0", libro.get('description', ''))
        description_text.pack(fill="both", expand=True, pady=(0, 10))
        
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=15, fill="x", padx=20)
        
        def guardar_cambios():
            """Guarda los cambios del libro"""
            titulo = title_entry.get()
            autor = author_entry.get()
            cantidad_str = quantity_entry.get()
            descripcion = description_text.get("1.0", "end-1c")
            
            if not titulo or not autor:
                messagebox.showerror("Error", "Título y Autor son requeridos")
                return
            
            if not cantidad_str.isdigit() or int(cantidad_str) < 0:
                messagebox.showerror("Error", "Cantidad debe ser un número válido")
                return
            
            # Actualizar en el grafo
            self.biblioteca.actualizar_libro(libro['id'], titulo, autor, int(cantidad_str), descripcion)
            
            # Actualizar UI
            self.actualizar_lista_libros()
            dialog.destroy()
            messagebox.showinfo("Éxito", "Libro actualizado correctamente")
        
        save_btn = ctk.CTkButton(button_frame, text="Guardar Cambios", fg_color="#2b5f7f", 
                                 hover_color="#1e4660", command=guardar_cambios)
        save_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def delete_book(self, libro):
        """Elimina un libro del sistema"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Eliminar Libro")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.transient(self.master)
        
        # Mensaje de confirmación
        message_label = ctk.CTkLabel(dialog, text=f"¿Seguro que desea eliminar '{libro['title']}'?", 
                                     font=("Arial", 12), wraplength=280)
        message_label.pack(pady=20, padx=10)
        
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=10, fill="x", padx=20)
        
        def confirmar_eliminacion():
            # Eliminar del grafo
            self.biblioteca.eliminar_libro(libro['id'])
            
            # Actualizar UI
            self.actualizar_lista_libros()
            dialog.destroy()
            messagebox.showinfo("Éxito", f"'{libro['title']}' ha sido eliminado del sistema")
        
        # Botón Confirmar
        confirm_btn = ctk.CTkButton(button_frame, text="Confirmar", fg_color="#7f2b2b", 
                                    hover_color="#601a1a", command=confirmar_eliminacion)
        confirm_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón Cancelar
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#2b5f7f", 
                                   hover_color="#1e4660", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def loan_book(self, libro):
        """Registra un préstamo de un libro"""
        if libro['copies'] <= 0:
            messagebox.showerror("Error", "Este libro no tiene copias disponibles")
            return
        
        # Crear un diálogo para obtener el ID del usuario
        dialog = ctk.CTkToplevel(self)
        dialog.title("Registrar Préstamo")
        dialog.geometry("350x150")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.transient(self.master)
        
        label = ctk.CTkLabel(dialog, text="Ingrese su ID de usuario:", font=("Arial", 12))
        label.pack(pady=10, padx=20)
        
        user_entry = ctk.CTkEntry(dialog, placeholder_text="ID Usuario")
        user_entry.pack(pady=10, padx=20, fill="x")
        
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=10, fill="x", padx=20)
        
        def procesar_prestamo():
            id_usuario = user_entry.get()
            if not id_usuario:
                messagebox.showerror("Error", "Debe ingresar un ID de usuario")
                return
            
            # Registrar el préstamo en el grafo
            id_prestamo = self.biblioteca.registrar_prestamo(id_usuario, libro['id'])
            
            if id_prestamo:
                # Actualizar UI
                self.actualizar_lista_libros()
                dialog.destroy()
                messagebox.showinfo("Éxito", f"Préstamo registrado exitosamente\nID Préstamo: {id_prestamo}")
            else:
                messagebox.showerror("Error", "No se pudo registrar el préstamo")
        
        confirm_btn = ctk.CTkButton(button_frame, text="Confirmar", fg_color="#2b5f2b", 
                                    hover_color="#1e4620", command=procesar_prestamo)
        confirm_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
