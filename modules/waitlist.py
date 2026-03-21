# Lista de espera

import customtkinter as ctk

class WaitlistScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back):
        super().__init__(parent)
        self.on_back = on_back
        
        # Título
        title_label = ctk.CTkLabel(self, text="Gestión de Lista de Espera", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Frame para lista de espera
        waitlist_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        waitlist_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        waitlist_title = ctk.CTkLabel(waitlist_frame, text="Usuarios en Lista de Espera", font=("Arial", 14, "bold"))
        waitlist_title.pack(pady=10)
        
        # Aquí iría una tabla con usuarios en lista de espera (simulado por ahora)
        sample_waitlist = ["1. Juan Pérez - El Quijote", 
                           "2. María López - Cien Años de Soledad",
                           "3. Carlos García - 1984"]
        
        for entry in sample_waitlist:
            entry_label = ctk.CTkLabel(waitlist_frame, text=entry, font=("Arial", 11))
            entry_label.pack(pady=5)
        
        # Botón Volver
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)