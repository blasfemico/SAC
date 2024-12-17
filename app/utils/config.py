import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    LOG_FILE = os.getenv("LOG_FILE", "ip_rotation.log")
    DATABASE_URL = os.getenv("DATABASE_URL")

    INTERFACE_LINUX = os.getenv("INTERFACE_LINUX", "enp3s0")
    INTERFACE_WINDOWS = os.getenv("INTERFACE_WINDOWS", "Ethernet")

    IP_SERVICE_URL = os.getenv("IP_SERVICE_URL", "https://api.ipify.org?format=json")
    BROWSER_PROFILES_DIR = "profiles"


    CHROME_EXECUTABLE_WINDOWS = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    CHROME_EXECUTABLE_LINUX = "/usr/bin/google-chrome"

    LOG_FILE = "browser_manager.log"
