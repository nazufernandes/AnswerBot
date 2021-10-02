import requests
from bs4 import BeautifulSoup

def urlEncode(searchQuery):
    encoded = searchQuery
    utf8 = encoded.replace(' ','+').replace('!','%21').replace('@','%40').replace('(','%28').replace(')','%29').replace('?','%3F')
    return utf8

def find_answers(question):
    page  = requests.get(f'https://vceguide.com/?s={urlEncode(question)}')
    soup = BeautifulSoup(page.content,'html.parser')

    site = soup.find(class_ = 'site-main')
    page = site.find('a', href=True)
    main_page = requests.get(page['href'])
    soup = BeautifulSoup(main_page.content,'html.parser')
    page  = soup.find(class_ = 'entry-content')
    ans = page.find_all('strong')
    print(question)
    for op in ans:
        print(str(op).get_text())

#--Driver Code
questions = []
print("Answers Bot(vceguide.com): {Nazu Fernandes.}")
for no in range(0,5):
    question  = input(f'{no+1}=>> ')
    if question == 'end':
        break
    questions.append(question)
    print('-'*50)

for question in questions:
    print("")
    find_answers(question)
