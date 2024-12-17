import platform

def detect_os():
    """
    Detecta el sistema operativo del usuario.
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        return "windows"
    elif "linux" in os_name:
        return "linux"
    else:
        raise Exception("Sistema operativo no soportado.")
