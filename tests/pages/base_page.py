from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def go_to(self, url):
        """Navigate to a URL"""
        self.driver.get(url)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Wait for page to fully load"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        time.sleep(1)  # Extra safety buffer
    
    def find_element(self, locator, timeout=10):
        """Find a single element with wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
    
    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            return []
    
    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def click_element(self, locator):
        """Click an element with wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def scroll_to_element(self, element):
        """Scroll to make element visible"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def take_screenshot(self, filename):
        """Take a screenshot"""
        self.driver.save_screenshot(f"screenshots/{filename}.png")