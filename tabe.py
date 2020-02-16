from bs4 import BeautifulSoup
import requests
import time
import csv
page = 1
#ファイル名(xxx.csv)を変える
with open('shibuya2.csv',mode='w', encoding='CP932', errors='replace', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['No', '店名', '場所', 'ジャンル', '評価', '金額', 'URL'])
    print('No', '店名', '場所', 'ジャンル', '評価', '金額')
    while page < 3:
        url = 'https://tabelog.com/tokyo/A1303/A130301/rstLst/{}/?Srt=D&SrtT=rt&sort_mode=1&LstSmoking=0&svd=20190407&svt=1900&svps=2'.format(page)
        result = requests.get(url) #URLを取得
        result.encoding = result.apparent_encoding
        soup = BeautifulSoup(result.text,'html.parser')
        rank_html_no = soup.find_all('p',class_='list-rst__rank-no')
        rank_html_name = soup.find_all('a',class_='list-rst__rst-name-target cpy-rst-name js-ranking-num')
        rank_html_genre = soup.find_all('span',class_='list-rst__area-genre cpy-area-genre')
        rank_html_rate = soup.find_all('span',class_='c-rating__val c-rating__val--strong list-rst__rating-val')
        rank_html_val = soup.find_all('span',class_='c-rating__val list-rst__budget-val cpy-lunch-budget-val')

        for rank_no, rank_name, rank_genre, rank_rate, rank_val in zip(rank_html_no, rank_html_name,rank_html_genre,rank_html_rate,rank_html_val):
            pre_rank_no = rank_no.get_text().strip()
            pre_rank_name = rank_name.get_text()
            pre_rank_genre_list = rank_genre.get_text().split('/')
            pre_rank_place = pre_rank_genre_list[0].strip()
            pre_rank_genre = pre_rank_genre_list[1].strip()
            pre_rank_rate = rank_rate.get_text()
            pre_rank_url = rank_name.get('href')
            pre_rank_price = rank_val.get_text()
            print('{0},"{1}","{2}","{3}","{4}","{5}'.format(pre_rank_no, pre_rank_name,pre_rank_place, pre_rank_genre,pre_rank_rate,pre_rank_price,pre_rank_url))
            f.write('{0},"{1}","{2}","{3}","{4}","{5}","{6}"\n'.format(pre_rank_no, pre_rank_name,pre_rank_place, pre_rank_genre,pre_rank_rate,pre_rank_price,pre_rank_url))
        time.sleep(1)
        page += 1