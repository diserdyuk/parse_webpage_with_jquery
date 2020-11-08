import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # get html code
    user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(d):    # write data to csv
    with open('catertrax.csv', 'a') as f:
        order = ['client', 'position', 'mail', 'phone']
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d) 


def get_containers(html):    # get containers with testimonials
    soup = BeautifulSoup(html, 'lxml')

    containers = soup.find('div', class_="testimonial-container").find_all('article')
    return containers


def get_text(l):    # get info in tags
    for i in l:
        try:
            client = i.find('p', class_='traxer-since').text.strip()
        except:
            client = ''
        try:        
            position = i.find('p', class_='testimonial-author').text.strip()
        except:
            position = ''
        try:
            mail = i.find('li', class_='email').find('a').get('href')
        except:
            mail= ''
        try:
            phone = i.find('li', class_='tel').text
        except:
            phone = ''

        data = {'client': client,    # pack data in dictionary
                'position': position,
                'mail': mail,
                'phone': phone}
        
        write_csv(data)    # write dictionary in csv format


def main():
    
    page = 1
    while True:
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))
        
        cards = get_containers(get_html(url))    # [] or [a, b, c]

        if cards:    # full list  
            get_text(cards)
            page += 1
        else:    # empty list 
            break
            


if __name__ == "__main__":
    main()
