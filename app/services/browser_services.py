from app.utils.browser_utils import get_unique_browser

def create_browser_profile(profile_name):
    """
    Crea un directorio para el perfil si no existe.
    """
    from app.utils.config import Config
    import os

    profile_path = os.path.join(Config.BROWSER_PROFILES_DIR, profile_name)
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
        print(f"[INFO] Perfil '{profile_name}' creado.")
    else:
        print(f"[INFO] Perfil '{profile_name}' ya existe.")

    return profile_path

def open_browser_with_profile(profile_name):
    """
    Abre un navegador Chrome con un perfil único.
    """
    create_browser_profile(profile_name)
    driver = get_unique_browser(profile_name)
    driver.get("https://www.whatismybrowser.com/")  
    print("[INFO] Navegador abierto correctamente.")
    return driver
