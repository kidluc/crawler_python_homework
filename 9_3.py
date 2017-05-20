import requests
import sys


def top_question(number_question, label):
    url = 'https://api.stackexchange.com/'
# api stack
    tail_url = '2.2/questions?pagesize=' + \
               str(number_question) + \
               '&order=desc&sort=votes&' \
               'tagged=' + label + \
               '&site=stackoverflow'
# tail_url is link https://api.stackexchange.com/docs
# with your config
    resp = requests.get(url + tail_url)
    # get url respone
    cvjson = resp.json()['items']
    # conver to json type amd get in items list
    count = 1
    # counting number
    for i in cvjson:
        # starting loop in list of json type
        print('Question ' + str(count))
        print(i['title'])
        print(i['link'])
        print('\n')
        count += 1


if __name__ == '__main__':  # mark script
    print(top_question(sys.argv[1], sys.argv[2]))  # run by argv add by user
    # with open('top_quest', 'w') as f:
    #    f.write(str(top_question(sys.argv[1], sys.argv[2])))
    # remove None in last line :)
