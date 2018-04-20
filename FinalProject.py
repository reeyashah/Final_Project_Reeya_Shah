import json
import requests
import sqlite3
import plotly.plotly as py
import plotly.graph_objs as go
# from bs4 import BeautifulSoup
from requests_oauthlib import OAuth2Session
import secrets

plotly_username = 'reeyashah'
plotly = 'BZFKEOgD9gSKOOyafdo'


google_CACHE_FNAME = 'cache_google.json'
yelp_CACHE_FNAME = 'cache_yelp.json'
google = 'Google'
yelp = 'Yelp'
DBNAME = 'restaurant1.db'
# City = 'cities.json'
# Ratings = 'ratings.json'
# with open('/reeyashah/dekstop/cache_google.json') as google_file:
#     plotly_user_config = json.load(google_file)
# url = py.plot ([
#     {
#         'x':[]
#         'y':[]
#
# ])
# plotly.tools.set_credentials_file(plotly_username = 'reeyashah', api_key = 'BZFKEOgD9gSKOOyafdo')
# def plotly_ten(place, type_, keyword):
#     conn.sqlite3.connect(DBNAME)
#     cur = conn.cursor()
#     ratings_list = []
#     restuarant_list = []
#     top_name_query = 'SELECT Google.Name FROM Google '
#     top_name_query += "WHERE Google.Keyword = '{}' ".format(keyword)
#     top_name_query += "AND Google.City = '{}' ".format(city_input)
#     cur.execute(top_name_query)
#
#     top_ratings_query = 'SELECT Google.RATING FROM Google'
#     top_ratings_query += "WHERE Google.Keyword = '{}' ".format(keyword)
#     top_ratings_query += "AND Google.City = '{}' ".format(city_input)
#     cur1.execute(top_ratings_query)
#
#     for restuarant in cur:
#         restuarant_list.append(x)
#     print(restuarant_list)
#
#     for rating in cur1:
#         ratings_list.append(x)
#     print(ratings_list)

#     x = [ratings_list]
#     y = [restuarant_list]
#
#
#
# trace1 = [go.Bar(
#     x = ['keyword']
#     y = [Google.rating]
# )]
# py.iplot(data,filename = 'doc')
#
# trace2 =[







# conn = sqlite3.connect('restaurant.db')
# cur = conn.cursor()

# def ratings_request_using_cache(ratings_url, params):
#     auth = OAuth2(consumer_key, consumer_secret_key, access_token, access_token_secret)


# def get_yelp_ratings():
#     req = requests.get("https://api.yelp.com/v3/businesses/search")
#     soup = BeautifulSoup(req.text, "html.parser")
#
#     city_list = soup.find(class_="main-search_suggestions suggestions-list-container location-suggestions-list-container hidden")
#     city_list1 = soup.find_all("li")
#     for x in city_list1:
#         if state_abbr.lower() in x.['data-suggest-query']:
#             state_data = make_request_using_cache(baseurl + x.a['data-suggest-query'])
#             state_soup = BeautifulSoup(state_data, 'html.parser')
#             city = state_soup.find_all("ul", class_ = "item suggestion suggestions-list-item suggest-button")
#             city_list = []
#             for c in city_list:
#                 city_type =

def get_google_location(place, type_, keyword):
    place = place
    type_ = type_
    keyword = keyword
    statement = str(place + ',' + type_ + ',' + keyword)

    cache_part_try = find_cache_info(statement, google_CACHE_FNAME)



    if cache_part_try != None:
        return None
    else:
        print('requesting new data')

        google_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        parameters = {'key': secrets.google_api_key, 'query': place}
        response1 = requests.get(google_url, parameters).text
        req = json.loads(response1)
        latitude = (req['results'][0]['geometry']['location']['lat'])
        longitude = (req['results'][0]['geometry']['location']['lng'])
        location = str(latitude) + "," + str(longitude)
        # print(location)
        # exit()

        # google2_url = "https://maps.googleapis.com/maps/api/name/nearbysearch/json"
        # parameters = {'key':AIzaSyBCxtZVJwSf720P-bJBLq8dcTYJJWmtLVw, 'location' : location, 'radisu' : 1000, }
    #      nearby_sites_list = []
