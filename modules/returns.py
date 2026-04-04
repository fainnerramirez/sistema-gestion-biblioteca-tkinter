# Devoluciones
import customtkinter as ctk
from tkinter import messagebox

class ReturnsScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, loans=[], books=[]):
        super().__init__(parent)
        self.on_back = on_back
        self.library_loans = loans
        self.library_books = books
        self.return_widgets = {} 
        
        # Título
        title_label = ctk.CTkLabel(self, text="Registrar Devolución", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Frame para lista de préstamos
        loans_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        loans_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        loans_title = ctk.CTkLabel(loans_frame, text="Préstamos Activos para Devolver", font=("Arial", 14, "bold"))
        loans_title.pack(pady=10)
        
        # Frame interno para los items
        self.items_frame = ctk.CTkFrame(loans_frame, fg_color="transparent")
        self.items_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Mostrar préstamos
        if self.library_loans:
            for idx, loan in enumerate(self.library_loans, 1):
                self.add_loan_item(idx, loan)
        else:
            empty_label = ctk.CTkLabel(self.items_frame, text="No hay préstamos pendientes", font=("Arial", 12), text_color="#888888")
            empty_label.pack(pady=20)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)
    
    def add_loan_item(self, idx, loan):
        """Agrega un item de préstamo a la pantalla"""
        item_frame = ctk.CTkFrame(self.items_frame, fg_color="#1a1a1a", corner_radius=5)
        item_frame.pack(pady=8, fill="x")
        
        # Info del préstamo
        info_text = f"{idx}. {loan['user']} - {loan['title']} ({loan['author']}) - Prestado: {loan['loan_date']}"
        info_label = ctk.CTkLabel(item_frame, text=info_text, font=("Arial", 11))
        info_label.pack(side="left", padx=10, pady=10)
        
        # Botón Devolver
        def devolver_libro():
            self.return_book(loan, item_frame, idx)
        
        return_btn = ctk.CTkButton(item_frame, text="Devolver", width=80, fg_color="#2b5f2b", 
                                   hover_color="#1e4620", command=devolver_libro)
        return_btn.pack(side="right", padx=10, pady=10)
        
        # Guardar referencias
        self.return_widgets[idx] = {
            'frame': item_frame,
            'label': info_label
        }
    
    def return_book(self, loan, item_frame, idx):
        """Procesa la devolución de un libro"""
        # Buscar el libro en la lista de libros
        book = next((b for b in self.library_books if b['id'] == loan['book_id']), None)
        
        if book:
            # Agregar una copia del libro
            book['copies'] += 1
            
            # Eliminar el préstamo de la lista
            self.library_loans.remove(loan)
            
            # Eliminar el widget
            item_frame.destroy()
            del self.return_widgets[idx]
            
            # Mostrar confirmación
            messagebox.showinfo("Devolución Registrada", 
                              f"'{loan['title']}' ha sido devuelto por {loan['user']}\n"
                              f"Copias disponibles: {book['copies']}")
            
            # Si no hay más préstamos, mostrar mensaje
            if not self.library_loans:
                empty_label = ctk.CTkLabel(self.items_frame, text="No hay préstamos pendientes", 
                                          font=("Arial", 12), text_color="#888888")
                empty_label.pack(pady=20)
        else:
            messagebox.showerror("Error", "No se encontró el libro en el sistema")