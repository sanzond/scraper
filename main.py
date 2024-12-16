import sys
import json
from datetime import datetime, timedelta
from src.scrapers.bsc_scraper import BscScraper
from src.scrapers.debank_scraper import DeBankScraper
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    if len(sys.argv) <= 1:
        logger.error("No command provided")
        return
    
    command = sys.argv[1]
    
    if command == "debank":
        scraper = DeBankScraper()
        # Implement debank scraping logic
        
    elif command == "bsc":
        scraper = BscScraper()
        try:
            with open("tokeninfo.json", "r") as f:
                tokeninfo = json.load(f)
                for token in tokeninfo:
                    if token["active"]:
                        scraper.get_token_holders(
                            token["token"],
                            token["contact_address"],
                            token["pagecount"],
                            token["scale"]
                        )
        except Exception as e:
            logger.error(f"Failed to process BSC data: {str(e)}")
    
    else:
        logger.error(f"Unknown command: {command}")

if __name__ == "__main__":
    main()