#      for x in nearby_data['results']:
#          nearby_sites_list.append(NearbyPlace(x['name']))
#      return nearby_sites_list
# example = NationalSite("National Park", "Grand Canyon", "dsfd")

        google2_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {'key':'AIzaSyBCxtZVJwSf720P-bJBLq8dcTYJJWmtLVw', 'location': location, 'radius' : 1000, 'type' : type_ , 'keyword' : keyword}
        response2 = requests.get(google2_url, parameters).text
        restaurant_results = json.loads(response2)
        restaurant_results = restaurant_results["results"]
        restaurant_in_city = {}
        restaurant_dict_list = []
        restaurant_names = {}
        for r in restaurant_results:
            latitude = round(r['geometry']['location']['lat'], 0)
            longitude = round(r['geometry']['location']['lng'], 0)
            location = str(latitude) + "," + str(longitude)
            restaurant_names = {'Id': str(location + "/" + r['name']), 'city': place.split(",")[0].rstrip(), 'state': place.split(",")[1].rstrip(), 'type' : type_, 'keyword': keyword, 'name': r['name'], 'rating': r['rating'], 'coord': location}
            restaurant_dict_list.append(restaurant_names)
        restaurant_in_city[statement] = restaurant_dict_list
        caching(statement, restaurant_in_city, google_CACHE_FNAME)
        Update_table(restaurant_in_city[statement], google) #check this

        return None


def get_google_location1(place, type_, keyword, keyword2, keyword3):
    place = place
    type_ = type_
    keyword = keyword
    statement1 = str(place + "," + type_ + "," + keyword + "," + keyword2 + "," + keyword3)

    cache_part_try1 = find_cache_info(statement1, google_CACHE_FNAME)



    if cache_part_try1 != None:
        return None
    else:
        print('requesting new data')

        google_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        parameters = {'key': secrets.google_api_key, 'query': place}
        response1 = requests.get(google_url, parameters).text
        req = json.loads(response1)
        latitude = (req['results'][0]['geometry']['location']['lat'])
        longitude = (req['results'][0]['geometry']['location']['lng'])
        location = str(latitude) + "," + str(longitude)
        # print(location)
        # exit()


        google2_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {'key':'AIzaSyBCxtZVJwSf720P-bJBLq8dcTYJJWmtLVw', 'location': location, 'radius' : 1000, 'type' : type_ , 'keyword' : statement1}
        response2 = requests.get(google2_url, parameters).text
        restaurant_results = json.loads(response2)
        restaurant_results = restaurant_results["results"]
        restaurant_in_city = {}
        restaurant_dict_list = []
        restaurant_names = {}
        for r in restaurant_results:
            latitude = round(r['geometry']['location']['lat'], 0)
            longitude = round(r['geometry']['location']['lng'], 0)
            location = str(latitude) + "," + str(longitude)
            restaurant_names = {'Id': str(location + "/" + r['name']),'city': place.split(",")[0].rstrip(), 'state': place.split(",")[1].rstrip(), 'type' : type_, 'keyword': keyword, 'name': r['name'], 'rating': r['rating'], 'coord': location}
            restaurant_dict_list.append(restaurant_names)
        restaurant_in_city[statement1] = restaurant_dict_list
        caching(statement1, restaurant_in_city, google_CACHE_FNAME)
        Update_table(restaurant_in_city[statement1], google) #check this

        return None




def yelp_information(place, type_, keyword = ""):
    location = place
    type_ = type_
    keyword = keyword
    word = str(keyword + ',' + type_ )
    key = str(place + ',' + type_ + ',' + keyword)
    cache_part_try = find_cache_info(key, yelp_CACHE_FNAME)

    if cache_part_try != None:
        return None
    else:
        yelp_url = "https://api.yelp.com/v3/businesses/search"
        definition = {'Authorization': 'Bearer EW5S0NEsEkQG-DCg8zMhjZvESXDJW0wWaP51OovBxHn0c-osGHe1Ni9ws7LVISMTzAvZvmhBRXQJdkcugRaXYucslAglPkcyEDiLrW_LeY7sgevooYiIO5z1ExrNWnYx'}
        input_info = {'term': word, 'location' : location}
        response1 = requests.get(yelp_url, headers = definition, params = input_info).text
        req = json.loads(response1)['businesses']
        restaurant_in_city1 = {}
        restaurant_dict_list1 = []
        restaurant_names1 = {}
        for r in req:
            latitude = round(r['coordinates']['latitude'], 0)
            longitude = round(r['coordinates']['longitude'], 0)
            location = str(latitude) + "," + str(longitude)
            restaurant_names1 = {'Id': str(location + "/" + r['name']),'city': place.split(",")[0].rstrip(), 'state': place.split(",")[1].rstrip(), 'type' : type_, 'keyword': keyword, 'name': r['name'], 'rating': r['rating'], 'coord': location}
            restaurant_dict_list1.append(restaurant_names1)
        restaurant_in_city1[key] = restaurant_dict_list1
        caching(key, restaurant_in_city1, yelp_CACHE_FNAME)
        Update_table(restaurant_in_city1[key], yelp) #check th
        return None

