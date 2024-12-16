import subprocess
import requests
from app.utils.logger import setup_logger
from app.utils.config import Config

logger = setup_logger()

def restart_network_linux():
    """
    Reinicia la red en Linux usando la interfaz configurada en el .env.
    """
    try:
        subprocess.run(["sudo", "ifconfig", Config.INTERFACE_LINUX, "down"], check=True)
        subprocess.run(["sudo", "ifconfig", Config.INTERFACE_LINUX, "up"], check=True)
        print(f"[INFO] Red reiniciada en Linux (Interfaz: {Config.INTERFACE_LINUX})")
        logger.info("Red reiniciada en Linux")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al reiniciar la red en Linux: {e}")
        raise

def restart_network_windows():
    """
    Reinicia la red en Windows usando la interfaz configurada en el .env.
    """
    try:
        subprocess.run(["netsh", "interface", "set", "interface", Config.INTERFACE_WINDOWS, "disable"], check=True)
        subprocess.run(["netsh", "interface", "set", "interface", Config.INTERFACE_WINDOWS, "enable"], check=True)
        print(f"[INFO] Red reiniciada en Windows (Interfaz: {Config.INTERFACE_WINDOWS})")
        logger.info("Red reiniciada en Windows")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al reiniciar la red en Windows: {e}")
        raise

def get_public_ip():
    """
    Obtiene la dirección IP pública utilizando múltiples servicios como fallback.
    """
    ip_services = [
        "https://api.ipify.org?format=json",
        "https://api64.ipify.org?format=json",
        "https://ipinfo.io/json",
        "https://ifconfig.me"
    ]

    for service in ip_services:
        try:
            print(f"[INFO] Intentando obtener IP desde: {service}")
            response = requests.get(service, timeout=5)
            response.raise_for_status()
            if "json" in service:
                ip = response.json().get("ip")
            else:
                ip = response.text.strip()
            if ip:
                logger.info(f"IP pública obtenida: {ip}")
                return ip
        except requests.RequestException as e:
            logger.error(f"Error al obtener IP desde {service}: {e}")
    
    logger.error("No se pudo obtener la IP pública desde ninguno de los servicios.")
    return None
