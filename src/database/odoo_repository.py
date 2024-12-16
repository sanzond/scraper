from typing import Dict, Any
import odoorpc
from datetime import datetime
from config.settings import Settings
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class OdooRepository:
    def __init__(self):
        self.odoo = self._connect_odoo()
    
    def _connect_odoo(self) -> odoorpc.ODOO:
        try:
            odoo = odoorpc.ODOO('172.26.32.1', port='18080')
            odoo.login(Settings.ODOO_DB, Settings.ODOO_USER, Settings.ODOO_PASSWORD)
            return odoo
        except Exception as e:
            logger.error(f"Failed to connect to Odoo: {str(e)}")
            raise
    
    def save_holder(self, data: Dict[str, Any]) -> None:
        try:
            logger.info(f"Saving holder data: {data}")
            self.odoo.env["onchain.holder"].create(data)
        except Exception as e:
            logger.error(f"Failed to save holder data: {str(e)}")
            raise
    
    def save_transaction(self, data: Dict[str, Any]) -> None:
        try:
            exist = self.odoo.env["onchain.transaction"].search_count(
                [("hash", "=", data['hash'])]
            )
            if not exist:
                logger.info(f"Saving transaction data: {data}")
                self.odoo.env["onchain.transaction"].create(data)
            else:
                logger.info(f"Transaction hash already exists: {data['hash']}")
        except Exception as e:
            logger.error(f"Failed to save transaction: {str(e)}")
            raise