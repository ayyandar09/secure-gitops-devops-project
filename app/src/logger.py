import logging
from config import Config

def setup_logger():
    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )
