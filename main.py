import customtkinter as ctk
from modules.login import LoginScreen
from modules.dashboard import Dashboard
from modules.books import BooksScreen
from modules.loans import LoansScreen
from modules.returns import ReturnsScreen
from modules.waitlist import WaitlistScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  
        self.geometry("1024x550")
        self.title("Gestion De Biblioteca - Ibero 2026")
        
        self.current_screen = None
        self.role = None
        self.show_login()

    def show_login(self):
        """Mostrar pantalla de login"""
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = LoginScreen(self, on_login=self.login_user)
        self.current_screen.pack(fill="both", expand=True)
    
    def login_user(self, role):
        """Almacenar el rol y mostrar el dashboard"""
        self.role = role
        self.show_dashboard()

    def show_dashboard(self):
        """Mostrar pantalla del dashboard"""
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = Dashboard(self, role=self.role, on_books=self.show_books, on_loans=self.show_loans, on_returns=self.show_returns, on_waitlist=self.show_waitlist, on_logout=self.show_login)
        self.current_screen.pack(fill="both", expand=True)
    
    def show_books(self):
        """Mostrar pantalla de libros"""
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = BooksScreen(self, on_back=self.show_dashboard, role=self.role)
        self.current_screen.pack(fill="both", expand=True)
        
    def show_loans(self):
        """Mostrar pantalla de préstamos"""
        print("Navigating to Loans section...")
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = LoansScreen(self, on_back=self.show_dashboard)
        self.current_screen.pack(fill="both", expand=True)
        
    def show_returns(self):
        """Mostrar pantalla de devoluciones"""
        print("Navigating to Returns section...")
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = ReturnsScreen(self, on_back=self.show_dashboard)
        self.current_screen.pack(fill="both", expand=True)
        
    def show_waitlist(self):
        """Mostrar pantalla de lista de espera"""
        print("Navigating to Waitlist section...")
        if self.current_screen:
            self.current_screen.pack_forget()
        
        self.current_screen = WaitlistScreen(self, on_back=self.show_dashboard)
        self.current_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()