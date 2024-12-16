import platform
from app.utils.ip_utils import restart_network_linux, restart_network_windows, get_public_ip
from app.utils.config import Config

def change_ip_and_validate():
    """
    Detecta el sistema operativo, reinicia la red y valida la nueva IP.
    """
    os_type = platform.system().lower()
    print(f"[INFO] Sistema operativo detectado: {os_type}")
    config = Config()

    if "linux" in os_type:
        restart_network_linux()
    elif "windows" in os_type:
        restart_network_windows()
    else:
        raise Exception("Sistema operativo no soportado")

    # Validar nueva IP
    new_ip = get_public_ip()
    if not new_ip:
        raise Exception("No se pudo validar la nueva dirección IP.")
    return new_ip
