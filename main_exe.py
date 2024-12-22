import tkinter as tk
from tkinter import messagebox
from threading import Thread
from app.services.browser_services import create_browser_profile, open_browser_with_profile
from app.services.ip_services import change_ip_and_validate
from app.services.interaction_services import InteractionManager
from app.utils.logger import setup_logger
import os

logger = setup_logger()

def rotate_ip_manual():
    """
    Rota la IP manualmente y muestra el resultado en la interfaz.
    """
    try:
        new_ip = change_ip_and_validate()
        messagebox.showinfo("Rotación de IP", f"Nueva IP: {new_ip}")
        logger.info(f"Rotación de IP manual realizada. Nueva IP: {new_ip}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al rotar la IP: {str(e)}")
        logger.error(f"Error al rotar la IP manualmente: {str(e)}")

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
        logger.info(f"Navegador con perfil '{profile_name}' iniciado manualmente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
        logger.error(f"Error al iniciar navegador con perfil '{profile_name}': {str(e)}")

def run_automated_script():
    """
    Ejecuta el script automatizado para todas las interacciones.
    """
    try:
        logger.info("Iniciando script automatizado para interacciones.")
        profiles = os.listdir("profiles")
        if not profiles:
            messagebox.showwarning("Advertencia", "No hay perfiles disponibles para automatización.")
            logger.warning("No se encontraron perfiles para la automatización.")
            return

        for profile in profiles:
            messagebox.showinfo("Automatización", f"Ejecutando interacciones para el perfil: {profile}")
            InteractionManager(profile)

        messagebox.showinfo("Éxito", "Script automatizado ejecutado correctamente.")
        logger.info("Script automatizado completado.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el script automatizado: {str(e)}")
        logger.error(f"Error en script automatizado: {str(e)}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Navegadores e IPs")
root.geometry("500x400")

# Título
label_title = tk.Label(root, text="Sistema de Navegadores e Interacciones", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Rotación de IP manual
btn_rotate_ip = tk.Button(root, text="Rotar IP Manualmente", command=rotate_ip_manual)
btn_rotate_ip.pack(pady=10)

# Entrada para navegador individual
label_single = tk.Label(root, text="Abrir Navegador con Perfil:")
label_single.pack()
entry_profile_name = tk.Entry(root, width=20)
entry_profile_name.pack(pady=5)
btn_open_single = tk.Button(root, text="Abrir Navegador", command=open_single_browser)
btn_open_single.pack(pady=10)

# Ejecución automatizada
btn_run_automation = tk.Button(root, text="Iniciar Script Automatizado", command=run_automated_script)
btn_run_automation.pack(pady=10)

# Mensaje informativo
label_info = tk.Label(root, text="Cada navegador tendrá un perfil y headers únicos.")
label_info.pack(pady=10)

# Iniciar la interfaz
def start_gui():
    try:
        logger.info("Interfaz gráfica iniciada.")
        root.mainloop()
    except Exception as e:
        logger.error(f"Error al iniciar la interfaz gráfica: {str(e)}")

if __name__ == "__main__":
    start_gui()
