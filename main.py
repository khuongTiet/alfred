import requests
from bs4 import BeautifulSoup
import re
from time import sleep

def not_pdf(href):
    return href and not re.compile(".pdf").search(href)

def find_path(url):
    return url.rsplit('/', 1)[0]

def request_download(url):
    r = requests.get(url, allow_redirects=True)
    filename = url.rsplit('/', 1)[1]
    location = './downloads/{}'.format(filename)
    open(location, 'wb').write(r.content)
    return location

def crawl(link):
    stack = find_links(link)
    files = []
    print('Before loop: stack = {}'.format(stack))
    while stack:
        print('start loop: stack = {}'.format(stack))
        current = stack.pop()
        if current[0:4] != 'http':
            current = find_path(target) + '/' + current
        print(current)
        if find_path(current) in link:
            for item in find_links(current):
                if item not in stack:
                    stack.append(item)
                    print('Added {}'.format(item))
            for item in find_files(current):
                if item not in files:
                    files.append(item)
                    print('Added {}'.format(item))
    return files
                

def find_files(target):
    page = requests.get(target, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('a', href=re.compile('.pdf'))

def find_links(target):
    page = requests.get(target, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    return [element['href'] for element in soup.find_all('a', href=not_pdf)]
    

#target = 'http://www.ics.uci.edu/~majumder/CG/cg.htm'
target = 'http://www.ics.uci.edu/~thornton/ics32/Notes/'
downloads = crawl(target)
print(downloads)

"""
for i in downloads:
    link = i['href']
    if link[0:4] != 'http':
        link = find_path(target) + '/' + link
    print("Downloading {}".format(link))
    sleep(2)
    request_download(link)
"""

print("Alfred is done")
