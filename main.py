from lib.soup import get_soup, get_url_list_from_xml, element_by_class, tag
import csv

xml = 'https://silverbobbin.com/post-sitemap.xml'

xml_urls = get_url_list_from_xml(xml)

outlines=''
maintitles=''

tuple = ()
tuples = ('URL', 'Title', 'OUTLINES')

q = ['how', 'what', 'why', 'where', 'when', 'do', 'does', 'is']

with open('outlines.csv', 'r') as fx:
    reader = csv.reader(fx)
    next(reader)
    for i, line in enumerate(reader):
        maintitle = ''
        result = ''
        print(line[0], flush=True)
        try:
            soup = get_soup(line[0])
            title = soup.find('h1')
            title = soup.title.text
            title = title.strip()
            location = title.find('?')
            title = title[0:location+1]
            split = title.split(' ', 1)[0]
            if split.lower() in q:
                h2 = soup.find_all('h2')
                for ind, h in enumerate(h2):
                    if h.text == title:
                        nxt = h.find_next_siblings()
                        for n in nxt:
                            if n.name == 'h3':
                                maintitle += '\n<h3>' + n.text + '</h3>\n'
                            if n.name == 'p':
                                maintitle += '\n<p>' + n.text + '</p>\n'
                            if n.name == 'h2':
                                break
                    elif h.text == 'Conclusion':
                        continue
                    elif h.text == 'Post navigation':
                        continue
                    else:
                        result += str(ind) + '. ' + h.text + '\n'
                with open('silverbobbin_info.csv', 'a',newline="", encoding='utf-8-sig') as res_file:
                    tup = (title, result)
                    writer = csv.writer(res_file)
                    writer.writerow(tup)
                with open('silverbobbin_outlines.csv', 'a',newline="", encoding='utf-8-sig') as main_file:
                    tup = (title, maintitle)
                    writer = csv.writer(main_file)
                    writer.writerow(tup)
            else:
                raise Exception("Desired Article Article not found")
        except Exception:
            print('Error: ' + line[0], flush=True)
            f = open('log.txt', 'a')
            f.write(line[0])
            f.write('\n')
            f.close()

