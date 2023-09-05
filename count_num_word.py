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

def process_url(the_url):
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
        filename = input('\nWhat filename do you want(xxx.txt): ')
        location = filename + '.txt'
        with open(location, 'w') as f_object:
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

# ファイル名を入力として受け取る
file_name = input("Enter the file name containing the list of URLs: ")

# ファイルからURLを読み込み、それぞれのURLに対してprocess_url関数を実行
with open(file_name, 'r') as file:
    urls = file.readlines()
    for url in urls:
        url = url.strip() # 改行や空白を取り除く
        process_url(url)

get_list()
store_results()