def yelp_information1(place, type_, keyword = "", keyword2 = "", keyword3 = ""):
    location = place
    type_ = type_
    keyword = keyword
    word = str(keyword + "," + type_ )
    key1 = str(place + "," + type_ + "," + keyword + "," + keyword2 + "," + keyword3)
    cache_part_try1 = find_cache_info(key1, yelp_CACHE_FNAME)

    if cache_part_try1 != None:
        return None
    else:
        yelp_url = "https://api.yelp.com/v3/businesses/search"
        definition = {'Authorization': 'Bearer EW5S0NEsEkQG-DCg8zMhjZvESXDJW0wWaP51OovBxHn0c-osGHe1Ni9ws7LVISMTzAvZvmhBRXQJdkcugRaXYucslAglPkcyEDiLrW_LeY7sgevooYiIO5z1ExrNWnYx'}
        input_info = {'term': key1, 'location' : location}
        response1 = requests.get(yelp_url, headers = definition, params = input_info).text
        req = json.loads(response1)['businesses']
        restaurant_in_city1 = {}
        restaurant_dict_list1 = []
        restaurant_names1 = {}
        for r in req:
            #print(r)
            latitude = round(r['coordinates']['latitude'], 0)
            longitude = round(r['coordinates']['longitude'], 0)
            location = str(latitude) + "," + str(longitude)
            restaurant_names1 = {'Id': str(location + "/" + r['name']),'city': place.split(",")[0].rstrip(), 'state': place.split(",")[1].rstrip(), 'type' : type_, 'keyword': keyword, 'name': r['name'], 'rating': r['rating'], 'coord': location}
            restaurant_dict_list1.append(restaurant_names1)
        restaurant_in_city1[key1] = restaurant_dict_list1
        caching(key1, restaurant_in_city1, yelp_CACHE_FNAME)
        Update_table(restaurant_in_city1[key1], yelp) #check th
        return None
    #print(req)
    # for x in req:
    #     print(x)
    # yelp_open = open(yelp_CACHE_FNAME, "w")
    # yelp_open.write(response1)
    # yelp_open.close()
    # Update_table(restaurant_in_city[key], yelp)
    # req = json.loads(response1)['businesses']
    # print(req)
    # exit()
    # yelp_open = open(yelp_CACHE_FNAME, "w")
    # yelp_open.write(response1)
    # yelp_open.close()


        # return cache_part_try

def caching(key, new_cache, doc):
    try:
        print("cache new part")
        reader = open(doc, "r")
        data = reader.read()
        reader.close()
        reader_json = json.loads(data)
        reader_json.update(new_cache)
        information_combined = json.dumps(reader_json)
        writer = open(doc, "w")
        writer.write(information_combined)
        writer.close()
    except:
        print("not caching new part")
        writer = open(doc, "w")
        spec = json.dumps(new_cache)
        writer.write(spec)
        writer.close()



# def make_request_using_cache(url):
#     if url in CACHE_DICTION:
#         print("getting cached data")
#         return CACHE_DICTION[url]
#
#     else:
#         print('making a new requests')
#         resp = requests.get(url).text
#         CACHE_DICTION[url] = resp
#         dumped_json_cache = json.dumps(CACHE_DICTION) #ask about error in class. using json.dumps(CACHE_DICTION) leads to type error Object of type nationalsite isn't json serializable, use url and html, key of cache be url and, value will be html string
#         writing = open(CACHE_FNAME,"w")
#         writing.write(dumped_json_cache)
#         writing.close()
#         return CACHE_DICTION[url]

def find_cache_info(key, doc):
    try:
        print("trying to cache")
        writer = open(doc,"r")
        reader = writer.read()
        reader_json = json.loads(reader)

        print('past json')

        if key in reader_json:
            print('passed properly')
            return reader_json[key]
        else:
            reader.close()
            return None
    except:
        print("not trying to cache")
        return None

def init_db(DBNAME):
    try:
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
    except Error as e:
        print(e)
    # google_file = open(google_CACHE_FNAME, 'r')
    # google_info = json.loads(google_file.read())

    #
    statement1 = '''
        DROP TABLE IF EXISTS 'Google';
    '''
    cur.execute(statement1)
    conn.commit()
    #conn.close()
    # google_file.close()

    statement2 = '''
        CREATE TABLE Google (
            'Id' TEXT NOT NULL,
            'City' TEXT NOT NULL,
            'State' TEXT NOT NULL,
            'Type' TEXT NOT NULL,
            'Keyword' TEXT NOT NULL,
            'Name' TEXT NOT NULL,
            'RATING' FLOAT NOT NULL,
            'coord' TEXT NOT NULL
            );
'''
    cur.execute(statement2)
    conn.commit()
    #conn.close()

    statement1 = 'DROP TABLE IF EXISTS "Yelp"'
    cur.execute(statement1)
    conn.commit()
    #conn.close()

    statement2 = '''
        CREATE TABLE Yelp (
            'Id' TEXT NOT NULL,
            'City' TEXT NOT NULL,
            'State' TEXT NOT NULL,
            'Type' TEXT NOT NULL,
            'Keyword' TEXT NOT NULL,
            'Name' TEXT NOT NULL,
            'RATING' FLOAT NOT NULL,
            'coord' TEXT NOT NULL
            );
    '''
    cur.execute(statement2)
    conn.commit()
    conn.close()


