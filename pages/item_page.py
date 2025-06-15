from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Item_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    add_to_cart_button = "//button[text()='Dodaj u korpu']"
    go_to_cart_button = "//button[text()='Pregledaj korpu']"

# Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

# Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Adding item to cart")

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print("Opening cart")

# Methods
    def item_to_cart(self): # go to Graphic Cards Page
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_go_to_cart_button()