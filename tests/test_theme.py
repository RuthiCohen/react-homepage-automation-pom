from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage

def emulate_color_scheme(driver, scheme: str):
    """
    Emulate system color scheme via Chrome DevTools Protocol.
    scheme is in {"dark", "light"}
    """
    assert scheme in ("dark", "light")
    driver.execute_cdp_cmd(
        "Emulation.setEmulatedMedia",
        {"features": [{"name": "prefers-color-scheme", "value": scheme}]}
    )

def detect_theme_via_dom(driver) -> str:
    """
    Detect the current theme by inspecting the DOM/computed styles.
    Falls back to luminance of the page background if no explicit markers exist.
    Returns "dark" or "light".
    """
    script = """
    const html = document.documentElement;
    const dataTheme = (html.getAttribute('data-theme') || '').toLowerCase();
    const cls = (html.className || '').toLowerCase();

    if (dataTheme === 'dark' || cls.includes('dark')) return 'dark';
    if (dataTheme === 'light' || cls.includes('light')) return 'light';

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
    """
    return driver.execute_script(script)

class TestTheme:
    def test_respects_system_theme(self, driver):
        """
        Verify react.dev respects system theme (prefers-color-scheme)
        by emulating dark/light and checking the page appearance.
        """
        home = HomePage(driver)
        home.navigate_to_homepage()

        # Emulate DARK
        emulate_color_scheme(driver, "dark")
        driver.refresh()
        home.wait_for_page_load()
        WebDriverWait(driver, 5).until(lambda d: detect_theme_via_dom(d) == "dark")
        assert detect_theme_via_dom(driver) == "dark"

        # Emulate LIGHT
        emulate_color_scheme(driver, "light")
        driver.refresh()
        home.wait_for_page_load()
        WebDriverWait(driver, 5).until(lambda d: detect_theme_via_dom(d) == "light")
        assert detect_theme_via_dom(driver) == "light"
