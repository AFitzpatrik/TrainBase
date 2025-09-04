import re

from playwright.sync_api import sync_playwright, expect

def test_add_book():
    with sync_playwright() as p:
        #This so we can see browser in action during the test
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/ebook/create/")
        expect(page).to_have_title(re.compile("Add e-book"))
        page.fill('input[name="name"]', "name")
        page.select_option("#id_ebook_author", label="franta pepa jednička")
        page.wait_for_selector('textarea[name="description"]')
        page.fill('textarea[name="description"]', "Description")
        page.wait_for_timeout(4000)
        browser.close()
