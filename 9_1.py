import requests
import argparse


def githubrepos(username):
    url = 'https://api.github.com/users/{}/repos'.format(username)
    resp = requests.get(url).json()
    for repo in resp:
        result = repo['full_name']
        index = result.find('/')
        print(result[index+1:])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help="The Github name", type=str)
    args = parser.parse_args()
    result1 = githubrepos(args.name)


if __name__ == '__main__':
    main()
