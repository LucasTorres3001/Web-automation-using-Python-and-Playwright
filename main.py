from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url='https://en.wikipedia.org/wiki/Main_Page')
    page.fill(selector='xpath=//*[@id="searchInput"]', value='Python (programming language)')
    page.locator(selector='xpath=//*[@id="searchform"]/div/button').click()
    time.sleep(10)