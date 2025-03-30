from pathlib import Path


class Timeouts:
    ELEMENT_VISIBILITY = 3


class Urls:
    BASE_URL = 'https://www.globalsqa.com'
    MANAGER_ENDPOINT_URL = '/angularJs-protractor/BankingProject/#/manager'


class Pathes:
    LOG_DIR = Path(__file__).parent / 'log'