def add_tables():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    add_open = open(google_CACHE_FNAME, "r")
    data = add_open.read()
    data_json = json.loads(data)
    add_open.close()


    for info in data_json:
        print(info)
        for content in data_json[info]:
            Id = content['Id']
            City = content['city']
            State = content['state']
            Type = content['type']
            Keyword = content['keyword']
            Name = content['name']
            Rating = content['rating']
            coord = content['coord']

            query = ''' INSERT INTO Google Values (?,?,?,?,?,?,?,?)
            '''


            params = (Id, City, State, Type, Keyword, Name, Rating, coord)
            conn.execute(query,params)
            conn.commit()
    conn.close()

    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    add_open = open(yelp_CACHE_FNAME, "r")
    data = add_open.read()
    data_json1 = json.loads(data)
    add_open.close()

    for info in data_json1:
        print(info)
        for content in data_json1[info]:
            Id = content['Id']
            City = content['city']
            State = content['state']
            Type = content['type']
            Keyword = content['keyword']
            Name = content['name']
            Rating = content['rating']
            coord = content['coord']

            query = ''' INSERT INTO Yelp Values (?,?,?,?,?,?,?,?)
            '''

            params = (Id, City, State, Type, Keyword, Name, Rating, coord)

            cur.execute(query, params)
            conn.commit()
    conn.close()







def Update_table(new_content, TABLE_NAME):
    conn = sqlite3.connect(DBNAME) #ASK and ask about json and homework 10
    cur = conn.cursor()

    for contents in new_content:
        Id = contents['Id']
        City = contents['city']
        State = contents['state']
        Type = contents['type']
        Keyword = contents['keyword']
        Name = contents['name']
        Rating = contents['rating']
        coord = contents['coord']

        query = ''' INSERT INTO {} Values (?,?,?,?,?,?,?,?)
        '''.format(TABLE_NAME)

        params = (Id, City, State, Type, Keyword, Name, Rating, coord)
        conn.execute(query, params)
    conn.commit()
    #conn.close()


def top_ten(user_command):
    print(user_command)
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    ten_statement = 'SELECT Google.City, Google.Name, Google.Rating '
    if city_input and keyword in user_command:
        ten_statement += "FROM Google JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Keyword = '{}' ".format(keyword)
        ten_statement += " AND Google.City = '{}' ".format(city_input)
        ten_statement += " ORDER BY Google.Rating DESC LIMIT 3"
    ten_places = cur.execute(ten_statement)
    print(ten_statement)
    return ten_places
    conn.commit()
    conn.close()
