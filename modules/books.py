import uuid
import customtkinter as ctk
from tkinter import messagebox

class BooksScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, role="usuario", books=[]):
        super().__init__(parent)
        self.on_back = on_back
        self.role = role
        self.library_books = books
        self.book_widgets = {}  # Diccionario para guardar referencias a los widgets de cada libro
        
        # Título con el rol del usuario
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=10, fill="x", padx=20)
        
        title_label = ctk.CTkLabel(title_frame, text="Gestión de Libros", font=("Arial", 24, "bold"))
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
               
        for idx, book in enumerate(self.library_books):
            book_item_frame = ctk.CTkFrame(self.books_frame, fg_color="#1a1a1a", corner_radius=5)
            book_item_frame.pack(pady=8, padx=10, fill="x")
            
            book_label = ctk.CTkLabel(book_item_frame, text=f"{book['title']} - {book['author']}", font=("Arial", 11))
            book_label.pack(side="left", padx=10, pady=10)
            
            copies_label = ctk.CTkLabel(book_item_frame, text=f"{book['copies']} copias", font=("Arial", 11, "bold"), text_color="#aaaaaa")
            copies_label.pack(side="right", padx=10, pady=10)
            
            self.book_widgets[book['id']] = {
                'book_label': book_label,
                'copies_label': copies_label,
                'frame': book_item_frame
            }
            
            # Botones según el rol
            if self.role == "admin":
                edit_btn = ctk.CTkButton(book_item_frame, text="Editar", width=70, fg_color="#2b5f7f", hover_color="#1e4660", command=lambda b=book: self.edit_book(b))
                edit_btn.pack(side="right", padx=5, pady=10)
                
                delete_btn = ctk.CTkButton(book_item_frame, text="Eliminar", width=70, fg_color="#7f2b2b", hover_color="#601a1a", command=lambda b=book: self.delete_book(b))
                delete_btn.pack(side="right", padx=5, pady=10)
            else:
                loan_btn = ctk.CTkButton(book_item_frame, text="Prestar", width=70, fg_color="#2b5f2b", hover_color="#1e4620", command=lambda b=book: self.loan_book(b))
                loan_btn.pack(side="right", padx=5, pady=10)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)
        
    def create_book(self):
        """Abre un formulario para crear un nuevo libro"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Crear Nuevo Libro")
        dialog.geometry("400x500")
        dialog.resizable(False, False)
        dialog.grab_set()  # Modal
        
        # Centrar ventana
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
            """Guarda los datos del libro y cierra la ventana"""
            datos = {
                'titulo': fields['titulo'].get(),
                'autor': fields['autor'].get(),
                'cantidad': fields['cantidad'].get(),
                'descripcion': fields['descripcion'].get("1.0", "end-1c")
            }
            
            if not datos['titulo'] or not datos['autor']:
                messagebox.showerror("Error", "Título y Autor son requeridos")
                return
            
            # Crear el nuevo libro
            nuevo_libro = {
                'id': uuid.uuid4(),
                'title': datos['titulo'],
                'author': datos['autor'],
                'copies': int(datos['cantidad']) if datos['cantidad'].isdigit() else 0,
                'description': datos['descripcion']
            }
            
            self.library_books.append(nuevo_libro)
            self.add_book_widget(nuevo_libro)
            dialog.destroy()
            messagebox.showinfo("Éxito", f"'{nuevo_libro['title']}' ha sido agregado")
        
        # Botón Guardar
        save_btn = ctk.CTkButton(button_frame, text="Guardar", fg_color="#2b5f2b", 
                                 hover_color="#1e4620", command=guardar_libro)
        save_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón Cancelar
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def refresh_book_widget(self, book_id):
        """Actualiza los widgets visuales de un libro específico"""
        if book_id in self.book_widgets:
            updated_book = next((b for b in self.library_books if b['id'] == book_id), None)
            if updated_book:
                self.book_widgets[book_id]['book_label'].configure(
                    text=f"{updated_book['title']} - {updated_book['author']}"
                )
                self.book_widgets[book_id]['copies_label'].configure(
                    text=f"{updated_book['copies']} copias"
                )
    
    def remove_book_widget(self, book_id):
        """Elimina el widget visual de un libro"""
        if book_id in self.book_widgets:
            self.book_widgets[book_id]['frame'].destroy()
            del self.book_widgets[book_id]
    
    def add_book_widget(self, book):
        """Agrega un nuevo widget de libro a la tabla"""
        book_item_frame = ctk.CTkFrame(self.books_frame, fg_color="#1a1a1a", corner_radius=5)
        book_item_frame.pack(pady=8, padx=10, fill="x")
        
        book_label = ctk.CTkLabel(book_item_frame, text=f"{book['title']} - {book['author']}", font=("Arial", 11))
        book_label.pack(side="left", padx=10, pady=10)
        
        copies_label = ctk.CTkLabel(book_item_frame, text=f"{book['copies']} copias", font=("Arial", 11, "bold"), text_color="#aaaaaa")
        copies_label.pack(side="right", padx=10, pady=10)
        
        self.book_widgets[book['id']] = {
            'book_label': book_label,
            'copies_label': copies_label,
            'frame': book_item_frame
        }
        
        # Botones según el rol
        if self.role == "admin":
            edit_btn = ctk.CTkButton(book_item_frame, text="Editar", width=70, fg_color="#2b5f7f", hover_color="#1e4660", command=lambda b=book: self.edit_book(b))
            edit_btn.pack(side="right", padx=5, pady=10)
            
            delete_btn = ctk.CTkButton(book_item_frame, text="Eliminar", width=70, fg_color="#7f2b2b", hover_color="#601a1a", command=lambda b=book: self.delete_book(b))
            delete_btn.pack(side="right", padx=5, pady=10)
        else:
            loan_btn = ctk.CTkButton(book_item_frame, text="Prestar", width=70, fg_color="#2b5f2b", hover_color="#1e4620", command=lambda b=book: self.loan_book(b))
            loan_btn.pack(side="right", padx=5, pady=10)
        
    def edit_book(self, book):
        print(f"Admin: Editar libro - {book}")
        dialog_edit_book = ctk.CTkToplevel(self)
        dialog_edit_book.title("Editar Libro")
        dialog_edit_book.geometry("400x500")
        dialog_edit_book.resizable(False, False)
        dialog_edit_book.grab_set()  # Modal
        dialog_edit_book.transient(self.master)
        title_label = ctk.CTkLabel(dialog_edit_book, text="Editar los datos del libro", font=("Arial", 14, "bold"))
        title_label.pack(pady=15)
        
        # Frame para campos
        form_frame = ctk.CTkFrame(dialog_edit_book, fg_color="transparent")
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        #title
        ctk.CTkLabel(form_frame, text="Título:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        title_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej: El Quijote")
        title_entry.insert(0, book['title'])
        title_entry.pack(fill="x", pady=(0, 10))
        
        #author
        ctk.CTkLabel(form_frame, text="Autor:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        author_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej: Miguel de Cervantes")
        author_entry.insert(0, book['author'])
        author_entry.pack(fill="x", pady=(0, 10))
        
        #cantidad
        ctk.CTkLabel(form_frame, text="Cantidad de copias:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        quantity_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej: 5")
        quantity_entry.insert(0, book['copies'])
        quantity_entry.pack(fill="x", pady=(0, 10))
        
        #descripción
        ctk.CTkLabel(form_frame, text="Descripción:", font=("Arial", 11)).pack(anchor="w", pady=(10, 0))
        description_text = ctk.CTkTextbox(form_frame, height=80, corner_radius=5)
        description_text.insert("1.0", book['description'] if 'description' in book else "")
        description_text.pack(fill="both", expand=True, pady=(0, 10))
        
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog_edit_book, fg_color="transparent")
        button_frame.pack(pady=15, fill="x", padx=20)
        
        # Botón Guardar
        def guardar_cambios():
            updated_data = {
                'id': book['id'],  # Preservar el ID
                'title': title_entry.get(),
                'author': author_entry.get(),
                'copies': quantity_entry.get(),
                'description': description_text.get("1.0", "end-1c")
            }
            print("Libro actualizado:", updated_data)
            # Actualizar en la lista de libros
            self.library_books = [updated_data if b['id'] == book['id'] else b for b in self.library_books]
            # Actualizar solo el widget afectado
            self.refresh_book_widget(book['id'])
            dialog_edit_book.destroy()
            messagebox.showinfo("Éxito", "Libro actualizado correctamente")
        
        save_btn = ctk.CTkButton(button_frame, text="Guardar Cambios", fg_color="#2b5f7f", 
                                 hover_color="#1e4660", command=guardar_cambios)
        save_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón Cancelar
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog_edit_book.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
            
    def delete_book(self, book):
        print(f"Admin: Eliminar libro - {book}")
        dialog_delete_book = ctk.CTkToplevel(self)
        dialog_delete_book.title("Eliminar Libro")
        dialog_delete_book.geometry("300x150")
        dialog_delete_book.resizable(False, False)
        dialog_delete_book.grab_set()  # Modal
        # Centrar ventana
        dialog_delete_book.transient(self.master)
        # Mensaje de confirmación
        message_label = ctk.CTkLabel(dialog_delete_book, text=f"Seguro que desea eliminar '{book['title']}'?", font=("Arial", 12), wraplength=280)
        message_label.pack(pady=20, padx=10)
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog_delete_book, fg_color="transparent")
        button_frame.pack(pady=10, fill="x", padx=20)
        
        # Botón Confirmar
        def confirmar_eliminacion():
            book_id = book['id']
            self.library_books = [b for b in self.library_books if b['id'] != book_id]
            self.remove_book_widget(book_id)
            dialog_delete_book.destroy()
            messagebox.showinfo("Eliminado", f"'{book['title']}' ha sido eliminado")

        confirm_btn = ctk.CTkButton(button_frame, text="Eliminar", fg_color="#7f2b2b", 
                                    hover_color="#601a1a", command=confirmar_eliminacion)
        confirm_btn.pack(side="left", padx=5, fill="x", expand=True)
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog_delete_book.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def search_books(self):
        """Filtra los libros según el texto de búsqueda"""
        search_text = self.search_entry.get().lower().strip()
        
        # Si la búsqueda está vacía, mostrar todos los libros
        if not search_text:
            for book_id, widgets in self.book_widgets.items():
                widgets['frame'].pack(pady=8, padx=10, fill="x")
            return
        
        # Filtrar y mostrar/ocultar libros
        for book_id, widgets in self.book_widgets.items():
            # Buscar el libro para obtener su título y autor
            book = next((b for b in self.library_books if b['id'] == book_id), None)
            if book:
                # Verificar si el texto coincide con título o autor (insensible a mayúsculas)
                title_match = search_text in book['title'].lower()
                author_match = search_text in book['author'].lower()
                
                if title_match or author_match:
                    # Mostrar el libro
                    widgets['frame'].pack(pady=8, padx=10, fill="x")
                else:
                    # Ocultar el libro
                    widgets['frame'].pack_forget()
    
    def loan_book(self, book):
        print(f"Usuario: Prestar libro - {book}")

