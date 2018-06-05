import unittest
import settings
from locators import *
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests


class TrendyolAutomationTests(unittest.TestCase, ):

    def setUp(self):

        self.init_driver(settings.desired_driver)
        self.wait = ui.WebDriverWait(self.driver, 10)

    def init_driver(self, desired_driver):

        if desired_driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif desired_driver == 'firefox':
            self.driver = webdriver.Firefox()
        elif desired_driver == 'opera':
            self.driver = webdriver.Opera()
        self.driver.maximize_window()

    def check_page_exist(self, page_locator):

        self.wait.until(ec.presence_of_element_located(page_locator))

    def click(self, element_locator):

        element = self.wait.until(ec.presence_of_element_located(element_locator))
        element.click()

    def close_mainpage_popup(self):

        if ec.presence_of_element_located(LoginPageLocators.GENDER_POPUP):
            self.click(LoginPageLocators.GENDER_POPUP_CLOSE)
            self.wait.until(ec.invisibility_of_element_located(LoginPageLocators.POPUP_OVERLAY))

    def login(self):

        self.driver.get(settings.login_url)
        self.check_page_exist(GlobalLocators.HEADER_LOGO)
        self.close_mainpage_popup()
        self.click(LoginPageLocators.LOGIN_POPUP_BUTTON)
        self.wait.until(ec.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(settings.login_email)
        self.wait.until(ec.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)).send_keys(
            settings.login_password)
        self.click(LoginPageLocators.SUBMIT_BUTTON)
        self.wait.until(ec.invisibility_of_element_located(LoginPageLocators.POPUP_OVERLAY))

    def smooth_scroll_to_bottom(self):

        scroll_animation_time = 25
        self.driver.execute_script(
            "$('html, body').animate({ scrollTop: $('#footer').offset().top }, 25000);")
        time.sleep(scroll_animation_time)

    def scroll_to_top(self):

        element = self.driver.find_element_by_css_selector(GlobalLocators.HEADER_DIV)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def check_image_load(self, image_list):

        for image in image_list:
            image_src = image.get_attribute('src')
            if requests.get(image_src).status_code != 200:
                print image_src + " IS NOT LOADED"

    def check_page_images(self, page_locator, page_image_locators):

        self.click(page_locator)
        self.check_page_exist(GlobalLocators.HEADER_LOGO)
        self.smooth_scroll_to_bottom()
        for i in range(0, len(page_image_locators)):
            page__images = self.driver.find_elements_by_css_selector(page_image_locators[i])
            self.check_image_load(page__images)
        self.scroll_to_top()

    def test_trendyol(self):

        self.login()
        for i in range(0, len(CategoryPageLocators.CATEGORY_PAGES)):
            self.check_page_images(CategoryPageLocators.CATEGORY_PAGES[i],
                                   CategoryPageLocators.CATEGORY_PAGE_IMAGE_LOCATORS)

        self.check_page_images(BoutiquePageLocators.BOUTIQUE_LOCATOR,
                               BoutiquePageLocators.BOUTIQUE_PAGE_IMAGE_LOCATORS)

        self.click(ProductPageLocators.PRODUCT_LOCATOR)
        self.click(ProductPageLocators.DROPDOWN_MENU)
        self.click(ProductPageLocators.SIZE_LOCATOR)
        self.click(ProductPageLocators.BASKET_BUTTON)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