def top_restaurant(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    top_statement = 'SELECT Google.City, Google.Name, Google.RATING FROM Google '
    if "restaurant" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    elif "bar" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    elif "food" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    elif "delivery" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    elif "takeout" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    elif "reservations" == type_input:
        top_statement += "JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        top_statement += "AND Google.City = '{}' ".format(city_input)
        top_statement += 'ORDER BY Google.Rating DESC LIMIT 3'
    top_places = cur.execute(top_statement).fetchall()
    print(top_statement)
    return top_places
    conn.commit()
    conn.close()
def top_city(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    city_statement = 'SELECT Google.City, Google.Type, AVG(Google.RATING) AS average FROM Google '
    if type_input and city_input in user_command:
        city_statement += " JOIN Yelp ON Google.Id = Yelp.Id WHERE Google.Type = '{}' ".format(type_input)
        city_statement += "AND Google.City = '{}' ".format(city_input)
        city_statement += "AND Google.Keyword = '{}' ".format(keyword)
        city_statement += " ORDER BY Google.Rating DESC LIMIT 3"
    city_places = cur.execute(city_statement)
    print(city_statement)
    return(city_places)
    conn.commit()
    conn.close()
def average_three_types(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    keyword_types = ['Mexican', 'Italian','Chinese', 'American', 'French', 'Indian', 'Thai', 'Korean','Japanese','Mediterranean']
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    keyword2 = full_command_split[4].strip()
    keyword3 = full_command_split[3].strip()
    get_google_location1(full_location, type_input, keyword, keyword2, keyword3)
    yelp_information1(full_location, type_input, keyword, keyword2, keyword3)
    city_input = full_command_split[0]
    three_statement = 'SELECT Google.City, Google.Keyword, AVG(Google.RATING) AS average FROM Google '
    if len(full_command_split) == 6:
        if keyword in keyword_types and keyword2 in keyword_types and keyword3 in keyword_types:
            three_statement += "JOIN Yelp ON Google.Id = Yelp.Id "
            three_statement += "WHERE Google.Keyword IN ('{}','{}','{}') ".format(keyword3, keyword2, keyword)
            three_statement += "AND Google.City = '{}' ".format(city_input)
            three_statement += "GROUP BY Google.Keyword "
            three_statement += "ORDER BY Google.RATING DESC"
    else:
        print('this did not work111')

    three_places = cur.execute(three_statement)
    #print(three_statement)
    return three_places
    conn.commit()
    conn.close()

def count_three(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    keyword2 = full_command_split[4].strip()
    keyword3 = full_command_split[3].strip()
    get_google_location1(full_location, type_input, keyword, keyword2, keyword3)
    yelp_information1(full_location, type_input, keyword, keyword2, keyword3)
    city_input = full_command_split[0]
    count_statement = 'SELECT Google.City, Google.Keyword, COUNT(Google.Keyword) as Count FROM Google '
    if len(full_command_split) == 6:
        if full_command_split[-1].strip() == keyword:
            print('yes!')
            if full_command_split[4].strip() == keyword2:
                print('yay!')
                if full_command_split[3].strip() == keyword3:
                    count_statement += "JOIN Yelp ON Google.Id = Yelp.Id "
                    count_statement += "WHERE Google.Keyword IN ('{}', '{}', '{}') ".format(keyword3, keyword2, keyword)
                    count_statement += "AND Google.City = '{}' ".format(city_input)
                    count_statement += "GROUP BY Google.Keyword "
                    count_statement += "ORDER BY COUNT(Google.Keyword) DESC"

    else:
        print('this did not work')
    count_places = cur.execute(count_statement)
    print(count_statement)
    return count_places
    conn.commit()
    conn.close()


def plotly_ten(user_command):
    conn=sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur1 = conn.cursor()
    full_command_split = user_command.split(',')
    print(full_command_split)
    full_location = str(full_command_split[0].strip() +  ", " + full_command_split[1].strip())
    #print(full_location)
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    ratings_list = []
    restaurant_list = []
    top_name_query = 'SELECT Google.Name FROM Google '
    top_name_query += 'JOIN Yelp on Google.Id = Yelp.Id '
    top_name_query += "WHERE Google.Keyword = '{}' ".format(keyword)
    top_name_query += "AND Google.City = '{}' ".format(city_input)
    top_name_query += "ORDER BY Google.Rating DESC LIMIT 3"
    cur.execute(top_name_query)
    print(top_name_query)


    top_ratings_query = 'SELECT Google.RATING FROM Google '
    top_ratings_query += 'JOIN Yelp on Google.Id = Yelp.Id '
    top_ratings_query += "WHERE Google.Keyword = '{}' ".format(keyword)
    top_ratings_query += "AND Google.City = '{}' ".format(city_input)
    top_ratings_query += "ORDER BY Google.Rating DESC LIMIT 3"
    cur1.execute(top_ratings_query)


    for restaurant in cur:
        print(restaurant)
        restaurant_list.append(restaurant[0])
    print(restaurant_list)

    for rating in cur1:
        print(rating)
        ratings_list.append(rating[0])
    print(ratings_list)

    trace0 = go.Bar(
        x = restaurant_list,
        y = ratings_list,
        marker = dict(
            color = 'rgb(150,200,255)',
            line = dict(
                color = 'rgb(8,10,100)',
                width = 1.5,
            )
        ),
        opacity = .7
    )

    data = [trace0]
    layout = go.Layout(
        title = 'Top ' + keyword  + ' in ' + full_location
    )
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'top_ten')
    conn.commit()
    conn.close()
def plotly_top_restaurant(user_command):
    conn=sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur1 = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    restaurant_list1 = []
    ratings_list1 = []
    top_name_query1 = 'SELECT Google.Name FROM Google '
    top_name_query1 += 'JOIN Yelp on Google.Id = Yelp.Id '
    top_name_query1 += "WHERE Google.Type = '{}' ".format(type_input)
    top_name_query1 += "AND Google.City = '{}' ".format(city_input)
    top_name_query1 += "ORDER BY Google.Rating DESC LIMIT 3"
    #top_name_query1 += "ORDER BY Google.RATING DESC LIMIT 10"
    cur.execute(top_name_query1)

    top_ratings_query1 = 'SELECT Google.RATING FROM Google '
    top_ratings_query1 += 'JOIN Yelp on Google.Id = Yelp.Id '
    top_ratings_query1 += "WHERE Google.Type = '{}' ".format(type_input)
    top_ratings_query1 += "AND Google.City = '{}' ".format(city_input)
    top_ratings_query1 += "ORDER BY Google.Rating DESC LIMIT 3"
    #top_ratings_query1 += "ORDER BY Google.RATING DESC LIMIT 10"
    cur1.execute(top_ratings_query1)


    for rating in cur1:
        ratings_list1.append(rating[0])


    for restaurant in cur:
        restaurant_list1.append(restaurant[0])
    trace1 = go.Bar(
        x = restaurant_list1,
        y = ratings_list1,
        marker = dict(
            color = 'rgb(150,200,255)',
            line = dict(
                color = 'rgb(8,10,100)',
                width = 1.5,
            )
        ),
        opacity = .7
    )

    data = [trace1]
    layout = go.Layout(
        title = 'Top ' + type_input + ' in ' + full_location
    )
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'top_places')
    conn.commit()
    conn.close()
def plotly_city(user_command):
    conn=sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur1 = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    get_google_location(full_location, type_input, keyword)
    yelp_information(full_location, type_input, keyword)
    city_input = full_command_split[0]
    restaurant_list2 = []
    ratings_list2 = []
    city_query1 = 'SELECT Google.Name FROM Google '
    city_query1 += 'JOIN Yelp on Google.Id = Yelp.Id '
    # city_query1 += "WHERE Google.Type = '{}' ".format(type_input)
    city_query1 += "AND Google.City = '{}' ".format(city_input)
    city_query1 += "AND Google.Keyword = '{}' ".format(keyword)
    city_query1 += "ORDER BY Google.Rating DESC LIMIT 3"
    #top_name_query1 += "ORDER BY Google.RATING DESC LIMIT 10"
    cur.execute(city_query1)

    city_ratings_query1 = 'SELECT AVG(Google.RATING) FROM Google '
    city_ratings_query1 += 'JOIN Yelp on Google.Id = Yelp.Id '
    city_ratings_query1 += "WHERE Google.Type = '{}' ".format(type_input)
    city_ratings_query1 += "AND Google.City = '{}' ".format(city_input)
    city_ratings_query1 += "ORDER BY Google.Rating DESC LIMIT 3"
    #top_ratings_query1 += "ORDER BY Google.RATING DESC LIMIT 10"
    cur1.execute(city_ratings_query1)


    for rating in cur1:
        ratings_list2.append(rating[0])
    print(ratings_list2)

    for restaurant in cur:
        restaurant_list2.append(restaurant[0])
    print(restaurant_list2)
    trace6 = go.Bar(
        x = restaurant_list2,
        y = ratings_list2,
        marker = dict(
            color = 'rgb(150,200,255)',
            line = dict(
                color = 'rgb(8,10,100)',
                width = 1.5,
            )
        ),
        opacity = .7
    )

    data = [trace6]
    layout = go.Layout(
        title = 'Top ' + keyword + ' ' + type_input + ' in ' + full_location
    )
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'top_places')
    conn.commit()
    conn.close()
def plotly_average_three(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur1 = conn.cursor()
    full_command_split = user_command.split(',')
    print(type(full_command_split))
    print(full_command_split)
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])

    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    keyword2 = full_command_split[4]
    keyword3 = full_command_split[3].strip()
    get_google_location1(full_location, type_input, keyword, keyword2, keyword3)
    yelp_information1(full_location, type_input, keyword, keyword2, keyword3)
    city_input = full_command_split[0]
    keyword_list = []
    ratings_list2 = []
    keyword_query = "SELECT Google.Keyword FROM Google "
    keyword_query += 'JOIN Yelp on Google.Id = Yelp.Id '
    keyword_query += "WHERE Google.Keyword IN ('{}', '{}', '{}') ".format(keyword3, keyword2, keyword)
    keyword_query += "AND Google.City = '{}' ".format(city_input)
    keyword_query += "GROUP BY Google.Keyword"
    print(keyword_query)
    cur.execute(keyword_query)

    average_ratings_query = 'SELECT AVG(Google.RATING) AS average FROM Google '
    average_ratings_query += 'JOIN Yelp on Google.Id = Yelp.Id '
    average_ratings_query += "WHERE Google.Keyword IN ('{}','{}','{}') ".format(keyword3,keyword2,keyword)
    average_ratings_query += "AND Google.City = '{}' ".format(city_input)
    average_ratings_query += 'GROUP BY Google.Keyword '
    average_ratings_query += 'ORDER BY Google.RATING DESC'
    print(average_ratings_query)
    cur1.execute(average_ratings_query)

    for keyword in cur:
        keyword_list.append(keyword[0])
    print(keyword_list)

    for rating in cur1:
        ratings_list2.append(rating[0])
    print(ratings_list2)

    trace2 = go.Bar(
        x = keyword_list,
        y = ratings_list2,
        marker = dict(
            color = 'rgb(150,200,255)',
            line = dict(
                color = 'rgb(8,10,100)',
                width = 1.5,
            )
        ),
        opacity = .7
    )

    data = [trace2]
    layout = go.Layout(
        title = 'Average Ratings of different keywords' + ' in ' + full_location #ask
    )
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'average_ratings')
    conn.commit()
    conn.close()
