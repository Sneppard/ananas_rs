from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.common.keys import Keys
import tkinter as tk

class GC_page(Base): # Graphic cards page

    lowest_price = None
    product_name = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators
    gc_header = "//h1[text()='Grafičke kartice']" # h1 - заголовок на странице с видеокартами, проверки по соответствию текста заголовка достаточно, чтобы убедиться, что мы действительно на странице с графическими картами
    sort_by_price_from_low = "//option[@value='prod_merchant_inventories_sr_price_asc']"
    manufacturer_list_menu = "//p[text()[contains(.,'Proizvođač diskretnog GPU-a')]]"
    radeon_checkbox = "//p[text()='AMD Radeon']"
    internal_memory = "//p[text()[contains(.,'Interna memoriјa')]]"
    memory_12GB_checkbox = "//p[text()='12GB']"
    price_lowest = "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputMarginDense MuiOutlinedInput-inputMarginDense'])[1]"
    first_item = "(//h3)[1]"

# Getters
    def get_gc_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gc_header)))

    def get_sort_by_price_from_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price_from_low)))

    def get_manufacturer_list_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_list_menu)))

    def get_radeon_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radeon_checkbox)))

    def get_internal_memory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.internal_memory)))

    def get_memory_12GB_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory_12GB_checkbox)))

    def get_price_lowest(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_lowest)))

    def get_first_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_item)))

# Actions
    def check_gc_header(self):
        assert self.get_gc_header().text == "Grafičke kartice"
        print("We are on Graphic cards page")

    def click_sort_by_price_from_low(self):
        self.get_sort_by_price_from_low().click()
        print("Click on sort option list")

    def click_manufacturer_list_menu(self):
        self.get_manufacturer_list_menu().click()
        print("Open manufacturer list menu")

    def click_radeon_checkbox(self):
        self.get_radeon_checkbox().click()
        print("Click on radeon checkbox")

    def click_internal_memory(self):
        self.get_internal_memory().click()
        print("Click on internal memory")

    def click_memory_12GB_checkbox(self):
        self.get_memory_12GB_checkbox().click()
        print("Click on checkbox 12GB")

    def check_price_lowest(self): # Достаю значение из поля с библиотеками tkinter и Keys. Иным способом не выйдет тут.
        self.get_price_lowest().click()
        self.get_price_lowest().send_keys(Keys.CONTROL, 'a')
        self.get_price_lowest().send_keys(Keys.CONTROL, 'c')
        tk.Tk().withdraw()
        return "{:,}".format(int(tk.Tk().clipboard_get())).replace(",", ".") # для сравнения в корзине нужна будет отформатированная цена, поэтому я делаю это сразу

    def check_product_name(self):
        return self.get_first_item().text

    def click_first_item(self): # Клик будет на первый товар в списке после всех сортировок
        self.get_first_item().click()
        print("Click first item")

# Methods
    def select_item(self, lowest_price=None, product_name=None): # go to Graphic Cards Page
        self.get_current_url()
        self.check_gc_header()
        self.click_sort_by_price_from_low()
        self.click_manufacturer_list_menu()
        self.click_radeon_checkbox()
        self.click_internal_memory()
        self.click_memory_12GB_checkbox()
        GC_page.lowest_price = self.check_price_lowest()
        print("Lowest price: " + GC_page.lowest_price)
        GC_page.product_name = self.check_product_name()
        print("Product name: " + GC_page.product_name)
        self.click_first_item()