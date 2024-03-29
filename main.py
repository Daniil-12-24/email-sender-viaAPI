import requests as rq
from send_email import email_sender

api_key = '2831be7ab94c48faa0a1ed8c51602fc7'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-12-17' \
      '&sortBy=publishedAt&' \
      'apiKey=2831be7ab94c48faa0a1ed8c51602fc7'

# make request
request = rq.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles
text = ''
for article in content['articles']:
    text = text + article['title'] + '\n' + article['url'] + 2*'\n'

# Transform into UTF-8
text = text.encode('utf-8')

email_sender(text)