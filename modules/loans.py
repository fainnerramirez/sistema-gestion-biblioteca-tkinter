import customtkinter as ctk

class LoansScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back):
        super().__init__(parent)
        self.on_back = on_back
        
        # Título
        title_label = ctk.CTkLabel(self, text="Gestión de Préstamos", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        sample_loans = ["1. Juan Pérez - El Quijote - 2024-06-01", 
                        "2. María López - Cien Años de Soledad - 2024-06-05"]
        
        for loan in sample_loans:
            loan_label = ctk.CTkLabel(self, text=loan, font=("Arial", 11))
            loan_label.pack(pady=5)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)