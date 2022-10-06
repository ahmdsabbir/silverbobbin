from bs4 import BeautifulSoup
import requests


def get_soup(url, parser='lxml'):
    html_texts = requests.get(url).text
    return BeautifulSoup(html_texts, parser)

def tag(soup, tag):
    return soup.find_all(tag)

def element_by_class(soup, element, classname):
    return soup.find(element, class_=classname)

def elements_by_class(soup, element, classname):
    return soup.find_all(element, class_=classname)

def element_by_id(soup, element, id):
    return soup.find(element, id=id)

def next_sib(element):
    return element.find_next_sibling()

def next_sibs(element):
    return element.find_next_siblings()

def prev_sib(element):
    return element.find_previous_sibling()

def prev_sibs(element):
    return element.find_previous_siblings()

# return: list of urls
def get_url_list_from_xml(url):
    souped = get_soup(url, parser='xml')
    urls = []
    loc_tags = souped.find_all('loc')
    for loc in loc_tags:
        urls.append(loc.get_text())
    return urls

