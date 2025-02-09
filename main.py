# Импортируем модули
import requests
from bs4 import BeautifulSoup
from time import sleep

# Создаем пустой список для хранения ссылок статей
list_artikles_url = []

# Имитируем подключение через браузер Mozilla на Windows
st_useragent = "Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
st_accept = "text/html"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

for count in range(1, 5):
 sleep(1)
 # Создаем сессию
 url = f"https://habr.com/ru/flows/develop/articles/page{count}"

 # Отправим GET()-запрос на сайт и сохраним полученное в переменную 'page':
 page = requests.get(url, headers)

 # Создаем объект BeautifulSoup c параметром 'lxml'
 soup = BeautifulSoup(page.text, 'lxml')

 # Находим все статьи с классом "tm-articles-list__item" и сохраняем их в переменной articles
 articles = soup.find_all("article", class_="tm-articles-list__item")

 # Выводим ссылки на статьи:
 for article in articles:
    url_articles = "https://habr.com" + article.find("a", class_="tm-title__link").get("href")

    # Добавляем ссылку на статью в список
    list_artikles_url.append(url_articles)
   

for url in list_artikles_url:
    # Отправим GET()-запрос на каждую ссылку статья и сохраним полученное в переменную 'page':
    page = requests.get(url, headers)

    # Создаем объект BeautifulSoup c параметром 'lxml'
    soup = BeautifulSoup(page.text, 'lxml')

    # Находим заголовок статьи и сохраняем его в переменной title
    title_articles = soup.find("h1", class_="tm-title tm-title_h1").text
    # Выводим заголовок статьи
    print(title_articles + "\n")

    # Находим ccылку на картинку статьи и сохраняем ее в переменной img_articles_url
    if soup.find("figure", class_="full-width") == None:
        print("Картинки нет")
    else:
        blok_img = soup.find("figure", class_="full-width")
        img_articles_url = blok_img.find("img").get("src")
        # Выводим ссылку на картинку статьи
        print(img_articles_url + "\n")

    # Пауза для демонстрации скорости обработки
    sleep(1)
    # Проверяем статус запроса
    print("Статус запроса =", page.status_code)
    print("-------------------------------------------")
    # Пауза для демонстрации скорости обработки
    sleep(2)

     





 
  


   


   
   
   
    


    




 





  
