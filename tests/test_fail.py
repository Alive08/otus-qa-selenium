def test_pass(driver, base_url):
    driver.get(base_url)
    assert "Your Storage" in driver.title
