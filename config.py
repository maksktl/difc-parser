# Пути до блоков с информацией
COMPANY_OVERVIEW_XPATH = '/html/body/div[1]/div[9]/div[2]/div[1]/div/div/div'
INFORMATION_XPATH = '/html/body/div[1]/div[9]/div[2]/div[2]/div/div'

# Путь до контейнера с полями 'key: value' относительно блока с информацией
FIELDS_XPATH = './div[contains(@class, "row")]'

# Пути до 'key: value' относительно самого контейнера
KEY_XPATH = './div[1]//p//text()'
VALUE_XPATH = './div[2]//p//text()'

# Пути до названия контейнера с данными о компании относительно самого контейнера
TITLES = ['./h5//text()', './h4//text()']

# Значения которые надо менять на null
CONVERT_TO_NULL = ['', 'Not Applic', 'Not Available']

# Сколько максимум компаний нужно спарсить
TOTAL = 1000

# MongoDB settings
USER = 'user'
PASSWORD = 'password'
HOST = 'localhost'
DB_NAME = 'difc'
COLLECTION_NAME = 'companies'