# Парсер для  _[difc.ae](https://www.difc.ae/public-register/)_

Программа собирает все данные о компаниях и сохраняет их в базу данных `MongoDB`

<img src="images/main_photo.png">

## Как установить

Установите Python пакеты из `requirements.txt`:

```bash
pip install -r requirements.txt
```

Заполните переменные в файле `config.py` своими данными для работы.

Запустите скрипт для сбора информации компаний из [Dubai International Financial Centre public registry](https://www.difc.ae/public-register/):
```bash
python start.py
```

### Рекомендации
 В документации _Scrapy_ настоятельно рекомендуется устанавливать его в специальной _виртуальной среде_ 
 во избежание конфликтов с пакетами вашей системы.
 ```bash
python3.8  -m venv scrapy_env
source scrapy_env/bin/activate
```
После активации виртуальной среды можете приступать к установке проекту как было описанно раннее.