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

## Requirements

- Python 3.7+
- Selenium WebDriver
- ChromeDriver

## Installation

1. Install Python 3.7 or newer.
2. Install Selenium WebDriver using pip: `pip install selenium`.
3. Download the latest version of ChromeDriver from the official website and install it according to the instructions.

## Usage

1. Import the `Connector` and `Operations` classes from this project.
2. Create an instance of the `Operations` class, passing the URL of the website you want to interact with.
3. Use the methods of the `Operations` class to interact with the website.

## Example

```python
from connector import Connector
from operations import Operations

# Create an instance of the Operations class
ops = Operations("https://www.example.com")

# Open the webpage
ops.open_web()

# Click a button on the webpage
ops.click_on_button("//button[@id='my-button']")

# Close the webpage
ops.close_web()
