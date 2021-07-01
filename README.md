1. Install `pip install auto-py-to-exe`
2. Build `auto-py-to-exe` 
3. Navigate to `output` folder -> run `main.exe`
4. Create `.env` file with config

ERRORLEVEL:

0. = Программа успешно отработала
1. = Текущий месяц отличается от месяца на сайте
2. = Невозможно прочитать поле в таблице на сайте
3. = Невозможно открыть входной файл
4. = Входной файл с ИНН не найден
5. = Ошибка запроса поиска по базе nalog.ru
6. = Ошибка создания заголовков таблицы в Excel
7. = Ошибка заполнения полей таблицы Excel

.env```
IN_FILE="D:\Git Repo\NalogInnSearch\innall.txt"
OUT_FOLDER="D:\Git Repo\NalogInnSearch\output\"
DEBUG=true
```