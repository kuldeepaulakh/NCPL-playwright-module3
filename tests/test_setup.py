from playwright.sync_api import  Page ,Expect
def test_brwser_open(page: Page):
    page.goto("https://www.example.com/")
    Expect(page.locator("h1")).t0_be_visible()