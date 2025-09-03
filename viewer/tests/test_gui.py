import re
from playwright.sync_api import Page, expect

def test_add_book(page: Page):
    page.goto("http://127.0.0.1:8000/ebook/create/")
    expect(page).to_have_title(re.compile("Add e-book"))
    page.get_by_label("name").fill("name")