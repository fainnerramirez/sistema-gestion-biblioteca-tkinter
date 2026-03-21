import customtkinter as ctk

class BooksScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, role="usuario"):
        super().__init__(parent)
        self.on_back = on_back
        self.role = role
        
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
        
        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Ingresa título o autor...")
        search_entry.pack(side="left", padx=5, pady=10, fill="x", expand=True)
        
        search_button = ctk.CTkButton(search_frame, text="Buscar")
        search_button.pack(side="left", padx=5, pady=10)
        
        # Mostrar botón "Crear Libro" solo si es admin
        if self.role == "admin":
            create_button = ctk.CTkButton(search_frame, text="+ Crear Libro", fg_color="#2b5f2b", hover_color="#1e4620", command=self.create_book)
            create_button.pack(side="left", padx=5, pady=10)
        
        # Frame para lista de libros
        books_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        books_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        books_title = ctk.CTkLabel(books_frame, text="Libros Disponibles", font=("Arial", 14, "bold"))
        books_title.pack(pady=10)
        
        # Aquí iría una tabla con libros (simulado por ahora)
        sample_books = [
            ("1. El Quijote - Miguel de Cervantes", "5 copias"),
            ("2. Cien Años de Soledad - Gabriel García Márquez", "3 copias"),
            ("3. 1984 - George Orwell", "2 copias")
        ]
        
        for idx, (book, copies) in enumerate(sample_books):
            book_item_frame = ctk.CTkFrame(books_frame, fg_color="#1a1a1a", corner_radius=5)
            book_item_frame.pack(pady=8, padx=10, fill="x")
            
            book_label = ctk.CTkLabel(book_item_frame, text=book, font=("Arial", 11))
            book_label.pack(side="left", padx=10, pady=10)
            
            copies_label = ctk.CTkLabel(book_item_frame, text=copies, font=("Arial", 11, "bold"), text_color="#aaaaaa")
            copies_label.pack(side="right", padx=10, pady=10)
            
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
        print("Admin: Crear nuevo libro")
    
    def edit_book(self, book):
        print(f"Admin: Editar libro - {book}")
    
    def delete_book(self, book):
        print(f"Admin: Eliminar libro - {book}")
    
    def loan_book(self, book):
        print(f"Usuario: Prestar libro - {book}")

