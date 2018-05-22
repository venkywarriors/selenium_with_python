from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")

ff = FindByIdName()
ff.test()