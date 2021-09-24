import requests
import lxml.html as html
import datetime
import emoji
import random

HOME_URL = 'https://news.ycombinator.com/'
XPATH_LINK_TO_ARTICLE = '//td[@class="title"]/a/@href'
XPATH_TITLE = '//td[@class="title"]/a/text()'


def random_emoji():
  list_emojis = ["💚","🐍","🚀","🐱‍👤","🏛","🗺","🤣","👌","🐱‍🐉", "🐲", "🐘", "🦘", "🐳", "🧠", "🦾", "💅", "🎈", "📗", "🟨"]
  rand = random.choice(list_emojis)
  return rand

def put_emoji(parse_home):
  def wrapper(*args, **kwargs):
    parse_home()
    today = datetime.date.today().strftime('%d-%m-%Y')
    with open(f'{today}.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n\t\tThe emoji of today is: {args[0]}\n')
  return wrapper

@put_emoji
def parse_home():
  try:
    response = requests.get(HOME_URL)
    if response.status_code ==200:
      home = response.content.decode("utf-8")
      parsed = html.fromstring(home)
      links_to_articles = parsed.xpath(XPATH_LINK_TO_ARTICLE)
      title_of_articles = parsed.xpath(XPATH_TITLE)
      today = datetime.date.today().strftime('%d-%m-%Y')

      with open(f'{today}.txt', 'w', encoding='utf-8') as f:
        for i in range(0,len(title_of_articles)-1):
          f.write(f'Title description: {title_of_articles[i]}')
          f.write(f'\n\t Link: {links_to_articles[i]}')
          f.write('\n\n')
    else: 
      raise ValueError(f"Error: {response.status_code}")
  except ValueError as ve:
    print(ve)

def run():
  rand=random_emoji()
  parse_home(rand)

if __name__ == '__main__':
  run()