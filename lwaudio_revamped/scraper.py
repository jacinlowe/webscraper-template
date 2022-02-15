from abc import ABC, abstractmethod
from pathlib import Path


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Scraper(ABC):
    @abstractmethod
    def login(self, email: str, password: str):
        pass

    @abstractmethod
    def run(self):
        """Business logic goes here the scraper code will run here"""
        pass

    @abstractmethod
    def change_url(self, url: str) -> None:
        pass

    @abstractmethod
    def wait_for_class(self, class_name: str) -> None:
        """pauses the driver until the class specified loads

        Args:
            class_name (str): its a class name
        """
        pass

    @abstractmethod
    def wait_for_xpath(self, xpath: str) -> None:
        """Pauses the driver and waits for the xpath to load

        Args:
            xpath (str): the xpath

        Returns:
            None

        Example:
            '//input[@id="login-email"]'

            single quotes then // then the element type [@selector type = "selector name"] end single quote
        """


class SeleniumScraper(Scraper):
    def __init__(self, url: str, headless: bool = True, logging: bool = False) -> None:
        self.url = url
        self.headless = headless
        self.logging = logging
        self.driver = self._start_webdriver()

    def _start_webdriver(self) -> webdriver.Chrome:
        chrome_options = self._chromedriver_options()
        chrome_driver = Path().cwd().joinpath("constants/chromedriver.exe")
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        return driver

    def _chromedriver_options(self) -> webdriver.ChromeOptions:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = self.headless
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--log-level=3")
        if not self.logging:
            chrome_options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )
        return chrome_options

    def get_webpage(self) -> None:
        self.driver.get(self.url)
        self.driver.execute_script("return document.body.innerHTML")

    def change_url(self, url: str) -> None:
        self.url = url
        self.get_webpage()

    def wait_for_class(self, class_name: str) -> None:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )

    def wait_for_xpath(self, xpath: str) -> None:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
