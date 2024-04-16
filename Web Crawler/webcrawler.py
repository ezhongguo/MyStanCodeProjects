"""
File: webcrawler.py
Name: Eva
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tables = soup.find_all('table', {'class': 't-stripe'})
        total_male_rank = 0
        total_female_rank = 0

        for table in tables:
            tags = table.find_all('tbody')
            for tag in tags:
                # Split the text content and substring only the first 1000 data
                text = tag.text.split()[:1000]
                for i in range(2, len(text), 5):
                    # Remove commas and convert it to an integer
                    male_rank = "".join(text[i].split(','))
                    total_male_rank += int(male_rank)
                for i in range(4, len(text), 5):
                    # Remove commas and convert it to an integer
                    female_rank = "".join(text[i].split(','))
                    total_female_rank += int(female_rank)
                print('Male Number: '+str(total_male_rank))
                print('Female Number: ' + str(total_female_rank))


if __name__ == '__main__':
    main()
