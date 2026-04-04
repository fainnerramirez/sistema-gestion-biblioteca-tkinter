import customtkinter as ctk

class LoansScreen(ctk.CTkFrame):
    def __init__(self, parent, on_back, loans=[]):
        super().__init__(parent)
        self.on_back = on_back
        self.library_loans = loans
        
        # Título
        title_label = ctk.CTkLabel(self, text="Gestión de Préstamos", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Frame para lista de préstamos con scrollbar
        loans_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        loans_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        loans_title = ctk.CTkLabel(loans_frame, text="Préstamos Activos", font=("Arial", 14, "bold"))
        loans_title.pack(pady=10)
        
        # Frame para scroll
        scroll_frame = ctk.CTkFrame(loans_frame)
        scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        if self.library_loans:
            for idx, loan in enumerate(self.library_loans, 1):
                loan_item = ctk.CTkFrame(scroll_frame, fg_color="#1a1a1a", corner_radius=5)
                loan_item.pack(pady=8, fill="x")
                
                loan_text = f"{idx}. {loan['user']} - {loan['title']} - {loan['loan_date']}"
                loan_label = ctk.CTkLabel(loan_item, text=loan_text, font=("Arial", 11))
                loan_label.pack(pady=10, padx=10)
        else:
            empty_label = ctk.CTkLabel(scroll_frame, text="No hay préstamos registrados", font=("Arial", 12), text_color="#888888")
            empty_label.pack(pady=20)
        
        back_button = ctk.CTkButton(self, text="Volver al Dashboard", command=self.on_back, 
                                    fg_color="#cc3333", hover_color="#aa2222")
        back_button.pack(pady=20)