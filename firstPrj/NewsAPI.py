import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-9-18&to=2023-9-19&sortBy=popularity&language=en&apiKey=fc1af8447bdf4f9c9064318c48a77588')
content = r.json()
#print(type(content))
articles = content['articles']
for article in articles:
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])
#print(content['articles'][0]['title'])