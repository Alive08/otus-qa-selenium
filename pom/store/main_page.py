from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MainPageLocators(BaseLocator):

    URL = ''

    URL_MAIN_PAGE = URL
    TITLE_MAIN_PAGE = "Your Store"
    LOCATOR_SLIDESHOW = Selector(By.CSS_SELECTOR, "#slideshow0")
    LOCATOR_SLIDESHOW_NEXT = Selector(
        By.CSS_SELECTOR, ".slideshow .swiper-button-next")
    LOCATOR_SLIDESHOW_PREV = Selector(
        By.CSS_SELECTOR, ".slideshow .swiper-button-prev")
    LOCATOR_FEATURED = Selector(By.CSS_SELECTOR, "h3")
    LOCATOR_CAROUSEL = Selector(By.CSS_SELECTOR, "#carousel0")


class MainPage(BasePage):

    locator = MainPageLocators

    def click_slideshow_next(self):
        el = self.find_element(self.locator.LOCATOR_SLIDESHOW_NEXT)
        hover = ActionChains(self.driver).move_to_element(el).pause(0.5).click(el)
        hover.perform()

    def click_slideshow_prev(self):
        el = self.find_element(self.locator.LOCATOR_SLIDESHOW_PREV)
        hover = ActionChains(self.driver).move_to_element(el).pause(0.5).click(el)
        hover.perform()

    def click_slideshow(self):
        el = self.find_element(self.locator.LOCATOR_SLIDESHOW)
        hover = ActionChains(self.driver).move_to_element(el).click(el)
        hover.perform()


if __name__ == '__main__':

    print(MainPage.locator.locators)
