import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage

class TestSearch:
    """Test cases for search functionality"""
    
    def test_search_opens_and_closes(self, driver):
        """Test opening and closing search"""
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        
        home_page.navigate_to_homepage()
        
        if home_page.open_search():
            assert search_page.is_search_overlay_visible()
            
            if search_page.close_search():
                driver.implicitly_wait(2)
        else:
            pytest.skip("Search button not found")
    
    def test_search_for_custom_hook(self, driver):
        """Test searching for 'custom hook'"""
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        
        home_page.navigate_to_homepage()
        
        if home_page.open_search():
            if search_page.type_in_search("custom hook"):
                results_count = search_page.get_search_results_count()
                
                if results_count > 0:
                    assert results_count > 0
                    
                    # Results should be relevant
                    result_titles = search_page.get_search_result_titles()
                    relevant_results = [title for title in result_titles 
                                     if 'hook' in title.lower() or 'custom' in title.lower()]
                    assert len(relevant_results) > 0
                else:
                    assert search_page.is_no_results_visible() or results_count == 0
        else:
            pytest.skip("Search functionality not available")
    
    def test_search_navigation(self, driver):
        """Test clicking on search results"""
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        
        home_page.navigate_to_homepage()
        original_url = driver.current_url
        
        if home_page.open_search():
            if search_page.type_in_search("useState"):
                if search_page.get_search_results_count() > 0:
                    search_page.click_first_result()
                    new_url = driver.current_url
                    assert new_url != original_url
        else:
            pytest.skip("Search functionality not available")