def plotly_count(user_command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur1 = conn.cursor()
    full_command_split = user_command.split(',')
    full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
    type_input = full_command_split[2].strip()
    keyword = full_command_split[-1].strip()
    keyword2 = full_command_split[4].strip()
    keyword3 = full_command_split[3].strip()
    get_google_location1(full_location, type_input, keyword, keyword2, keyword3)
    yelp_information1(full_location, type_input, keyword, keyword2, keyword3)
    city_input = full_command_split[0]
    keyword_list1 = []
    count_list = []
    keyword_query1 = 'SELECT Google.Keyword FROM Google '
    keyword_query1 += 'JOIN Yelp on Google.Id = Yelp.Id '
    keyword_query1 += "WHERE Google.Keyword IN ('{}', '{}', '{}') ".format(keyword3, keyword2, keyword)
    keyword_query1 += "AND Google.City = '{}' ".format(city_input)
    keyword_query1 += "GROUP BY Google.Keyword"
    cur.execute(keyword_query1)
    print(keyword_query1)

    count_query = 'SELECT COUNT(Google.Keyword) FROM Google '
    count_query += 'JOIN Yelp on Google.Id = Yelp.Id '
    count_query += "WHERE Google.Keyword IN ('{}', '{}', '{}') ".format(keyword3, keyword2, keyword)
    count_query += "AND Google.City = '{}' ".format(city_input)
    count_query += 'GROUP BY Google.Keyword '
    cur1.execute(count_query)
    print(count_query)

    for keyword in cur:
        keyword_list1.append(keyword[0])
    print(keyword_list1)

    for count in cur1:
        count_list.append(count[0])
    print(count_list)

    trace3 = go.Bar(
        x = keyword_list1,
        y = count_list,
        marker = dict(
            color = 'rgb(150,200,255)',
            line = dict(
                color = 'rgb(8,10,100)',
                width = 1.5,
            )
        ),
        opacity = .7
    )

    data = [trace3]
    layout = go.Layout(
        title = 'Counts of Keywords in ' + full_location
    )
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'count_places1')
    conn.commit()
    conn.close()
    # def handle_two():
