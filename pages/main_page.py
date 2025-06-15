from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Main_page(Base):

    url = 'https://ananas.rs/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    agree_with_cookies_button = "//button[text()[contains(.,'Slažem se')]]"
    all_categories_menu = "//button[@title='Dugme za meni kategorija']"
    it_shop_button = "//span[text()[contains(.,'IT Shop')]]"
    gcp_button = "//a[text()[contains(.,'Grafičke kartice')]]" # Graphic cards page button.

# Getters
    def get_agree_with_cookies_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agree_with_cookies_button)))

    def get_all_categories_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_categories_menu)))

    def get_gcp_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gcp_button)))

    def get_it_shop_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.it_shop_button)))

# Actions
    def click_agree_with_cookies_button(self):
        try: # Try-except тут очень вряд ли нужно, так как мы в режиме гостя. Но пусть будет
            self.get_agree_with_cookies_button().click()
            print("Agreed with cookies conditions")
        except:
            print("Accepting cookies unnecessary this time")

    def hover_over_acm(self):
        ActionChains(self.driver).move_to_element(self.get_all_categories_menu()).perform()
        print("Hover mouse over All categories menu")

    def hover_over_isb(self):
        ActionChains(self.driver).move_to_element(self.get_it_shop_button()).perform()
        print("Hover mouse over All categories menu")

    def click_gcp_button(self):
        self.get_gcp_button().click()
        print("Click graphic cards page button")

# Methods
    def go_to_gcp(self): # go to Graphic Cards Page
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_agree_with_cookies_button()
        self.get_current_url()
        self.hover_over_acm()
        self.hover_over_isb()
        self.click_gcp_button()