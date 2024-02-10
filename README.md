# Web Automation and Webscraping with Selenium

## Description

This project is a comprehensive toolkit designed to facilitate browser automation and webscraping tasks using Selenium WebDriver. It includes the `Connector` and `Operations` classes that provide a wide range of functionalities for interacting with websites, such as opening webpages, clicking buttons, inputting text, scrolling through pages, and retrieving element information.

The primary aim of this project is to simplify and streamline the process of automating browser tasks and scraping data from websites, thereby making these tasks more accessible and efficient.

## Locator Dictionary

This project uses a dictionary to map string keys to Selenium's `By` locator types. This dictionary is defined in the `locator_dict.py` file as follows:



```python
from selenium.webdriver.common.by import By

LOCATOR_DICT = {
    "xpath": By.XPATH,
    "id": By.ID,
    "class_name": By.CLASS_NAME,
    "css_selector": By.CSS_SELECTOR,
    "tag_name": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "name": By.NAME,
}
```

## Installation

1. Install the required packages:
```bash
pip install selenium
```
2. Download ChromeDriver compatible with your version of Google Chrome.
3. Clone the repository:
    git clone https://github.com/Markowian22/WEB_SCRAPER.git
4. Navigate to the project directory:
    cd WEB_SCRPAER
5. Install the package:
    pip install .



## Usage
After installing the package, you can import it in your Python script:
```python
from operations import Operations

# Create an instance of the Operations class
operations = Operations("https://www.example.com")

# Open the webpage
operations.open_web()

# Click a button on the webpage
operations.click_on_button("//button[@id='submit']")

# Input text into a field on the webpage
operations.send_keys("Hello, World!", "input_field")

# Press ENTER in a field on the webpage
operations.click_ENTER("input_field")

# Retrieve text from an element on the webpage
text = operations.get_text_from_element("//div[@class='content']")

# Retrieve all elements of a specified type on the webpage
elements = operations.get_all("//div[@class='content']")

# Retrieve one element of a specified type on the webpage
element = operations.get_one_element("//div[@class='content']")

# Scroll the webpage to the last element of a specified type
operations.scroll_to_last_element("//div[@class='content']")

# Scroll the webpage to a specified element
operations.scroll_to_element("//div[@class='content']")

# Scroll the webpage to the bottom
operations.scroll_to_down_page()

# Wait until the number of 'div' elements on the webpage stops increasing
operations.wait_for_all_element_on_website()

# Close the Chrome WebDriver and the associated webpage
operations.close_web()
```

