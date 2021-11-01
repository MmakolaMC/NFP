import argparse
from functions import dates, get_data, modify_data

parser = argparse.ArgumentParser(description = 'Retrieve and plot the NFP and unemployment data')

parser.add_argument('---year', type=int, dest='year', help='Year to be parsed into Fred to retrieve data',
                    default=input(int()))
parser.add_argument('---month', type=int, dest='month', help='Month to be parsed into Fred to retrieve data',
                    default=input(int()))
parser.add_argument('---date', type=int, dest='date', help='Date to be parsed into Fred to retrieve data',
                    default=input(int))

period = parser.parse_args()

year = period.year
month = period.month
date = period.date

start, end = dates(year, month, date)
df_employed, df_unemployment = get_data(start, end)
modify_data(df_employed, df_unemployment)

