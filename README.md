# SDET_UI_2025
[![Run Tests](https://github.com/Lichinin/SDET_UI_2025/actions/workflows/main.yml/badge.svg)](https://github.com/Lichinin/SDET_UI_2025/actions/workflows/main.yml)

**Автор:** Виталий Личинин  
**Репозиторий:** [GitHub](https://github.com/Lichinin/sdet_practicum_lichinin)

## Оглавление
1. [Цели проекта](#цели-проекта)
2. [Используемые технологии](#используемые-технологии)
3. [Структура проекта](#структура-проекта)
   - [Описание папок](#описание-папок)
   - [Ключевые файлы](#ключевые-файлы)
4. [Запуск проекта](#запуск-проекта)
   - [Базовый запуск](#базовые-команды)
   - [Дополнительные параметры](#дополнительные-параметры-запуска)
5. [Результаты тестирования](#результат-выполнения-тестов)
6. [Логирование](#примеры-логов)
7. [Allure отчеты](#примеры-отчетности-allure)

## Цели проекта
- Создание и автоматизация UI-тестов для веб-ресурса
- Реализация паттерна Page Object Model
- Интеграция Allure для генерации отчетов
- Настройка логирования критически важных операций
- Реализация параллельного запуска тестов
- Настройка CI/CD через GitHub Actions

## Используемые технологии

| Компонент         | Версия    | Назначение                          |
|-------------------|-----------|-------------------------------------|
| Python            | 3.10+     | Базовый язык проекта                |
| pytest            | 8.3.5     | Фреймворк для тестирования          |
| selenium          | 4.29.0    | Взаимодействие с браузером          |
| allure-pytest     | 2.13.5    | Интеграция с Allure                 |
| Faker             | 37.1.0    | Генерация тестовых данных           |
| pytest-xdist      | 3.6.1     | Параллельный запуск тестов          |

## Структура проекта

```
SDET_UI_2025                                                                       
├─ allure-results                                                                  
├─ constants                                                                       
│  └─ constants.py                                                                 
├─ helpers                                                                         
│  ├─ assertion_helper.py                                                          
│  └─ data_helper.py                                                               
├─ locators                                                                        
│  └─ locators.py                                                                  
├─ log                                                                             
├─ pages                                                                           
│  ├─ base_page.py                                                                 
│  └─ manager_page.py                                                              
├─ testcases                                                                       
│  ├─ id1_create_customer.md                                                       
│  ├─ id2_sort_customers_by_name.md                                                
│  └─ id3_delete_customer.md                                                       
├─ tests                                                                           
│  ├─ test_ui                                                                      
│  │  └─ test_manager_page.py                                                      
│  └─ conftest.py                                                                  
├─ pytest.ini                                                                      
├─ README.md                                                                       
└─ requirements.txt    

```

### Описание папок
- **allure-results** - JSON-файлы для генерации Allure отчетов
- **constants** - константы проекта
- **helpers** - вспомогательные модули
- **locators** - CSS/XPath локаторы элементов
- **log** - логи выполнения тестов
- **pages** - Page Object модели
- **testcases** - документация тест-кейсов
- **tests** - тестовые сценарии

### Ключевые файлы
- **base_page.py** - базовый класс страницы
- **manager_page.py** - страница менеджера банка
- **conftest.py** - фикстуры pytest
- **pytest.ini** - конфигурация тестов
- **requirements.txt** - зависимости

## Запуск проекта

### Базовые команды
```bash
git clone https://github.com/Lichinin/SDET_UI_2025.git
cd SDET_UI_2025
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
pytest
```

### Дополнительные параметры запуска:
```
pytest --browser=firefox --browser_version=125 -n 3 --log_level=DEBUG
```
| Параметр          | Описание                              | Значения по умолчанию      |
|-------------------|---------------------------------------|----------------------------|
| `--browser`       | Браузер для тестов (chrome, firefox, edge)                    | `chrome`                   |
| `--url`           | URL тестируемого приложения           | `https://www.globalsqa.com`|
| `--browser_version` | Версия браузера                     | последняя стабильная       |
| `--log_level`     | Уровень логирования                   | `INFO`                     |
| `-n`              | Количество потоков                    | `3`                        |


### Результат выполнения тестов.
* __Запуск тестов без параметров:__
pytest
```
$ pytest
========================================================================== test session starts ==========================================================================
platform win32 -- Python 3.10.6, pytest-8.1.1, pluggy-1.4.0 -- C:\Users\Lichi\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: E:\Dev\SDET_UI_2025
configfile: pytest.ini
plugins: allure-pytest-2.13.5, Faker-25.0.0, xdist-3.6.1
3 workers [3 items]     
scheduling tests via LoadScheduling

tests/test_ui/test_manager_page.py::test_customer_add 
tests/test_ui/test_manager_page.py::test_customer_delete        
tests/test_ui/test_manager_page.py::test_customers_sort_by_name 
DevTools listening on ws://127.0.0.1:51504/devtools/browser/f11f69c8-b116-46bd-9c34-62ece64c9ded

DevTools listening on ws://127.0.0.1:51505/devtools/browser/947d8eb5-880a-427e-85ad-44cdc1bc1235

DevTools listening on ws://127.0.0.1:51506/devtools/browser/0843a626-8deb-4e48-a851-d6dd6da34ca7

[gw2] [100%] PASSED tests/test_ui/test_manager_page.py::test_customer_delete
[gw1] [ 66%] PASSED tests/test_ui/test_manager_page.py::test_customers_sort_by_name 
[gw0] [100%] PASSED tests/test_ui/test_manager_page.py::test_customer_add
========================================================================== 3 passed in 41.07s ===========================================================================

```

* __Запуск тестов с параметрами:__
$ pytest --browser='firefox' --browser_version='125'
```
========================================================================== test session starts ==========================================================================
platform win32 -- Python 3.10.6, pytest-8.1.1, pluggy-1.4.0 -- C:\Users\Lichi\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: E:\Dev\SDET_UI_2025
configfile: pytest.ini
plugins: allure-pytest-2.13.5, Faker-25.0.0, xdist-3.6.1
3 workers [3 items]     
scheduling tests via LoadScheduling

tests/test_ui/test_manager_page.py::test_customer_add
tests/test_ui/test_manager_page.py::test_customer_delete        
tests/test_ui/test_manager_page.py::test_customers_sort_by_name 
[gw1] [ 33%] PASSED tests/test_ui/test_manager_page.py::test_customers_sort_by_name 
[gw2] [ 66%] PASSED tests/test_ui/test_manager_page.py::test_customer_delete 
[gw0] [100%] PASSED tests/test_ui/test_manager_page.py::test_customer_add 

========================================================================== 3 passed in 25.87s ===========================================================================
```

### Примеры логов.

test_customer_add(chrome).log
```
INFO ===> Test test_customer_add started at 2025-03-28 00:33:46.553902
INFO Browser chrome v. None started
INFO * Get element "('css selector', 'button[ng-click="addCust()"]')"
INFO * Get element "('css selector', 'input[ng-model="fName"]')"
INFO * Get element "('css selector', 'input[ng-model="lName"]')"
INFO * Get element "('css selector', 'input[ng-model="postCd"]')"
INFO * Get element "('css selector', 'button[type="submit"]')"
INFO * Check assertion
INFO *** Test completed successful ***
INFO * Get element "('css selector', 'button[ng-click="showCust()"]')"
INFO * Get element "('css selector', 'input[ng-model="searchCustomer"]')"
INFO * Get element "('xpath', '//tr[contains(@class, "ng-scope") and .//td[text()="lilhn"]]//button[text()="Delete"]')"
INFO ===> Test test_customer_add finished at 2025-03-28 00:34:02.356124
```
test_customers_sort_by_name(firefox).log
```
INFO ===> Test test_customers_sort_by_name started at 2025-03-28 00:37:43.765269
INFO Browser firefox v. 125 started
INFO * Get element "('css selector', 'button[ng-click="showCust()"]')"
INFO * Get element "('css selector', 'a[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]')"
INFO * Get element "('css selector', 'a[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]')"
INFO * Get elements ('css selector', 'tr.ng-scope td:nth-child(1)')
INFO * Check assertion
INFO *** Test completed successful ***
INFO ===> Test test_customers_sort_by_name finished at 2025-03-28 00:38:02.276336
```

### Примеры отчетности Allure.
* Summary по тестам:

* Тесткейсы:

* Пример отчета по тесткейсу:
