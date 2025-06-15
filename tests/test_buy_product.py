import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.gc_page import GC_page
from pages.item_page import Item_page
from pages.main_page import Main_page


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

def test_buy_product_1():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test 1")

    mp = Main_page(driver)
    mp.go_to_gcp()
    gcp = GC_page(driver)
    gcp.select_item()
    ip = Item_page(driver)
    ip.item_to_cart()
    cp = Cart_page(driver)
    cp.assert_product()

    time.sleep(10)
    driver.close()