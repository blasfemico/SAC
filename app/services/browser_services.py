from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.utils.browser_utils import ensure_profiles_folder, get_random_user_agent
from app.utils.config import Config
import os

def create_browser_profile(profile_name):
    """
    Crea un directorio para el perfil si no existe.
    """
    profile_path = os.path.join(Config.BROWSER_PROFILES_DIR, profile_name)
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
        print(f"[INFO] Perfil '{profile_name}' creado.")
    else:
        print(f"[INFO] Perfil '{profile_name}' ya existe.")
    return profile_path

def open_browser_with_profile(profile_name):
    """
    Abre un navegador local con un perfil único y User-Agent aleatorio.
    """
    ensure_profiles_folder()

    # Configura la ruta del perfil
    profile_path = os.path.join(Config.BROWSER_PROFILES_DIR, profile_name)
    os.makedirs(profile_path, exist_ok=True)

    # Genera un User-Agent aleatorio
    user_agent = get_random_user_agent()

    # Configura Chrome
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Inicia el navegador localmente
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    print(f"[INFO] Navegador con perfil '{profile_name}' abierto. User-Agent: {user_agent}")
    driver.get("https://www.whatismybrowser.com/")  # Página de prueba
    return driver
