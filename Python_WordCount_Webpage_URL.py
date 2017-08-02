import bs4

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

def get_avg():
    for key, value in page_count_list.items():
        all_word_count.append(value)
    a = sum(all_word_count)
    b = len(all_word_count)
    calculation = a / b
    average_number = round(calculation,1)
    print('\nThe Average Word Count is ' + str(average_number) + ' Words')

def get_list():
    print('\n||||||||||||| LIST OF ALL URL WITH WORD COUNT |||||||||||||')
    for key, value in page_count_list.items():
        print('\n' + key + '    ---------    ' + str(value))
    get_avg()
    get_word_count()

def get_word_count():
    the_url = input(prompt)
    if the_url == 'quit':
        store_results()
    elif the_url == 'list':
        get_list()
    else:
        pass
    print('\nProcessing webpage................')
    fetched_url = uReq(the_url)
    page_html = fetched_url.read()
    fetched_url.close()
    page_soup = soup(page_html, "html.parser")
    seeing = page_soup.findAll('p')
    the_text = str(seeing)
    word_list = the_text.split()
    word_count = len(word_list)
    print('\n' + the_url[:50] + '... has ' + str(word_count) + ' words')
    page_name = str(the_url[8:50])
    page_count_list[page_name] = word_count

def store_results():
    question = '\nDo you want to save the results to a txt file? y or n: '
    answer = input(question)
    if answer == 'y':
        filename = input('\nWhat filename do you want: ')
        location = filename + '.txt'
        with open(location , 'w') as f_object:
            for key, value in page_count_list.items():
                f_object.write(key + ' ----------- ' + str(value) + '\n')
                f_object.write('\n')
        print('\nYour results have been stored as ' + str(location))
    else:
        pass
    input('\nPress "Enter" to Shutdown Program')
    exit()

page_count_list = {}
all_word_count = []

while True:
    prompt = 'Type "quit" to exit program ||| Type "list" to see all word counts'
    prompt +='                                                                '
    #just for spacing in command prompt
    prompt += '\nPlease paste the url of the webpage you want counted: '
    get_word_count()

    try:
        get_word_count()
    except ValueError:
        print('\n!!!!! Please Enter a Valid Command or URL !!!!!')
    else:
        pass
