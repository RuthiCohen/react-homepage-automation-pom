from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import time

class HomePage(BasePage):
    """Page Object for React.dev homepage"""
    
    # Locators
    HEADER = (By.TAG_NAME, "header")
    FOOTER = (By.TAG_NAME, "footer")
    LOGO = (By.CSS_SELECTOR, "[aria-label*='React'], img[alt*='React'], .logo")
    NAVIGATION_LINKS = (By.CSS_SELECTOR, "nav a, [role='navigation'] a")
    THEME_TOGGLE = (By.CSS_SELECTOR, "[aria-label*='theme'], button[title*='theme'], .theme-toggle")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[aria-label*='search'], button[title*='search'], .search-button")
    
    # Main content
    MAIN_CONTENT = (By.TAG_NAME, "main")
    GET_STARTED_BUTTON = (By.XPATH, "//a[contains(text(), 'Get Started')] | //button[contains(text(), 'Get Started')]")
    LEARN_BUTTON = (By.XPATH, "//a[contains(text(), 'Learn')] | //button[contains(text(), 'Learn')]")
    CODE_EXAMPLES = (By.CSS_SELECTOR, "pre, code, .code-example, .highlight")
    
    # Mobile elements
    MOBILE_MENU_TOGGLE = (By.CSS_SELECTOR, "[aria-label*='menu'], .menu-toggle, button[aria-expanded]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://react.dev"
    
    def navigate_to_homepage(self):
        """Navigate to React.dev homepage"""
        self.go_to(self.base_url)
    
    def is_header_visible(self):
        """Check if header is visible"""
        return self.is_element_visible(self.HEADER)
    
    def is_footer_visible(self):
        """Check if footer is visible"""
        return self.is_element_visible(self.FOOTER)
    
    def click_logo(self):
        """Click the React logo"""
        self.click_element(self.LOGO)
    
    def toggle_theme(self):
        """Toggle between light and dark theme"""
        if self.is_element_visible(self.THEME_TOGGLE):
            self.click_element(self.THEME_TOGGLE)
            time.sleep(1)  # Wait for theme transition
            return True
        return False
    
    def get_current_theme(self):
        """Get current theme (light/dark)"""
        html_element = self.driver.find_element(By.TAG_NAME, "html")
        
        data_theme = html_element.get_attribute("data-theme")
        if data_theme:
            return data_theme
        
        class_name = html_element.get_attribute("class") or ""
        if "dark" in class_name.lower():
            return "dark"
        elif "light" in class_name.lower():
            return "light"
        
        body_bg = self.driver.execute_script(
            "return window.getComputedStyle(document.body).backgroundColor"
        )
        
        if "0, 0, 0" in body_bg or body_bg == "rgb(0, 0, 0)":
            return "dark"
        else:
            return "light"
    
    def open_search(self):
        """Open search functionality"""
        if self.is_element_visible(self.SEARCH_BUTTON):
            self.click_element(self.SEARCH_BUTTON)
            return True
        return False
    
    def get_navigation_links(self):
        """Get all navigation link texts"""
        links = self.find_elements(self.NAVIGATION_LINKS)
        link_texts = []
        
        for link in links:
            text = link.text.strip()
            if text:  
                link_texts.append(text)
        
        return link_texts
    
    def click_get_started(self):
        """Click Get Started button"""
        if self.is_element_visible(self.GET_STARTED_BUTTON):
            self.click_element(self.GET_STARTED_BUTTON)
            return True
        return False
    
    def get_code_examples(self):
        """Get all code example texts"""
        code_blocks = self.find_elements(self.CODE_EXAMPLES)
        code_texts = []
        
        for block in code_blocks:
            text = block.text.strip()
            if text:
                code_texts.append(text)
        
        return code_texts
    
    def scroll_to_footer(self):
        """Scroll to footer"""
        self.scroll_to_bottom()
    
    
    def toggle_mobile_menu(self):
        """Toggle mobile navigation menu"""
        if self.is_element_visible(self.MOBILE_MENU_TOGGLE):
            self.click_element(self.MOBILE_MENU_TOGGLE)
            time.sleep(0.5)
            return True
        return False