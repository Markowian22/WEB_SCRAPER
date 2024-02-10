import logging

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locator_dict import LOCATOR_DICT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# LOCATOR_DICT = {
#     "xpath": By.XPATH,
#     "id": By.ID,
#     "class_name": By.CLASS_NAME,
#     "css_selector": By.CSS_SELECTOR,
#     "tag_name": By.TAG_NAME,
#     "link_text": By.LINK_TEXT,
#     "name": By.NAME,
# }


class Connector:
    """
    The Connector class provides a foundation for interacting with a webpage using Selenium WebDriver.
    """

    def __init__(self, url_link):
        """
        Initializes an instance of the Connector class.

        Parameters:
        url_link (str): The URL of the webpage to interact with.
        """
        self.url_link = url_link
        self.chrome_options = self._set_driver_options()
        self.driver = self._create_driver()

    def _set_driver_options(self):
        """
        Configures the options for the Chrome WebDriver.

        Returns:
        Options: A set of options for the Chrome WebDriver.
        """
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        self.chrome_options.add_experimental_option("useAutomationExtension", True)
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        return self.chrome_options

    def _create_driver(self):
        """
        Creates an instance of the Chrome WebDriver with the configured options.

        Returns:
        WebDriver: An instance of the Chrome WebDriver, or None if an error occurred.
        """
        try:
            return webdriver.Chrome(options=self.chrome_options)
        except WebDriverException as e:
            logger.error(f"Error while creating an instance of webdriver.Chrome: {e}")
            return None

    def open_web(self):
        """
        Opens the webpage specified by the URL link in the Chrome WebDriver.
        """
        if self.driver is not None:
            try:
                self.driver.get(self.url_link)
                self.driver.set_page_load_timeout(10)
                self.driver.implicitly_wait(10)
            except WebDriverException as e:
                logger.error(f"Error while opening the webpage: {e}")

    def switch_to_frame(self, frame_index=0):
        """
        Switches the context of the WebDriver to a specified frame on the webpage.

        Parameters:
        frame_index (int): The index of the frame to switch to. Default is 0.
        """
        if self.driver is not None:
            try:
                self.driver.switch_to.frame(frame_index)
            except NoSuchElementException as e:
                logger.error(f"Error while switching to frame: {e}")

    def close_web(self):
        """
        Closes the Chrome WebDriver and the associated webpage.
        """
        if self.driver is not None:
            try:
                self.driver.quit()
            except WebDriverException as e:
                logger.error(f"Error while closing the browser: {e}")


