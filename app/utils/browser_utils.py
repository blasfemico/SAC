import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from app.utils.config import Config
from app.utils.logger import setup_logger
from app.utils.os_detector import detect_os

logger = setup_logger()

def ensure_profiles_folder():
    """
    Crea la carpeta de perfiles si no existe.
    """
    if not os.path.exists(Config.BROWSER_PROFILES_DIR):
        os.makedirs(Config.BROWSER_PROFILES_DIR)
        logger.info("Carpeta 'profiles' creada automáticamente.")
        print("[INFO] Carpeta 'profiles' creada automáticamente.")
    else:
        logger.info("Carpeta 'profiles' ya existe.")
        print("[INFO] Carpeta 'profiles' ya existe.")

def get_chrome_executable():
    """
    Retorna la ruta del ejecutable de Chrome según el sistema operativo.
    """
    os_type = detect_os()
    if os_type == "windows":
        return Config.CHROME_EXECUTABLE_WINDOWS
    elif os_type == "linux":
        return Config.CHROME_EXECUTABLE_LINUX
    else:
        raise Exception("Sistema operativo no soportado.")

def get_unique_browser(profile_name):
    """
    Abre un navegador Chrome con un perfil único y un User-Agent dinámico.
    """
    ensure_profiles_folder()  

    profile_path = os.path.join(Config.BROWSER_PROFILES_DIR, profile_name)
    os.makedirs(profile_path, exist_ok=True)

    ua = UserAgent()
    user_agent = ua.random


    chrome_options = Options()
    chrome_options.binary_location = get_chrome_executable()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    logger.info(f"Navegador con perfil '{profile_name}' iniciado. User-Agent: {user_agent}")
    print(f"[INFO] Navegador con perfil '{profile_name}' iniciado.")
    print(f"[INFO] User-Agent asignado: {user_agent}")
    return driver
