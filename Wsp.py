import requests
from bs4 import BeautifulSoup

ratings = []


html = requests.get("https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=JHQ870E5P6TMC8PKBG1W&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17")
soup = BeautifulSoup (html.content, "html.parser")

star = soup.find_all('div', class_ = 'inline-block ratings-imdb-rating')

for i in star :
    ratings.append (i.text.replace('\n',''))

    print(ratings)

directros_list =[]
actor_list =[]

main_details = soup.find_all('div' ,class_="lister-item-content")


for movie in main_details:

    # names= main_details[0].find_all('p')[2].text
    names = movie.find_all('p')[2].text

    # directros_list.append(names)

    names = names.split('|')
    directros_list.append(names[0])
    actor_list.append(names[1])

print(directros_list[0])
print(actor_list[0])