class Operations(Connector):
    """
    The Operations class extends the Connector class and provides methods for interacting with a webpage.
    """

    def __init__(self, url_link):
        """
        Initializes an instance of the Operations class.

        Parameters:
        url_link (str): The URL of the webpage to interact with.
        """
        super().__init__(url_link)
        self.elements = None
        self.lista = []

    def click_on_button(self, element, locator_type="xpath"):
        """
        Initiates a click event on a specified button on the webpage.

        Parameters:
        element (str): The locator of the button element.
        locator_type (str): The type of the locator. Default is "xpath".
        """
        by = LOCATOR_DICT[locator_type]
        if self.driver is not None:
            try:
                button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((by, element))
                )
                button.click()
            except TimeoutException as e:
                logger.error(f"Error while clicking the button: {e}")

    def send_keys(self, text, element_name, locator_type="id"):
        """
        Inputs a specified text into a specified field on the webpage.

        Parameters:
        text (str): The text to be inputted.
        element_name (str): The locator of the field element.
        locator_type (str): The type of the locator. Default is "id".
        """
        if self.driver is not None:
            try:
                by = LOCATOR_DICT[locator_type]
                field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((by, element_name))
                )
                field.send_keys(text)
            except Exception as e:
                print(f"Błąd podczas wpisywania tekstu: {e}")

    def click_ENTER(self, element_name, locator_type="id"):
        """
        Simulates the pressing of the ENTER key in a specified field on the webpage.

        Parameters:
        element_name (str): The locator of the field element.
        locator_type (str): The type of the locator. Default is "id".
        """
        by = LOCATOR_DICT[locator_type]
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((by, element_name))
            ).send_keys(Keys.RETURN)
        except TimeoutException as e:
            logger.error(f"Error while pressing ENTER: {e}")

    def get_text_from_element(self, element, locator_type="xpath"):
        """
        Retrieves the text content of a specified element on the webpage.

        Parameters:
        element (str): The locator of the element.
        locator_type (str): The type of the locator. Default is "xpath".

        Returns:
        list: A list of text content from the specified element.
        """

        if self.driver is not None:
            try:
                by = LOCATOR_DICT[locator_type]
                elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((by, element))
                )
                for text in elements:
                    self.lista.append(text.text)
                return self.lista
            except TimeoutException as e:
                logger.error(f"Error while retrieving text from element: {e}")

    def go_back(self):
        """
        Navigates the webpage back to the previous page.
        """
        if self.driver is not None:
            try:
                self.driver.back()
            except Exception as e:
                logger.error(f"Error while navigating back: {e}")

    def get_all(self, element: str, locator_type="xpath"):
        """
        Retrieves all elements of a specified type on the webpage.

        Parameters:
        element (str): The locator of the element.
        locator_type (str): The type of the locator. Default is "xpath".

        Returns:
        list: A list of all elements of the specified type.
        """
        by = LOCATOR_DICT[locator_type]
        try:
            elements = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((by, element))
            )
            return elements
        except TimeoutException as e:
            logger.error(f"Error while retrieving all elements: {e}")

    def get_one_element(self, element: str, locator_type="xpath"):
        """
        Retrieves one element of a specified type on the webpage.

        Parameters:
        element (str): The locator of the element.
        locator_type (str): The type of the locator. Default is "xpath".

        Returns:
        WebElement: The first matched element of the specified type.
        """
        by = LOCATOR_DICT[locator_type]
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((by, element))
            )
            return element
        except TimeoutException as e:
            logger.error(f"Error while retrieving one element: {e}")

    def scroll_to_last_element(self, element: str, locator_type="xpath"):
        """
        Scrolls the webpage to the last element of a specified type.

        Parameters:
        element (str): The locator of the element.
        locator_type (str): The type of the locator. Default is "xpath".
        """
        by = LOCATOR_DICT[locator_type]
        try:
            while True:
                try:
                    # Try to find the element
                    elements = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((by, element))
                    )
                    index = len(elements)

                except TimeoutException:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(elements[index - 1]).perform()
                    break

        except Exception as e:
            logger.error(f"Error while scrolling to element: {e}")

    def scroll_to_element(self, element: str, locator_type="xpath"):
        """
        Scrolls the webpage to a specified element.

        Parameters:
        element (str): The locator of the element.
        locator_type (str): The type of the locator. Default is "xpath".
        """
        by = LOCATOR_DICT[locator_type]
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((by, element))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except NoSuchElementException as e:
            logger.error(f"Error while scrolling to element: {e}")

    def scroll_to_down_page(self):
        """
        Scrolls the webpage to the bottom of the page.
        """
        try:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
        except Exception as e:
            logger.error(f"Error while scrolling to bottom of page: {e}")

    def wait_for_all_element_on_website(self):
        """
        Waits until the number of 'div' elements on the webpage stops increasing.
        """
        old_len = 0
        while True:
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda driver: len(driver.find_elements(By.TAG_NAME, "div"))
                    != old_len
                )
                old_len = len(self.driver.find_elements(By.TAG_NAME, "div"))
            except TimeoutException:
                break
            except Exception as e:
                logger.error(f"Error while waiting for all elements on website: {e}")
                break

    def sprawdz_element(self, element: str, locator_type="xpath"):
        by = LOCATOR_DICT[locator_type]
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((by, element))
            )
            return element.is_displayed()
        except Exception as e:
            logger.error(f"The element is not visible on the page: {e}")
