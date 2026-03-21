import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
        
    def __init__(self, parent, role="usuario", on_books=None, on_loans=None, on_returns=None, on_waitlist=None, on_logout=None):
        super().__init__(parent)
        self.role = role
        self.on_books = on_books
        self.on_loans = on_loans
        self.on_returns = on_returns
        self.on_waitlist = on_waitlist
        self.on_logout = on_logout
        
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(padx=20, pady=10, fill="x")
        
        welcome_label = ctk.CTkLabel(header_frame, text=f"Bienvenido {role.upper()}", font=("Arial", 14, "bold"))
        welcome_label.pack(side="left")
        
        logout_button = ctk.CTkButton(header_frame, text="Cerrar Sesión", width=120, fg_color="#7f2b2b", hover_color="#601a1a", command=self.logout)
        logout_button.pack(side="right")
        
        grid_container = ctk.CTkFrame(self, fg_color="transparent")
        grid_container.pack(pady=15, padx=20, fill="both", expand=True)
        
        grid_container.grid_rowconfigure((0, 1), weight=1)
        grid_container.grid_columnconfigure((0, 1), weight=1)
        
        # LIBROS - disponible para todos
        self.frame_top_left = ctk.CTkFrame(grid_container, fg_color="#2b2b2b", corner_radius=10)
        self.frame_top_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        label_tl = ctk.CTkLabel(self.frame_top_left, text="Libros", font=("Arial", 16, "bold"))
        label_tl.pack(pady=20)
        button_tl = ctk.CTkButton(self.frame_top_left, text="Ir a Libros", command=self.go_to_books)
        button_tl.pack(pady=10)

        # PRÉSTAMOS - disponible para todos
        self.frame_top_right = ctk.CTkFrame(grid_container, fg_color="#2b2b2b", corner_radius=10)
        self.frame_top_right.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        label_tr = ctk.CTkLabel(self.frame_top_right, text="Préstamos", font=("Arial", 16, "bold"))
        label_tr.pack(pady=20)
        button_tr = ctk.CTkButton(self.frame_top_right, text="Ver Préstamos", command=self.go_to_loans)
        button_tr.pack(pady=10)

        # DEVOLUCIONES - disponible para todos
        self.frame_bottom_left = ctk.CTkFrame(grid_container, fg_color="#2b2b2b", corner_radius=10)
        self.frame_bottom_left.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        label_bl = ctk.CTkLabel(self.frame_bottom_left, text="Devoluciones", font=("Arial", 16, "bold"))
        label_bl.pack(pady=20)
        button_bl = ctk.CTkButton(self.frame_bottom_left, text="Registrar Devolución", command=self.go_to_returns)
        button_bl.pack(pady=10)

        # LISTA DE ESPERA - solo para ADMIN
        self.frame_bottom_right = ctk.CTkFrame(grid_container, fg_color="#2b2b2b", corner_radius=10)
        self.frame_bottom_right.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        if role == "admin":
            label_br = ctk.CTkLabel(self.frame_bottom_right, text="Lista de Espera", font=("Arial", 16, "bold"))
            label_br.pack(pady=20)
            button_br = ctk.CTkButton(self.frame_bottom_right, text="Gestionar Espera", command=self.go_to_waitlist)
            button_br.pack(pady=10)
        else:
            label_br = ctk.CTkLabel(self.frame_bottom_right, text="Acceso Solo Admin", font=("Arial", 16, "bold"), text_color="#888888")
            label_br.pack(pady=20)
            info_label = ctk.CTkLabel(self.frame_bottom_right, text="Esta sección es solo para\nadministradores", font=("Arial", 11), text_color="#666666")
            info_label.pack(pady=10)
    
    def go_to_books(self):
        if self.on_books:
            self.on_books()
    
    def go_to_loans(self):
        if self.on_loans:
            self.on_loans()
    
    def go_to_returns(self):
        if self.on_returns:
            self.on_returns()
    
    def go_to_waitlist(self):
        if self.on_waitlist:
            self.on_waitlist()
    
    def logout(self):
        if self.on_logout:
            self.on_logout()