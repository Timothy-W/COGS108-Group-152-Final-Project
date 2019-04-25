# Webscraper for COGS108 final project
# Author: Timothy Walker
# Date: 25 April 2019
#
# Notes: Links are in the following format;
#
#        https://www.billboard.com/archive/charts/2000/r-b-hip-hop-songs
#
#        For additional genres, add the last directory of the link. For
#        example, the genre of the link above would be 'r-b-hip-hop-songs'.
#

# library imports
from urllib.request import Request, urlopen
import bs4 as bs
import pandas as pd

# Set year and genres to scrape, ending year not inclusive
yearStart = 2000
yearEnd = 2011
genreList = ['r-b-hip-hop-songs', 'rap-song', 'country-songs',
             'alternative-songs', 'hot-mainstream-rock-tracks']


for genre in genreList:

    print('Grabbing genre: ' + genre)

    # Write header
    file = open(genre + ".csv", "w")
    file.write('Year,Title,Artist\n')
    file.close()

    for year in range(yearStart, yearEnd):

        print('year: ' + str(year))

        # Grab html
        req = Request('https://www.billboard.com/archive/charts/' + str(year) + '/' + genre + '/',
                      headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        html = pd.read_html(webpage, header=0)  # dfs is a list of dataframes
        df = html[0]  # df is a pandas datafram

        # Rename columsn, drop dupplicate songs and add year
        df.columns = ['Year', 'Title', 'Artist']
        df.drop_duplicates(subset='Title', inplace=True)
        df['Year'] = year

        # Print to .csv
        df.to_csv(path_or_buf=genre + '.csv',
                  header=False, mode='a', index=False)
