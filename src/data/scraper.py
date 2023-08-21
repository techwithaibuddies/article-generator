import os
import csv
import datetime
import requests
from bs4 import BeautifulSoup


url_links = ['https://www.thehindu.com/business/',
             'https://www.thehindu.com/business/agri-business/',
             'https://www.thehindu.com/business/Economy/',
             'https://www.thehindu.com/business/Industry/',
             'https://www.thehindu.com/business/markets/',
             'https://www.thehindu.com/business/budget/',
             'https://www.thehindu.com/sci-tech/',
             'https://www.thehindu.com/sci-tech/science/',
             'https://www.thehindu.com/sci-tech/technology/',
             'https://www.thehindu.com/sci-tech/health/',
             'https://www.thehindu.com/sci-tech/agriculture/',
             'https://www.thehindu.com/sci-tech/energy-and-environment/',
             'https://www.thehindu.com/sci-tech/technology/gadgets/',
             'https://www.thehindu.com/sci-tech/technology/internet/',
             'https://www.thehindu.com/news/',
             'https://www.thehindu.com/news/national/',
             'https://www.thehindu.com/news/international/',
             'https://www.thehindu.com/news/states/',
             'https://www.thehindu.com/news/cities/',
             'https://www.thehindu.com/society/',
             'https://www.thehindu.com/life-and-style/',
             'https://www.thehindu.com/life-and-style/fashion/',
             'https://www.thehindu.com/life-and-style/fitness/',
             'https://www.thehindu.com/life-and-style/food/',
             'https://www.thehindu.com/life-and-style/homes-and-gardens/',
             'https://www.thehindu.com/life-and-style/luxury/',
             'https://www.thehindu.com/life-and-style/motoring/',
             'https://www.thehindu.com/life-and-style/travel/',
             'https://www.thehindu.com/data/',
             'https://www.thehindu.com/society/faith/',
             'https://www.thehindu.com/society/history-and-culture/',
             'https://www.thehindu.com/opinion/editorial/',
             'https://www.thehindu.com/opinion/columns/',
             'https://www.thehindu.com/opinion/interview/',
             'https://www.thehindu.com/books/',
             'https://www.thehindu.com/books/books-reviews/',
             'https://www.thehindu.com/books/books-authors/',
             'https://www.thehindu.com/sport/',
             'https://www.thehindu.com/sport/cricket/',
             'https://www.thehindu.com/sport/football/',
             'https://www.thehindu.com/sport/hockey/',
             'https://www.thehindu.com/sport/tennis/',
             'https://www.thehindu.com/sport/athletics/',
             'https://www.thehindu.com/sport/motorsport/',
             'https://www.thehindu.com/sport/races/',
             'https://www.thehindu.com/sport/other-sports/'
             'https://www.thehindu.com/topic/russia-ukraine-crisis/'
             ]

file_name = 'articles_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
output_directory = os.path.join(os.path.dirname(
    __file__), '/home/prashanth/DS/NLP/article-generator/data/raw')  # Specify the output directory

output_path = os.path.join(output_directory, file_name)

with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Article'])

    for url in url_links:
        try:
            response = requests.get(url, allow_redirects=True)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            article_links = [link['href'] for link in soup.find_all(
                'a', href=True) if 'article' in link['href']]

            for link in article_links:
                try:
                    article_response = requests.get(link, allow_redirects=True)
                    article_response.raise_for_status()
                    article_soup = BeautifulSoup(
                        article_response.content, 'html.parser')

                    article_title = article_soup.find('h1', class_='title').text.strip(
                    ) if article_soup.find('h1', class_='title') else 'N/A'
                    article_body = article_soup.find(
                        'div', class_='articlebodycontent')
                    article_text = '\n'.join(
                        [p.text for p in article_body.find_all('p')]) if article_body else 'N/A'

                    writer.writerow([article_title, article_text])

                except requests.exceptions.RequestException as e:
                    print(f"Error fetching article from {link}: {e}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")

print("Data has been scraped and saved to:", output_path)
