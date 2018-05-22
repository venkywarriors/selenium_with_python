"""
@package base

WebDriver Factory class implementation

It reads the configurations and creates a webdriver instance
based on browser and operating system.

This class is used in guibasetestcase class to get the webdriver instance
that can be used by the framework to interact with different browsers on various platforms.
This should not be directly inherited in page classes or test classes

Example:
    wdf = WebDriverFactory()
    wdf.getWebDriverInstance(remote=remote_session)
"""
from base.configreader import ConfigReader
import traceback
from selenium import webdriver
from utilities.driver_session import DriverSession as DS
import utilities.custom_logger as cl

class WebDriverFactory():

    def __init__(self):
        """
        Inits WebDriverFactory class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.cfg = ConfigReader(fileName="testenvironment.ini")
        self.cfg.configRead()
        self.log = cl.customLogger()

    """
        TODO: Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self, remote="No"):
        """
       Get WebDriver Instance based on the browser and operating system configuration

        Required Parameters:
            None

        Optional Parameters:
            remote: Provide 'Yes' to run the code on selenium grid environment

        Returns:
            'WebDriver Instance'
        """
        version = self.getVersion()
        platform = self.getOS()
        desired_caps = {}

        browser = self.getBrowser()
        app_url = self.getAppURL()

        # If running on remote, set grid using the desired capabilities
        if remote.lower() == "yes":
            hub_url = self.getGridHubURL()
            if browser == "iexplorer":
                desired_caps['browserName'] = 'iexplorer'
            elif browser == "firefox":
                desired_caps['browserName'] = 'firefox'
                # desired_caps = webdriver.DesiredCapabilities.FIREFOX
            elif browser == "chrome":
                desired_caps['browserName'] = 'chrome'
            else:
                desired_caps['browserName'] = 'phantomjs'

            desired_caps = self.setVersionAndPlatform(desired_caps, platform, version)

            try:
                self.driver = webdriver.Remote(desired_capabilities=desired_caps,
                                               command_executor=hub_url)
            except BaseException:
                traceback.print_stack()
        # If running on local, desired capabilities is not needed
        else:
            if browser == "iexplorer":
                self.driver = webdriver.Ie()
            elif browser == "firefox":
                self.driver = webdriver.Firefox()
            elif browser == "chrome":
                self.driver = webdriver.Chrome()
            else:
                self.driver = webdriver.PhantomJS()

        self.printConfiguration()
        # Setting Driver Implicit Time out for An Element
        self.driver.implicitly_wait(3)
        # Maximize the window
        self.driver.maximize_window()
        # Loading browser with App URL
        self.driver.get(app_url)
        DS.setDriver(self.driver)
        return self.driver

    def setVersionAndPlatform(self, desiredCap, platform, version):
        """
        Set browser version and platform (operating system)

        Required Parameters:
            desiredCap: Desired Capabilities to append platform and version
            platform: Operating System where tests are running
            version: Browser where tests are running

        Optional Parameters:
            None

        Returns:
            'WebDriver Instance'
        """
        if "MAC" == platform:
            desiredCap['platform'] = "MAC"
        elif "LINUX" == platform:
            desiredCap['platform'] = "LINUX"
        elif "WINDOWS" == platform:
            desiredCap['platform'] = "WINDOWS"
        if version:
            desiredCap['version'] = version
        return desiredCap

    def printConfiguration(self):
        """
        Prints configuration to the console before tests start

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.log.info("********** Execution Configuration Start **********")
        self.log.info("Grid Host or URL : " + str(self.getGridHubURL()))
        self.log.info("App URL          : " + str(self.getAppURL()))
        self.log.info("Browser Type     : " + str(self.getBrowser()))
        self.log.info("Browser Version  : " + str(self.getVersion()))
        self.log.info("Platform (OS)    : " + str(self.getOS()))
        self.log.info("********** Execution Configuration End **********")
        print()

    def getGridHubURL(self):
        """
        Get the grid hub url

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        grid_hub =  self.cfg.getConfiguration("Grid", "hub")
        grid_port = self.cfg.getConfiguration("Grid", "hubport")
        return "http://" + grid_hub + ":" + grid_port + "/wd/hub"

    def getAppURL(self):
        """Get the app url

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        app_url =  self.cfg.getConfiguration("Array", "url")
        return app_url

    def getBrowser(self):
        """Get the browser name

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        browser =  self.cfg.getConfiguration("Platform", "browser")
        return browser

    def getVersion(self):
        """Get the browser version

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        version =  self.cfg.getConfiguration("Platform", "version")
        return version

    def getOS(self):
        """Get the operating system

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        # self.log.info("*#" * 30)
        # self.log.info(dir(self))
        # self.log.info("*#" * 30)
        # platform = self.gspec.get_platform()
        # operatingSystem = platform["os"]
        operatingSystem =  self.cfg.getConfiguration("Platform", "os")
        return operatingSystem

    def username(self):
        """Get the username

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        username =  self.cfg.getConfiguration("Array", "user")
        return username

    def password(self):
        """Get the password

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        password =  self.cfg.getConfiguration("Array", "password")
        return password

    def isArrayVirtual(self):
        """Get if array is virtual

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        isVirtual = self.cfg.getConfiguration("Array", "virtual")
        return isVirtual