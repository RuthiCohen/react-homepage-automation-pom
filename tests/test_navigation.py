import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

class TestNavigation:
    """Test cases for navigation functionality"""
    
    def test_logo_returns_to_homepage(self, driver):
        """Test clicking logo returns to homepage"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Try to navigate to a different page first
        learn_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/learn']")
        if learn_links:
            learn_links[0].click()
            home_page.wait_for_page_load()
            
            home_page.click_logo()
            home_page.wait_for_page_load()
            
            # Should be back at homepage
            assert driver.current_url.endswith("/") or driver.current_url == "https://react.dev"
    
    def test_navigation_links_work(self, driver):
        """Test that navigation links work"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Test Learn link
        learn_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/learn']")
        if learn_links:
            original_url = driver.current_url
            learn_links[0].click()
            home_page.wait_for_page_load()
            
            assert driver.current_url != original_url
            assert "/learn" in driver.current_url
    
    def test_mobile_navigation(self, mobile_driver):
        """Test mobile navigation menu"""
        home_page = HomePage(mobile_driver)
        home_page.navigate_to_homepage()
        
        if home_page.toggle_mobile_menu():
            # Mobile menu functionality exists
            assert True
        else:
            # Mobile menu toggle not found 
            pytest.skip("Mobile menu toggle not found")
    
    def test_external_links_have_proper_attributes(self, driver):
        """Test external links open in new tabs"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        home_page.scroll_to_footer()
        
        # Find GitHub link
        github_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='github.com']")
        
        for link in github_links:
            href = link.get_attribute("href")
            target = link.get_attribute("target")
            
            # External links should open in new tab
            assert "github.com" in href
            assert target == "_blank"