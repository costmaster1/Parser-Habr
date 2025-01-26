# Импортируем модули
import requests
from bs4 import BeautifulSoup
from time import sleep

# Имитируем подключение через браузер Mozilla на Windows
st_useragent = "Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
st_accept = "text/html"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

for count in range(1, 6):
 sleep(3)
 # Создаем сессию
 url = f"https://habr.com/ru/flows/develop/articles/page{count}"

 # Отправим GET()-запрос на сайт и сохраним полученное в переменную 'page':
 page = requests.get(url, headers)

# Проверим статус запроса
 print("Статус запроса =", page.status_code)

 # Создаем объект BeautifulSoup c параметром 'lxml'
 soup = BeautifulSoup(page.text, 'lxml')

 # Находим все статьи с классом "tm-articles-list__item" и сохраняем их в переменной articles
 articles = soup.find_all("article", class_="tm-articles-list__item")

 # Выводим заголовки статей и ссылки на них:
 for article in articles:
    url_articles = "https://habr.com" + article.find("a", class_="tm-title__link").get("href")
   
    print(url_articles + "\n\n")





 
  


   


   
   
   
    


    




 





  
