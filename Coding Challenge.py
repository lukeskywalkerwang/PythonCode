import csv
from datetime import *

price_min = input('Minimum Price: ')
price_max = input('Maximum Price: ')
expires_start = input('Earliest Expiration Date (Month/Date/Year): ')
expires_stop = input('Latest Expiration Date (Month/Date/Year): ')

if expires_start != '*':
    m1, d1, y1 = expires_start.split('/')
    expires_start = date(int(y1), int(m1), int(d1))
if expires_stop != '*':
    m2, d2, y2 = expires_stop.split('/')
    expires_stop = date(int(y2), int(m2), int(d2))

csvFile = open('Products.csv','r')
lines = csv.reader(csvFile)
next(lines)     # Skip the header

print('\n{:>4} {:^40} {:^5}  {:^8}'.format('id', 'name', 'price', 'expires'))     # Print Header

for row in lines:
    m, d, y = row[3].split('/')
    if  (price_min == '*' or float(price_min) <= float(row[2])) and \
        (price_max == '*' or float(price_max) >= float(row[2])) and \
        (expires_start == '*' or expires_start <= date(int(y), int(m), int(d))) and \
        (expires_stop == '*' or expires_stop >= date(int(y), int(m), int(d))):
            print('{:>4} {:<40} {:>5.2f}  {:>8}'
                  .format(row[0], row[1], float(row[2]), date(int(y), int(m), int(d)).strftime("%x")))

csvFile.close()

''' Alternative approach is to set min low and max high at no min/max 
if price_min == '*':
    price_min = -10^99

if price_max == '*':
    price_max = 10^99

if expires_start == '*':
    expires_start = '1/1/0001'

if expires_stop == '*':
    expires_stop = '12/31/9999'

if float(price_min) <= float(row[2]) <= float(price_max) and expires_start <= date(int(y), int(m), int(d)) <= expires_stop:
'''
