"""
Module de logging pour l'application
"""

import logging
import os
from datetime import datetime
from typing import Optional


class GameLogger:
    """Logger personnalisé pour le jeu"""
    
    def __init__(self, name: str = "game", log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Éviter les doublons de handlers
        if not self.logger.handlers:
            self._setup_handlers(log_file)
    
    def _setup_handlers(self, log_file: Optional[str] = None):
        """Configure les handlers de logging"""
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        if log_file or os.path.exists("logs"):
            log_path = log_file or f"logs/game_{datetime.now().strftime('%Y%m%d')}.log"
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            
            file_handler = logging.FileHandler(log_path, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def info(self, message: str):
        """Log un message info"""
        self.logger.info(message)
    
    def error(self, message: str):
        """Log un message d'erreur"""
        self.logger.error(message)
    
    def debug(self, message: str):
        """Log un message de debug"""
        self.logger.debug(message)
    
    def warning(self, message: str):
        """Log un message d'avertissement"""
        self.logger.warning(message)


# Instance globale du logger
_logger_instance: Optional[GameLogger] = None


def get_logger(name: str = "game", log_file: Optional[str] = None) -> GameLogger:
    """
    Récupère une instance du logger
    
    Args:
        name (str): Nom du logger
        log_file (Optional[str]): Fichier de log
        
    Returns:
        GameLogger: Instance du logger
    """
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = GameLogger(name, log_file)
    return _logger_instance
