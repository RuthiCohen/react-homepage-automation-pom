from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAccessibility:
    """Test cases for accessibility features"""
    
    def test_keyboard_navigation(self, driver):
        """Test keyboard navigation"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()
        
        # Tab through elements
        focusable_elements = []
        for i in range(10):  # Tab through first 10 elements
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.TAB)
            focused = driver.execute_script("return document.activeElement")
            
            if focused:
                tag_name = focused.tag_name
                text = focused.text[:50] if focused.text else ""  # First 50 chars
                focusable_elements.append({"tag": tag_name, "text": text})
        
        assert len(focusable_elements) > 0
        
        interactive_tags = ["a", "button", "input"]
        found_interactive = any(elem["tag"].lower() in interactive_tags 
                              for elem in focusable_elements)
        assert found_interactive
    
    def test_heading_structure(self, driver):
        """Test proper heading hierarchy"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Find all headings
        headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6")
        assert len(headings) > 0
        
        # Should have at least one h1
        h1_elements = driver.find_elements(By.TAG_NAME, "h1")
        assert len(h1_elements) >= 1
    
    def test_image_alt_text(self, driver):
        """Test that images have alt text"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Find all images
        images = driver.find_elements(By.TAG_NAME, "img")
        
        for img in images:
            alt_text = img.get_attribute("alt")
            aria_label = img.get_attribute("aria-label")
            role = img.get_attribute("role")
            
            # Images should have alt text, aria-label, or be decorative
            assert alt_text is not None or aria_label is not None or role == "presentation"