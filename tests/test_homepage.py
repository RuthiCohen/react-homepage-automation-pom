import pytest
from pages.home_page import HomePage

class TestHomepage:
    """Test cases for React.dev homepage basic functionality"""
    
    def test_homepage_loads_successfully(self, driver):
        """Test that homepage loads with correct title"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Check page title
        assert "React" in home_page.get_page_title()
        
        # Check main content is visible
        assert home_page.is_element_visible(home_page.MAIN_CONTENT)
    
    def test_header_and_footer_visible(self, driver):
        """Test that header and footer are present"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Check header
        assert home_page.is_header_visible()
        
        # Scroll to footer and check
        home_page.scroll_to_footer()
        assert home_page.is_footer_visible()
    
    def test_navigation_links_present(self, driver):
        """Test that navigation links are present"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        nav_links = home_page.get_navigation_links()
        
        # Should have some navigation links
        assert len(nav_links) > 0
        
        # Check for expected links (case insensitive)
        nav_links_lower = [link.lower() for link in nav_links]
        assert any("learn" in link for link in nav_links_lower)
    
    def test_call_to_action_buttons(self, driver):
        """Test that CTA buttons are visible"""
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()
        
        # Look for common CTA button text
        get_started_visible = home_page.is_element_visible(home_page.GET_STARTED_BUTTON)
        learn_visible = home_page.is_element_visible(home_page.LEARN_BUTTON)
        
        # At least one CTA should be visible
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
        
        # Header should still be visible on mobile
        assert home_page.is_header_visible()
        
        # Main content should be visible
        assert home_page.is_element_visible(home_page.MAIN_CONTENT)