# 📚 Sistema de Gestión de Biblioteca

Una aplicación de escritorio para gestionar un sistema de biblioteca. Proyecto colaborativo para la clase de Estructura de Datos 2026.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|-----------|-----------|
| **Lenguaje** | Python 3.8+ |
| **Frontend** | Tkinter (Aplicación de Escritorio) |
| **Lógica** | Python |
| **Testing** | Playwright para Python |

---

## 📋 Plan del Proyecto

### Funcionalidades Requeridas

| # | Funcionalidad | Responsable |
|---|---|---|
| 1 | 🔐 Login | Fainner |
| 2 | 🏠 Dashboard/Homepage | Cristian |
| 3 | 🔍 Buscar Libro | Cristian |
| 4 | 📤 Prestar Libro | Miguel |
| 5 | 📥 Devolver Libro | Miguel |
| 6 | ⏳ Lista de Espera | Fainner |
| 7 | ⚙️ CRUD Administrador (Crear, Leer, Modificar, Eliminar) | John Ramírez |

---

## 🎨 Interfaz de Usuario

### Componentes
- **Framework UI**: Tkinter
- **Tipo de Aplicación**: Escritorio Multiplataforma
- **Responsividad**: Redimensionable con adaptación automática

### Paleta de Colores

```
🟦 Azul Primario:     #1E3A8A (Encabezados, botones principales)
🟦 Azul Secundario:   #3B82F6 (Botones secundarios, hover)
⚪ Fondo:             #F8FAFC (Fondo claro)
⚫ Texto Oscuro:      #1F2937 (Texto principal)
🟩 Verde Éxito:       #10B981 (Confirmaciones, éxito)
🟥 Rojo Error:        #EF4444 (Errores, validaciones)
🟨 Amarillo Alerta:   #F59E0B (Advertencias)
```

### Inspiración de Diseño
- 📌 **Pinterest**: Buscar referencias de diseño moderno
- 🎨 **Plantilla**: Uso de colores armoniosos y tipografía clara

---

## 🚀 Cómo Ejecutar

### Requisitos Previos

```bash
# Verificar versión de Python
python --version  # Python 3.8 o superior
```

### Instalación y Ejecución

**Windows:**
```bash
cd c:\Users\framir02\projects\universidad-ibero\estructura-datos-2026\gestion-biblioteca
python main.py
```

**Mac/Linux:**
```bash
cd ~/ruta/al/proyecto/gestion-biblioteca
python3 main.py
```

**Desde VS Code:**
- Abre `main.py` y presiona `Ctrl + F5` (o `F5`)

---

## 🧪 Testing y Depuración

### Herramienta de Testing
- **Framework**: Playwright para Python
- **Propósito**: Automatización de pruebas E2E de la interfaz Tkinter
- **Instalación**:
```bash
pip install playwright
playwright install
```

**Ejemplo básico de prueba:**
```python
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        # Tu código de prueba aquí
        pass
```

---

## 📁 Estructura del Proyecto

```
gestion-biblioteca/
├── main.py                 # Punto de entrada de la aplicación
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
├── tests/                 # Pruebas automatizadas
│   └── test_cases.py
├── modules/               # Módulos de lógica
│   ├── auth.py           # Autenticación (Fainner)
│   ├── dashboard.py      # Dashboard (Cristian)
│   ├── search.py         # Búsqueda (Cristian)
│   ├── lending.py        # Préstamo (Miguel)
│   ├── returns.py        # Devoluciones (Miguel)
│   ├── waitlist.py       # Lista de espera (Fainner)
│   └── admin.py          # CRUD Admin (John Ramírez)
└── ui/                    # Componentes de interfaz
    ├── styles.py          # Estilos y colores
    └── components.py      # Widgets personalizados
```

---

## 👥 Equipo de Desarrollo

| Miembro | Responsabilidad |
|---------|-----------------|
| 🔐 Fainner | Login, Lista de Espera |
| 📊 Cristian | Dashboard, Búsqueda de Libros |
| 📦 Miguel | Préstamo y Devolución de Libros |
| ⚙️ John Ramírez | CRUD del Administrador |

---

## 💡 Recomendaciones de Desarrollo

### Estilo de Código
- Seguir PEP 8 (Python Enhancement Proposal)
- Usar nombres de variables descriptivos en español
- Documentar funciones con docstrings

### Control de Versiones
- El repositorio es **público** en GitHub
- Hacer commits descriptivos
- Crear ramas por funcionalidad: `feature/login`, `feature/dashboard`

### Colaboración
- Comunicarse por pull requests
- Revisar código antes de hacer merge
- Probar cambios localmente antes de pusear

---

## 📦 Dependencias

```
tkinter (incluido en Python)
playwright>=1.40.0
pytest>=7.0.0
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## 🎯 Próximos Pasos

1. ✅ Clonar el repositorio
2. ✅ Instalar dependencias
3. ✅ Revisar la estructura del proyecto
4. ✅ Crear rama para tu módulo
5. ✅ Comenzar desarrollo
6. ✅ Realizar pruebas locales
7. ✅ Hacer pull request

---

## 📞 Soporte

Si tienes dudas:
- Revisa la documentación de [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Consulta la documentación de [Playwright](https://playwright.dev/python/)
- Comunícate con tu equipo

---

**Proyecto**: Sistema de Gestión de Biblioteca  
**Curso**: Estructura de Datos 2026  
**Universidad**: Iberoamericana  
**Versión**: 1.0  
**Última actualización**: Marzo 2026