#     user_input1 = input('Enter your first command')
#     user_input2 = input('Enter your second command')

def interactive_prompt():
    user_command = ''
    keyword_types = ['Mexican', 'Italian','Chinese', 'American', 'French', 'Indian', 'Thai', 'Korean','Japanese','Mediterranean']
    while user_command != 'exit':
        user_command = input('Enter a command: ')
        if len(user_command) == 0:
            user_command = input("You entered an empty command, please press enter and input valid command")
            continue
        elif user_command.isdigit():
            user_command = input("You entered a numerical digit, please press enter and input a valid command")
            continue
        # elif len(user_command) == 1:
        #     user_command = input("You entered an invalid command, please enter a valid command")
        #     continue
        #elif user_command !=
        elif user_command == 'exit':
            print('bye')
            exit()
        full_command_split = user_command.split(',')
        print(user_command)

        if len(full_command_split) == 4:
            full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
            type_input = full_command_split[2].strip()
            keyword = full_command_split[-1].strip()
            get_google_location(full_location, type_input, keyword)
            yelp_information(full_location, type_input, keyword)
            city_input = full_command_split[0]
            if keyword in keyword_types:
                answer= input('Do you want to see the top 3 names based on keyword, type, or both?')
                if answer == 'keyword':
                    x = top_ten(user_command)
                    for part in x:
                        print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                    answer = input('Do you want to see the graph?')
                    if answer == 'yes':
                        plotly_ten(user_command)
                    else:
                        print('No graph will be shown')
                        continue
                elif answer == 'type':
                    if type_input == 'restaurant':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    elif type_input == 'bar':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    elif type_input == 'food':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    elif type_input == 'delivery':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    elif type_input == 'takeout':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    elif type_input == 'reservations':
                        x = top_restaurant(user_command)
                        for part in x:
                            print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                        answer = input('Do you want to see the graph?')
                        if answer == 'yes':
                            plotly_top_restaurant(user_command)
                        else:
                            print('No graph will be shown')
                            continue
                    else:
                        print("Command not recognized: ", answer)
                        continue
                elif answer == 'both':
                    x = top_city(user_command)
                    for part in x:
                        print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                    answer = input('Do you want to see the graph?')
                    if answer == 'yes':
                        plotly_city(user_command)
                    else:
                        print('No graph will be shown')
                        continue
                else:
                    print("Answer not recognized: ", answer)
                    continue
            else:
                print("Command not recognized: ", user_command)
                continue


        elif len(full_command_split) == 6:
            #full_command_split = user_command.split(',')
            full_location = ", ".join([full_command_split[0].strip(),full_command_split[1].strip()])
            type_input = full_command_split[2].strip()
            keyword = full_command_split[-1].strip()
            keyword2 = full_command_split[4].strip()
            keyword3 = full_command_split[3].strip()
            get_google_location1(full_location, type_input, keyword, keyword2, keyword3)
            yelp_information1(full_location, type_input, keyword, keyword2, keyword3)
            city_input = full_command_split[0]
            # if len(full_command_split) == 0:
            #     print('You entered an empty command, please enter a valid command')
            #     continue
            # elif city_input.isdigit():
            #     user_command = input("You entered a numerical digit, please enter a valid command")
            #     continue
            if keyword in keyword_types and keyword2 in keyword_types and keyword3 in keyword_types:
                answer = input("Do you want to see the average ratings or counts for the keyword you entered?")
                if answer == 'average ratings':
                    x = average_three_types(user_command)
                    for part in x:
                        print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                    answer = input('Do you want to see the graph?')
                    if answer == 'yes':
                        plotly_average_three(user_command)
                    else:
                        print('No graph will be shown')
                        continue
                elif answer == 'counts':
                    x = count_three(user_command)
                    for part in x:
                        print('{0:60} {1:50} {2:50}'.format(part[0], part[1], part[2]))
                    answer = input('Do you want to see the graph?')
                    if answer == 'yes':
                        plotly_count(user_command)
                    else:
                        print('No graph will be shown')
                        continue
                else:
                    print("Command not recognized: ", answer)
                    continue

            else:
                print("Command not recognized: ", user_command)
        #elielse:f len(full_command_split) != 4 and len(full_command_split) != 6:
            #print("Command not recognized: ", user_command)
        else:
            print("Command not recognized: ", user_command)







