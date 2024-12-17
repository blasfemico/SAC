import logging
from app.utils.config import Config

def setup_logger():
    """
    Configura un logger que guarda en el archivo definido en LOG_FILE.
    """
    logging.basicConfig(
        filename=Config.LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("IPRotationLogger")
    logger = logging.getLogger("BrowserManagerLogger")
    return logger
