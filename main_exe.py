import tkinter as tk
from tkinter import messagebox
from threading import Thread
from app.services.browser_services import create_browser_profile, open_browser_with_profile


def open_single_browser():
    """
    Abre un navegador con un nombre de perfil personalizado.
    """
    profile_name = entry_profile_name.get().strip()
    if not profile_name:
        messagebox.showerror("Error", "Debe ingresar un nombre de perfil.")
        return

    try:
        create_browser_profile(profile_name)
        Thread(target=open_browser_with_profile, args=(profile_name,)).start()
        messagebox.showinfo("Éxito", f"Navegador '{profile_name}' iniciado.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Navegadores")
root.geometry("450x300")

# Título
label_title = tk.Label(root, text="Sistema de Navegadores Locales", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Entrada para navegador individual
label_single = tk.Label(root, text="Abrir Navegador con Perfil:")
label_single.pack()
entry_profile_name = tk.Entry(root, width=20)
entry_profile_name.pack(pady=5)
btn_open_single = tk.Button(root, text="Abrir Navegador", command=open_single_browser)
btn_open_single.pack(pady=5)

# Mensaje informativo
label_info = tk.Label(root, text="Cada navegador tendrá un perfil y headers únicos.")
label_info.pack(pady=10)

# Iniciar la interfaz
root.mainloop()
