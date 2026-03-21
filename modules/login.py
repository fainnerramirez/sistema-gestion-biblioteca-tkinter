import customtkinter as ctk
import os
from PIL import Image

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, on_login):
        super().__init__(parent)
        self.on_login = on_login
        
        image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "ibero.png")
        
        if os.path.exists(image_path):
            try:
                pil_image = Image.open(image_path)
                ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(60, 60))
                image_label = ctk.CTkLabel(self, image=ctk_image, text="")
                image_label.image = ctk_image 
                image_label.pack(pady=20)
            except Exception as e:
                print(f"Error cargando imagen: {e}")
                emoji_label = ctk.CTkLabel(self, text="📚", font=("Arial", 64))
                emoji_label.pack(pady=20)
        else:
            emoji_label = ctk.CTkLabel(self, text="📚", font=("Arial", 64))
            emoji_label.pack(pady=20)
        
        # Título
        title_label = ctk.CTkLabel(self, text="Gestión de Biblioteca", font=("Arial", 32, "bold"))
        title_label.pack(pady=20)
                
        subtitle_label = ctk.CTkLabel(self, text="Selecciona tu rol", font=("Arial", 16))
        subtitle_label.pack(pady=10)
        
        # Frame para botones
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, expand=True)
        
        # Botón Admin
        admin_button = ctk.CTkButton(
            button_frame,
            text="Administrador",
            command=lambda: self.on_login("admin"),
            font=("Arial", 14, "bold"),
            width=200,
            height=60,
            fg_color="#2b5f2b",
            hover_color="#1e4620"
        )
        admin_button.pack(pady=20)
        
        admin_label = ctk.CTkLabel(button_frame, text="Crear, editar y eliminar libros", font=("Arial", 10), text_color="#888888")
        admin_label.pack()
        
        # Botón Usuario
        user_button = ctk.CTkButton(
            button_frame,
            text="Usuario",
            command=lambda: self.on_login("usuario"),
            font=("Arial", 14, "bold"),
            width=200,
            height=60,
            fg_color="#2b5f7f",
            hover_color="#1e4660"
        )
        user_button.pack(pady=20)
        
        user_label = ctk.CTkLabel(button_frame, text="Prestar y devolver libros", font=("Arial", 10), text_color="#888888")
        user_label.pack()
