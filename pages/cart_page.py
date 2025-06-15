from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from pages.gc_page import GC_page


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators

# Getters
    def get_item_name_in_cart(self):
        item_name_in_cart = "//a[text()='" + str(GC_page.product_name) + "']"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, item_name_in_cart)))

    def get_item_price_in_cart(self):
        item_price_in_cart = "//span[text()='" + str(GC_page.lowest_price) + "']"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, item_price_in_cart)))

# Actions
    def assert_item_name_in_cart(self):
        assert self.get_item_name_in_cart().text == str(GC_page.product_name)
        print("Product name correct")

    def assert_item_price_in_cart(self):
        assert self.get_item_price_in_cart().text == str(GC_page.lowest_price)
        print("Price correct")

# Methods
    def assert_product(self): # go to Graphic Cards Page
        self.assert_item_name_in_cart()
        self.assert_item_price_in_cart()
        print("Sorry, but I won't create unnecessary accounts and won't bother real business too much\nMeaning, the tests are finished")