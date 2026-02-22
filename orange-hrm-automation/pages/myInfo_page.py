from playwright.sync_api import Page

class MyInfoPage(Page):
    def __init__(self, page):
        self.page = page
        self.my_info_tab = page.locator('span:has-text("My Info")')

    def clickMy_Info(self):
        self.my_info_tab.click()

    def select_nationality_dropdown(self):
        self.personalDetails_nationality.click()
        self.personalDetails_nationalitySelect.click()
        self.personalDetails_saveButton.click()


