
import requests
import yaml

# def read data 
def read_api():
    url = f'https://newsapi.org/v2/everything?q=tesla&from={date}&sortBy=publishedAt&apiKey={key}'
    response = requests.get(url)
    data_api = response.json()
    articles = data_api.get('articles',[])
    return articles

# opening env.yml file and getting data
with open('env.yml','r') as fo:
    conf = yaml.safe_load(fo)
# getting key from env.yml
key = conf.get('api_key')
# getting Current date from env.yml
date = conf.get('date')
read_api()