# keyword
if __name__ == "__main__":
    interactive_prompt()
    #init_db(DBNAME)
    #add_tables()
    #Update_table()
    #init_db(DBNAME)
    #plotly_count("Ann Arbor, MI, restaurant, Chinese, Mexican, American")
    #plotly_average_three("Seattle, WA, restaurant, Italian, Mexican, American")
    #plotly_top_restaurant("Ann Arbor, MI, bar, American")
    #plotly_ten("Ann Arbor, MI, bar, Italian")
    #yelp_information1("Las Vegas, NV", "restaurant", "Mexican", "Chinese", "American")
    #yelp_information("Alpharetta, GA", "restaurant", "Mexican")
    #get_google_location("Alpharetta, GA", "restaurant", "Mexican")
    #get_google_location1("Cleveland, OH", "bar", "American", "Mexican","Italian" )
    #print(average_three_types("Ann Arbor, MI, restaurant, Mexican, Italian, Chinese"))
    #print(count_three("Dallas, TX, restaurant, Mexican, Italian, Chinese"))
    #print(top_ten("Ann Arbor, MI ,bar, American"))
    #print(top_city("Ann Arbor, MI ,restaurant, Chinese"))
    #print(top_restaurant("Ann Arbor, MI, bar, American"))
    #add_tables()

    #list_new_dict = [ {'city': 'Canton', 'state' : 'GA', 'type': 'Restuarant', 'keyword': 'Indian', "name": 'Anything', 'rating': '5'}, {'city': 'Duluth', 'state' : 'GA', 'type': 'Restuarant', 'keyword': 'Indian', "name": 'Anything', 'rating': '5'},{'city': 'Rochester', 'state' : 'MI', 'type': 'Restuarant', 'keyword': 'Chinese', "name": 'Anything', 'rating': '5'}]
    #Update_table(list_new_dict, google)
