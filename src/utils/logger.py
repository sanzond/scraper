import logging
from datetime import datetime
import sys
#注释说明：
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File Handler
    file_handler = logging.FileHandler(
        f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger