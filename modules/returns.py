# Devoluciones
import customtkinter as ctk

class ReturnsScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back):
        super().__init__(parent)
        self.on_back = on_back
        
        # Título
        title_label = ctk.CTkLabel(self, text="Registrar Devolución", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Aquí iría la lógica para registrar devoluciones (simulado por ahora)
        sample_returns = ["1. Juan Pérez - El Quijote - Devuelto el 2024-06-10", 
                          "2. María López - Cien Años de Soledad - Devuelto el 2024-06-12"]
        
        for ret in sample_returns:
            return_label = ctk.CTkLabel(self, text=ret, font=("Arial", 11))
            return_label.pack(pady=5)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)