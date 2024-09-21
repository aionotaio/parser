# Парсер

## Функционал
- Извлекает данные из таблицы
- Периодически обновляет страницу для получения актуальной информации
- Проверяет изменения данных в таблице
- Запись данных в csv-файл (если они изменились)
- Запись логов
- Непрерывная работа с помощью бесконечного цикла

## Запуск

Python version: 3.10+

Installing virtual env: \
`pip install virtualenv` \
`cd <project_dir>` \
`python -m venv venv`


Activating: 
 - Mac/Linux - `source venv/bin/activate` 
 - Windows - `.\venv\Scripts\activate` 

Installing all dependencies: \
`pip install -r requirements.txt`

Run main script: \
`python main.py`

## config.py
- `LOGS_DIR` - директория с лог-файлом
- `LOGS_PATH` - прямой путь к лог-файлу
- `RES_DIR` - директория с результатами
- `RES_PATH` - прямой путь к результатам

- `SLEEP_DELAY` - задержка от первого значения и до второго значения в секундах между повторными запросами к таблице
- `MAX_ATTEMPTS` - кол-во попыток для повторного запроса при ошибке

## Результаты
`logs/logs.txt` - Логи \
`./data.csv` - CSV с записанными данными