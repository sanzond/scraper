import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ODOO_URL = os.getenv("ODOO_URL", "https://ai.cnudi.cn/")
    ODOO_DB = os.getenv("ODOO_DB", "jxc2")
    ODOO_USER = os.getenv("ODOO_USER")
    ODOO_PASSWORD = os.getenv("ODOO_PASSWORD")
    
    BSC_SCAN_BASE_URL = "https://bscscan.com"
    DEBANK_BASE_URL = "https://debank.com/profile/"
    
    BROWSER_ARGS = [
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    ]
    
    REQUEST_TIMEOUT = 60000
    RETRY_ATTEMPTS = 3
    RETRY_DELAY = 15  # seconds