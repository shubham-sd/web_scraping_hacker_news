# Import the packages
import requests
from bs4 import BeautifulSoup
import pprint

# Request the url
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select('.storylink')
subtext = soup.select('.subtext')

# Creating a fuction to sort stories by votes decending order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

# Define a fucntion to get news
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))