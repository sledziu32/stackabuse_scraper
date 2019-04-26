import requests
from bs4 import BeautifulSoup

core_url = "https://stackabuse.com"

page_num = str(1)
tags = ["python", "java", "node", "javascript", "unix", "linux", "git"]

for tag in tags:
    print(tag)
    scraped_SA = []
    for page_num in range(1, 40):
        page_num = str(page_num)
        result = requests.get(f'https://stackabuse.com/tag/{tag}/page/{page_num}/')
        print(result)
        if result.status_code == requests.codes.ok:
            page = result.text
            soup = BeautifulSoup(page, 'html.parser')  
            articles = soup.find_all('h2', class_='post-title') 
            for article in articles:
                title = article.find('a').get_text()
                link = article.find('a')["href"]
                long_link = "".join([core_url, link])
                scraped_SA.append([title, long_link])
        else:
            pass
    print(len(scraped_SA))
    message = f"""<H3>list of {tag} articles on <a href="{core_url}">StackAbuse</a></h3>"""
    link_list = [f'<li><a href="{scraped_SA[i][1]}">{scraped_SA[i][0]}</a></li>' for i in range(len(scraped_SA))]
    _list = "\n".join(link_list)
    new_page = f"""<html><head></head><body>{message}<ol>{_list}</ol></body></html>"""
    f = open(f'SA_{tag}_links.html','w')
    f.write(new_page)
    f.close()

