from selenium import webdriver

class FindByXPathCSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element by CSS")

ff = FindByXPathCSS()
ff.test()