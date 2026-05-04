import customtkinter as ctk
from tkinter import messagebox

class WaitlistScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, biblioteca=None):
        super().__init__(parent)
        self.on_back = on_back
        self.biblioteca = biblioteca
        
        # Título
        title_label = ctk.CTkLabel(self, text="Gestión de Lista de Espera (Sistema de Grafos)", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Frame para lista de espera
        waitlist_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        waitlist_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        waitlist_title = ctk.CTkLabel(waitlist_frame, text="Usuarios en Lista de Espera", font=("Arial", 14, "bold"))
        waitlist_title.pack(pady=10)
        
        self.items_frame = ctk.CTkFrame(waitlist_frame, fg_color="transparent")
        self.items_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Obtener lista de espera del grafo
        lista_espera = self.biblioteca.obtener_lista_espera()
        
        if lista_espera:
            for idx, entrada in enumerate(lista_espera, 1):
                item_frame = ctk.CTkFrame(self.items_frame, fg_color="#1a1a1a", corner_radius=5)
                item_frame.pack(pady=8, fill="x")
                
                entry_text = f"{idx}. {entrada['user']} - {entrada['title']} (agregado: {entrada['added_date']})"
                entry_label = ctk.CTkLabel(item_frame, text=entry_text, font=("Arial", 11))
                entry_label.pack(side="left", padx=10, pady=10)
                
                # Botón para procesar
                def procesar_espera(e=entrada, f=item_frame):
                    self.procesar_de_espera(e, f)
                
                process_btn = ctk.CTkButton(item_frame, text="Procesar", width=80, fg_color="#2b5f7f", 
                                           hover_color="#1e4660", command=procesar_espera)
                process_btn.pack(side="right", padx=10, pady=10)
        else:
            empty_label = ctk.CTkLabel(self.items_frame, text="No hay usuarios en lista de espera", 
                                      font=("Arial", 12), text_color="#888888")
            empty_label.pack(pady=20)
        
        # Frame para agregar a lista de espera
        add_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        add_frame.pack(padx=20, pady=10, fill="x")
        
        add_title = ctk.CTkLabel(add_frame, text="Agregar a Lista de Espera", font=("Arial", 12, "bold"))
        add_title.pack(pady=10)
        
        button_add_frame = ctk.CTkFrame(add_frame, fg_color="transparent")
        button_add_frame.pack(padx=10, pady=10, fill="x")
        
        add_btn = ctk.CTkButton(button_add_frame, text="Agregar Usuario a Espera", fg_color="#2b5f2b", 
                               hover_color="#1e4620", command=self.agregar_a_espera)
        add_btn.pack(fill="x", padx=5)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)
    
    def agregar_a_espera(self):
        """Abre un diálogo para agregar un usuario a la lista de espera"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Agregar a Lista de Espera")
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.transient(self.master)
        
        # Título
        title_label = ctk.CTkLabel(dialog, text="Ingrese los datos del usuario", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)
        
        # Usuario
        ctk.CTkLabel(dialog, text="ID de usuario:", font=("Arial", 11)).pack(anchor="w", padx=20, pady=(10, 0))
        user_entry = ctk.CTkEntry(dialog, placeholder_text="Ej: user123")
        user_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Libro
        ctk.CTkLabel(dialog, text="ID de libro:", font=("Arial", 11)).pack(anchor="w", padx=20, pady=(10, 0))
        book_entry = ctk.CTkEntry(dialog, placeholder_text="Ingrese el ID del libro")
        book_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Frame para botones
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=10, fill="x", padx=20)
        
        def agregar():
            user_id = user_entry.get().strip()
            book_id = book_entry.get().strip()
            
            if not user_id or not book_id:
                messagebox.showerror("Error", "Todos los campos son requeridos")
                return
            
            # Verificar que el libro existe
            libro = self.biblioteca.obtener_libro(book_id)
            if not libro:
                messagebox.showerror("Error", "El libro no existe en el sistema")
                return
            
            # Agregar a la lista de espera
            self.biblioteca.agregar_a_espera(user_id, book_id)
            
            dialog.destroy()
            messagebox.showinfo("Éxito", f"Usuario '{user_id}' agregado a la lista de espera para '{libro['title']}'")
        
        confirm_btn = ctk.CTkButton(button_frame, text="Agregar", fg_color="#2b5f2b", 
                                    hover_color="#1e4620", command=agregar)
        confirm_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancelar", fg_color="#7f2b2b", 
                                   hover_color="#601a1a", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=5, fill="x", expand=True)
    
    def procesar_de_espera(self, entrada, frame):
        """Procesa una entrada de la lista de espera"""
        self.biblioteca.eliminar_de_espera(entrada['id'])
        frame.destroy()
        messagebox.showinfo("Procesado", f"Se notificará a {entrada['user']} sobre la disponibilidad de '{entrada['title']}'")
