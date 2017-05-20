import requests
import json


# https://maps.googleapis.com/maps/api/place/radarsearch/
# json?location=10.779614,106.699256&radius=5000&type=cafe
# &keyword=coffee&key=AIzaSyCBYiul_JQrW7U9xfq30qpboLvHlYTXo84


def get_hcm_coffe(lat, lg, radius, tag, keyword):
    API_KEY = 'AIzaSyCBYiul_JQrW7U9xfq30qpboLvHlYTXo84'
    loc = str(lat) + ',' + str(lg)
    # lat, long of location
    rad = radius
    # radius searching around
    types = tag
    # tag, key word
    url = ('https://maps.googleapis.com/maps/api/place/'
           'nearbysearch/json?location={0}&radius={1}&'
           'types={2}&sensor=false&key={3}'.format(str(loc),
                                                   str(rad),
                                                   str(types),
                                                   str(API_KEY)))
    r = requests.get(url)
    jsonraw = r.text
    jsondata = json.loads(jsonraw)
    count = 1
    while count <= 50:
        for i in jsondata['results']:
            print('The Name of coffe shop: ', i['name'])
            print('The location in city: ', i['vicinity'])
            print('\n')
            count += 1


if __name__ == '__main__':
    import sys
    get_hcm_coffe(sys.argv[1], sys.argv[2],
                  sys.argv[3], sys.argv[4], sys.argv[5])
