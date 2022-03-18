# Web Crawler Exercise

from bs4 import BeautifulSoup
from urllib.request import urlopen

storyname = input("What's the short story path? ")
URLlink = 'https://www.classicshorts.com/stories/' + storyname + '.html'    # Build URL link string

try:
    response = urlopen(URLlink)
    soup = BeautifulSoup(response, 'html.parser')
    atag = soup.findAll('a')

    dictionary = {}
    keylist =[]

    for key in atag:        # Part 1: Search for the keywords in the short story
        if "dictionary" in key.get('href'):
            keylist.append(key.get('href').replace("http://dictionary.reference.com/browse/", ""))

    for key in keylist:     # Build dictionary from keylist and set value to null
        dictionary[key] = ''

    while len(dictionary) == 0:     # Part 2: Build dictionary
        print('Short story found. There are no vocabulary words.')
        break       # End the program

    else:
        print('Short story found. There are', len(dictionary), 'unique vocabulary words.')

        while True:     # Iterate if the answer is neither Y/y N/n
            answer = input('Would you like to update a definition (Y/N)? ')
            if answer in ['y', 'Y']:
                key = input('Term: ')
                if key not in dictionary:
                    print('ERROR! Term not found.')

                else:
                    if dictionary[key] != '':
                        print('WARNING! ', key, " is currently defined as '", dictionary[key], "'", sep='')
                    dictionary[key] = input("Definition: ")

            elif answer in ['n', 'N']:      # Part 3: Write to a file
                filename = input('What would you like to save the file as? ')
                vocabfile = open(filename, 'w')

                longword = len(max(dictionary, key=len))        # Find the length of the longest word

                for key in dictionary:      # Write data to the file in specified format
                    ftext ='{:<{l1}} - {}'.format(key, dictionary[key], l1=longword)
                    print(ftext, file=vocabfile)

                vocabfile.close()
                print('File saved')

                break       # End the program

except:     # End the program if URL of the short story does not work
    print('Short story not found.')
