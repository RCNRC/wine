# Новое русское вино

Сайт магазина авторского вина "Новое русское вино". Требует файл с расширением `xlsx` как базу данных о продуктах.

## Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip download --destination-directory DIR -r requirements.txt
```

В директорию проекта поместите excel файл `file.xlsx`, в которм на листе под именем `Лист1` будут храниться данные в следующем формате:
1. 1-ая строка содержит последовательно: "Категория" (букав A), "Название" (букав B), "Сорт" (букав C), "Цена" (букав D), "Картинка" (букав E), "Акция" (букав F).
2. Каждая последующая строка содержит:
   1. под буквой A - строку с категорией вина,
   2. под буквой B - строку с названием вина,
   3. под буквой C - строку с сортом вина,
   4. под буквой D - строку с ценой вина,
   5. под буквой E - строку с местоположением картинки вина в папке `wine/assets`,
   6. под буквой F - строку с акцией для вина,

## Запуск

1. Запустите сайт командой с необязательным параметром `file.xlsx`: `python3 main.py file.xlsx`.
   - Если не установить `file.xlsx`, то по умолчанию данные берутся из файла `wine.xlsx` из той же директории, что и скрипт.
2. Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
