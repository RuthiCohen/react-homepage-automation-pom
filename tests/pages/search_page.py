from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import time

class SearchPage(BasePage):
    """Page Object for search functionality"""
    
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='search'], .search-input")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-results, [role='listbox'], .results-container")
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, ".search-result, [role='option'], .result-item")
    CLOSE_SEARCH_BUTTON = (By.CSS_SELECTOR, "[aria-label*='close'], .close-search, button[title*='close']")
    SEARCH_OVERLAY = (By.CSS_SELECTOR, ".search-overlay, .search-modal, .search-container")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".no-results, .empty-results")
    
    def type_in_search(self, query):
        """Type in search input"""
        search_input = self.find_element(self.SEARCH_INPUT)
        if search_input:
            search_input.clear()
            search_input.send_keys(query)
            time.sleep(1)  # Wait for search 
            return True
        return False
    
    def press_enter(self):
        """Press Enter in search"""
        search_input = self.find_element(self.SEARCH_INPUT)
        if search_input:
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)
            return True
        return False
    
    def click_first_result(self):
        """Click the first search result"""
        results = self.find_elements(self.SEARCH_RESULT_ITEMS)
        if results:
            results[0].click()
            return True
        return False
    
    def get_search_results_count(self):
        """Get number of search results"""
        results = self.find_elements(self.SEARCH_RESULT_ITEMS)
        return len(results)
    
    def get_search_result_titles(self):
        """Get titles of search results"""
        results = self.find_elements(self.SEARCH_RESULT_ITEMS)
        titles = []
        
        for result in results:
            title = result.text.strip()
            if title:
                titles.append(title)
        
        return titles
    
    def close_search(self):
        """Close search overlay"""
        if self.is_element_visible(self.CLOSE_SEARCH_BUTTON):
            self.click_element(self.CLOSE_SEARCH_BUTTON)
            return True
        return False
    
    def is_search_overlay_visible(self):
        """Check if search overlay is visible"""
        return self.is_element_visible(self.SEARCH_OVERLAY)
    
    def is_no_results_visible(self):
        """Check if no results message is visible"""
        return self.is_element_visible(self.NO_RESULTS_MESSAGE)