from playwright.sync_api import sync_playwright, Browser, Page
from typing import Optional
from config.settings import Settings
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class BaseScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
    
    def _launch_browser(self) -> None:
        try:
            playwright = sync_playwright().start()
            self.browser = playwright.chromium.launch(
                headless=self.headless,
                args=Settings.BROWSER_ARGS
            )
        except Exception as e:
            logger.error(f"Failed to launch browser: {str(e)}")
            raise
    
    def _create_page(self) -> Page:
        if not self.browser:
            self._launch_browser()
        return self.browser.new_page()