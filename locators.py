from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_POPUP_BUTTON = (By.CSS_SELECTOR, '.login-register-button-container')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#loginForm #email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#loginForm #password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#loginForm #loginSubmit')
    GENDER_POPUP = (By.CSS_SELECTOR, '.homepage-popup')
    GENDER_POPUP_CLOSE = (By.CSS_SELECTOR, 'a.fancybox-item.fancybox-close')
    POPUP_OVERLAY = (By.CSS_SELECTOR, '.fancybox-overlay')


class CategoryPageLocators(object):
    CATEGORY_PAGES = [(By.CSS_SELECTOR, '#item2'), (By.CSS_SELECTOR, '#item3'), (By.CSS_SELECTOR, '#item4'),
                      (By.CSS_SELECTOR, '#item5'), (By.CSS_SELECTOR, '#item6'), (By.CSS_SELECTOR, '#item7'),
                      (By.CSS_SELECTOR, '#item8'), (By.CSS_SELECTOR, '#item9'), (By.CSS_SELECTOR, '#item10')]

    CATEGORY_PAGE_IMAGE_LOCATORS = ['.bigBoutiqueImage', '.littleBoutiqueImage']
    CATEGORY_PAGE_PLACE_HOLDER_IMAGE_PATHS = ['bbph.png', 'lbph.jpg']


class BoutiquePageLocators(object):
    BOUTIQUE_PAGE_IMAGE_LOCATORS = ['.prc-picture']
    BOUTIQUE_LOCATOR = (By.CSS_SELECTOR, '.butik-large-image')
    BOUTIQUE_PAGE_PLACE_HOLDER_IMAGE_PATH = ['defaultBoutiquePlaceholderWithoutBorder.jpg']


class ProductPageLocators(object):
    PRODUCT_LOCATOR = (By.CSS_SELECTOR, '.prc-picture')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '.variant-picker-button')
    SIZE_LOCATOR = (By.CSS_SELECTOR, '#mCSB_1 > div.mCSB_container > li:nth-child(3) > a')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.add-to-basket-text')


class GlobalLocators(object):
    HEADER_LOGO = (By.CSS_SELECTOR, '#logo')
    HEADER_DIV = '.header'
