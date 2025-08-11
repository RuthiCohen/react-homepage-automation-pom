import pytest
from pages.home_page import HomePage

class TestHomepage:
    """Test cases for React.dev homepage basic functionality"""
    
    def test_homepage_loads_successfully(self, driver):
        """Test that homepage loads with correct title"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        assert "React" in home_page.get_page_title()
        
        assert home_page.is_element_visible(home_page.MAIN_CONTENT)
    
    def test_header_and_footer_visible(self, driver):
        """Test that header and footer are present"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        assert home_page.is_header_visible()
        home_page.scroll_to_footer()
        assert home_page.is_footer_visible()
    
    def test_navigation_links_present(self, driver):
        """Test that navigation links are present"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        nav_links = home_page.get_navigation_links()
        
        assert len(nav_links) > 0
        nav_links_lower = [link.lower() for link in nav_links]
        assert any("learn" in link for link in nav_links_lower)
    
    def test_call_to_action_buttons(self, driver):
        """Test that CTA buttons are visible"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        get_started_visible = home_page.is_element_visible(home_page.GET_STARTED_BUTTON)
        learn_visible = home_page.is_element_visible(home_page.LEARN_BUTTON)
        
        assert get_started_visible or learn_visible
    
    def test_code_examples_present(self, driver):
        """Test that code examples are displayed"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        code_examples = home_page.get_code_examples()
        assert len(code_examples) > 0
    
    def test_responsive_design(self, mobile_driver):
        """Test responsive design on mobile"""
        home_page = HomePage(mobile_driver)
        home_page.navigate_to_homepage()
        
        assert home_page.is_header_visible()
        assert home_page.is_element_visible(home_page.MAIN_CONTENT)