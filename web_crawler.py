# Beautiful soup

from multiprocessing import Pool
import bs4 as bs
import random
import requests as req
import string

def random_starting_url():
    # starting 
    # random lower case characters for range of 3
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))

    # url - random url 
    url = ''.join(['http://', starting, '.com'])

    return url

# url = random_starting_url()
# print(url)

# create web spider 
# main task - go to website and spiter web out entire inter web app
# crawling around 

def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

# def get links
def get_links(url):
    try:
        resp = req.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body

        links = [link.get('href') for link in body.find_all('a')]

        links = [handle_local_links(url, link) for link in links]

        links = [str(link.encode('ascii')) for link in links]

        return links

    except TypeError as e:
        print(e)
        print('Got a type error')
        return []
    except IndexError as e:
        print(e)
        print('Not find any useful links')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got not links')
        return []
    except Exception as e:
        print(str(e))
        # log this error 
        return []

def main():
    how_many = 50
    p = Pool(processes = how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]

    # while True:
    #     data = p.map(get_links [link for link in parse_us])
    #     data = [url for url_list in data for url in url_list]

    #     parse_us = data
    #     p.close()
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('urls.txt', 'w') as f:
        f.write(str(data))

if __name__=='__main__':
    main()
