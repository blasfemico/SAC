import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from app.utils.logger import setup_logger

logger = setup_logger()

class InteractionManager:
    """
    Clase para manejar interacciones automatizadas en Facebook.
    """

    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.driver = None

        # Límites diarios para acciones
        self.MAX_LIKES_PER_DAY = 10
        self.MAX_COMMENTS_PER_DAY = 5
        self.MAX_REACTIONS_PER_DAY = 8

        self.profile_stats = {
            "likes": 0,
            "comments": 0,
            "reactions": 0
        }

    def simulate_human_behavior(self):
        """
        Simula pausas humanas con tiempos aleatorios.
        """
        delay = random.uniform(2, 5)  # Pausas de 2 a 5 segundos
        logger.info(f"Simulando pausa de {round(delay, 2)} segundos.")
        time.sleep(delay)

    def check_daily_limits(self, action_type):
        """
        Verifica si el límite diario de una acción ha sido alcanzado.
        """
        if self.profile_stats[action_type] >= getattr(self, f"MAX_{action_type.upper()}_PER_DAY"):
            logger.info(f"Límite diario alcanzado para {action_type}. Total realizado: {self.profile_stats[action_type]}")
            return False
        self.profile_stats[action_type] += 1
        logger.info(f"{action_type.capitalize()} realizado. Total hasta ahora: {self.profile_stats[action_type]}")
        return True

    def like_posts(self):
        """
        Automatiza dar likes en publicaciones de Facebook.
        """
        try:
            logger.info("Buscando publicaciones para dar like...")
            posts = self.driver.find_elements(By.XPATH, '//div[@aria-label="Me gusta"]')
            if not posts:
                logger.warning("No se encontraron publicaciones para dar like.")
                return

            for post in posts[:random.randint(1, 3)]:  # Dar like a 1-3 publicaciones
                if not self.check_daily_limits("likes"):
                    break
                self.simulate_human_behavior()
                post.click()
                logger.info("Like dado a una publicación.")
        except Exception as e:
            logger.error(f"Error al dar like: {str(e)}")

    def comment_on_posts(self):
        """
        Automatiza comentarios en publicaciones del feed.
        """
        try:
            logger.info("Buscando publicaciones para comentar...")
            posts = self.driver.find_elements(By.XPATH, '//div[@aria-label="Escribir un comentario..."]')

            if not posts:
                logger.warning("No se encontraron publicaciones para comentar.")
                return

            comments = [
                "¡Qué interesante publicación! 😊",
                "Esto es increíble, gracias por compartir. 💡",
                "Muy buen contenido, sigue así. 🚀",
                "Me encanta esta idea, ¡excelente! 🌟"
            ]

            for post in posts[:random.randint(1, 2)]:  # Comentar de 1 a 2 publicaciones
                if not self.check_daily_limits("comments"):
                    break
                self.simulate_human_behavior()
                post.click()
                comment_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
                comment = random.choice(comments)
                comment_box.send_keys(comment)
                comment_box.send_keys("\ue007")  # Simula Enter para enviar el comentario
                logger.info(f"Comentario publicado: {comment}")
                self.simulate_human_behavior()
        except Exception as e:
            logger.error(f"Error al comentar publicaciones: {str(e)}")

    def react_to_posts(self):
        """
        Automatiza reacciones con emojis en publicaciones.
        """
        try:
            logger.info("Buscando publicaciones para reaccionar...")
            reactions = self.driver.find_elements(By.XPATH, '//div[@aria-label="Reaccionar"]')

            emoji_reactions = ["❤️", "😆", "😢", "😡", "👍"]

            for reaction in reactions[:random.randint(1, 3)]:  # Reaccionar de 1 a 3 publicaciones
                if not self.check_daily_limits("reactions"):
                    break
                self.simulate_human_behavior()
                ActionChains(self.driver).move_to_element(reaction).perform()
                emoji = random.choice(emoji_reactions)
                emoji_button = self.driver.find_element(By.XPATH, f'//div[@aria-label="{emoji}"]')
                emoji_button.click()
                logger.info(f"Reacción dada: {emoji}")
                self.simulate_human_behavior()
        except Exception as e:
            logger.error(f"Error al dar reacciones: {str(e)}")

    def execute_random_interaction(self):
        """
        Selecciona y ejecuta una interacción aleatoria.
        """
        logger.info("Seleccionando una interacción aleatoria...")
        actions = [self.like_posts, self.comment_on_posts, self.react_to_posts]  # Lista de interacciones
        action = random.choice(actions)  # Seleccionar una acción aleatoria
        action()

    def start_interactions(self, driver):
        """
        Inicia el navegador y las interacciones automatizadas.
        """
        self.driver = driver
        logger.info(f"Iniciando interacciones para el perfil: {self.profile_name}")

        # Realizar varias interacciones aleatorias
        for _ in range(random.randint(2, 5)):
            self.execute_random_interaction()

        logger.info(f"Interacciones completadas para el perfil: {self.profile_name}")
        self.driver.quit()
