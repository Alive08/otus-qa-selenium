import pytest
from selenium.webdriver.common.by import By
import allure

@allure.epic('The Great Project')
@allure.feature('Internet Test')
@allure.story('Testing sites availability')
@allure.title('Get main page')
@pytest.mark.parametrize('url', ("http://example.com", "http://ya.ru"))
def test_url(driver, url):
    driver.logger.info("open %s", url)

    with allure.step(f'Open {url}'):
        driver.get(url)
    
    with allure.step('Find h1 header'):
        driver.find_element(By.CSS_SELECTOR, "body > div > h1")
        

@allure.epic("My epic", "Another epic")
@allure.feature("My feature", "Another feature", "One more feature")
@allure.story("My story", "Alternative story")
def test_multiple_bdd_label():
     pass