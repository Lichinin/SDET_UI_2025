import datetime
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from helpers.data_helper import DataHelper
from pages.manager_page import ManagerPage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--url', action='store', default='https://www.globalsqa.com')
    parser.addoption('--log_level', action='store', default="INFO")
    parser.addoption('--browser_version', action='store')


@pytest.fixture(scope='function')
def logger(request):
    log_dir = Path(__file__).parent.parent / 'log'
    log_dir.mkdir(exist_ok=True)
    log_level = request.config.getoption('--log_level')
    browser_name = request.config.getoption('--browser')
    logger = logging.getLogger(request.node.name)
    file_handler = RotatingFileHandler(
        str(log_dir / f'{request.node.name}({browser_name}).log'),
        maxBytes=30000000,
        backupCount=3)
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test %s started at %s' % (request.node.name, datetime.datetime.now()))

    yield logger

    logger.info('===> Test %s finished at %s' % (request.node.name, datetime.datetime.now()))

    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


@pytest.fixture()
def browser(request, logger) -> WebDriver:
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    url = request.config.getoption('--url')

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        # driver.fullscreen_window()
    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(
            'Browser name must be "chrome", "firefox" or "edge"'
        )
    driver.url = url
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s v. %s started" % (browser_name, browser_version))

    yield driver
    driver.quit()


@pytest.fixture()
def manager_page(browser) -> ManagerPage:
    browser.get(f'{browser.url}/angularJs-protractor/BankingProject/#/manager')
    return ManagerPage(browser)


@pytest.fixture()
def setup_customer():
    code = DataHelper.generate_post_code()
    first_name = DataHelper.generate_first_name(code)
    return {'code': code, 'first_name': first_name}
