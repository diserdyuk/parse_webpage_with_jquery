import requests
from bs4 import BeautifulSoup


def get_html(url):    # get html code
    user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(d):
    with open('catertrax.csv', 'a') as f:
        order = []
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d) 


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    containers = soup.find('div', class_="testimonial-container").find_all('article')
    for i in containers:
        print(i)


def main():
    url = 'https://catertrax.com/why-catertrax/traxers/'
    get_data(get_html(url))


if __name__ == "__main__":
    main()