class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def wait_for_visible(self, selector):
        return self.page.locator(selector)
