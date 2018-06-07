import unittest
import settings
from locators import *
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains


class TrendyolAutomationTests(unittest.TestCase):

    def setUp(self):

        self.init_driver(settings.desired_driver)
        self.wait = ui.WebDriverWait(self.driver, 10)

    def init_driver(self, desired_driver):

        if desired_driver == 'chrome':
            self.driver = webdriver.Chrome(settings.chrome_driver_path)
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

        time_to_scroll = self.driver.execute_script(
            "var distancetofooter = Math.abs($(document).scrollTop() - $('#footer').offset().top);"
            "var timetoscroll = distancetofooter  + 1000;"
            "$('html, body').animate({ scrollTop: $('#footer').offset().top }, timetoscroll); return timetoscroll;")
        time.sleep(time_to_scroll / 1000)

    def scroll_to_top(self):

        element = self.driver.find_element_by_css_selector(GlobalLocators.HEADER_DIV)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def check_image_load(self, image_list, place_holder_image_path):

        for image in image_list:
            image_src = image.get_attribute('src')
            image_size = self.driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth !='undefined' && arguments[0].naturalWidth > 0",
                image)

            if place_holder_image_path in image_src or image_size is False:
                if image.get_attribute("title") == "":
                    print "ERROR LOADING " + image.find_element_by_xpath("./../../../..").get_attribute("title")
                else:
                    print "ERROR LOADING " + image.get_attribute("title")

    def check_page_images(self, page_locator, page_image_locators, place_holder_images):

        self.click(page_locator)
        self.check_page_exist(GlobalLocators.HEADER_LOGO)
        self.smooth_scroll_to_bottom()
        for i in range(0, len(page_image_locators)):
            page__images = self.driver.find_elements_by_css_selector(page_image_locators[i])
            self.check_image_load(page__images, place_holder_images[i])
        self.scroll_to_top()

    def test_trendyol(self):

        self.login()
        for i in range(0, len(CategoryPageLocators.CATEGORY_PAGES)):
            self.check_page_images(CategoryPageLocators.CATEGORY_PAGES[i],
                                   CategoryPageLocators.CATEGORY_PAGE_IMAGE_LOCATORS,
                                   CategoryPageLocators.CATEGORY_PAGE_PLACE_HOLDER_IMAGE_PATHS)

        self.check_page_images(BoutiquePageLocators.BOUTIQUE_LOCATOR,
                               BoutiquePageLocators.BOUTIQUE_PAGE_IMAGE_LOCATORS,
                               BoutiquePageLocators.BOUTIQUE_PAGE_PLACE_HOLDER_IMAGE_PATH)

        self.click(ProductPageLocators.PRODUCT_LOCATOR)
        self.click(ProductPageLocators.DROPDOWN_MENU)
        self.click(ProductPageLocators.SIZE_LOCATOR)
        self.click(ProductPageLocators.BASKET_BUTTON)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
