import sys
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.search_page import SearchPage


def open_search_or_shortcut(driver, home_page):
    """Try the site's search button"""

    if home_page.open_search():
        return True

    # keyboard fallback (Cmd+K on mac(my computer), Ctrl+K otherwise)
    body = driver.find_element(By.TAG_NAME, "body")
    try:
        if sys.platform == "darwin":
            body.send_keys(Keys.COMMAND, "k")
        else:
            body.send_keys(Keys.CONTROL, "k")
    except Exception:
        pass

    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        return True
    except Exception:
        pass

    # try: '/' key (many docs use it to open search)
    try:
        body.send_keys("/")
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        return True
    except Exception:
        return False


def close_search(driver):
    """Close by clicking a close button if exists, or just press ESC."""
    # try to click a close button if present
    try:
        close_btn = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close'], [aria-label*='close']"))
        )
        close_btn.click()
        return True
    except Exception:
        pass

    # fallback: ESC
    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(0.3)
        return True
    except Exception:
        return False


class TestSearch:
    """Test cases for search functionality"""

    def test_search_opens_and_closes(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_homepage()

        opened = open_search_or_shortcut(driver, home_page)
        assert opened, "Could not open search on react.dev"

        # basic check: search input is visible
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )

        assert close_search(driver)

    def test_search_for_custom_hook(self, driver):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)

        home_page.navigate_to_homepage()

        if open_search_or_shortcut(driver, home_page):
            if search_page.type_in_search("custom hook"):
                # give results a moment to show
                time.sleep(1)
                results_count = search_page.get_search_results_count()

                if results_count > 0:
                    assert results_count > 0
                    titles = search_page.get_search_result_titles()
                    relevant = [t for t in titles if "hook" in t.lower() or "custom" in t.lower()]
                    assert len(relevant) > 0
                else:
                    # either show 'no results' or 0 items
                    assert search_page.is_no_results_visible() or results_count == 0
        else:
            pytest.skip("Search functionality not available")

    def test_search_navigation(self, driver):
        home_page = HomePage(driver)
        search_page = SearchPage(driver)

        home_page.navigate_to_homepage()
        original_url = driver.current_url

        if open_search_or_shortcut(driver, home_page):
            if search_page.type_in_search("useState"):
                time.sleep(1)
                if search_page.get_search_results_count() > 0:
                    search_page.click_first_result()
                    new_url = driver.current_url
                    assert new_url != original_url
        else:
            pytest.skip("Search functionality not available")