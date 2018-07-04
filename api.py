# File: api.py
# Description: Examples on how to work with API and web resources in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to work with API and web resources in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/API_in_Python (date of access: XX.XX.XXXX)




# Working with API in Python and web resources

import requests  # Importing library for doing requests
import json      # Importing library to work with json' data format

# Web resource openweathermap.org to get weather forecast
# Url for sending requests to
api_url = 'http://api.openweathermap.org/data/2.5/weather'

# Asking the city name to be found and represented with weather forecast
city = input('City name, please ')

# Setting parameters for the request
params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',  # It's needed to sing up to get personal one
    'units': 'metric'  # Saying that we need to get data in 'metric' standard and show temperature in Celsius
}

# Creating a request
respond = requests.get(api_url, params=params)

# Asking for the status
print(respond.status_code)

# Asking for the content type
print(respond.headers['Content-Type'])

# Getting the Python object as dictionary from json data in two ways
# Option 1 - Getting the dictionary from json data with 'requests' library
dic_from_json_1 = respond.json()
print(dic_from_json_1)

# Option 2 - Getting the dictionary from json data with 'json' library
dic_from_json_2 = json.loads(respond.text)
print(dic_from_json_2)

# All data that is received above contains key and the description can be found here
# https://openweathermap.org/current#current_JSON

# Showing some results from dictionary
data = dic_from_json_1
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))




# Implementing the task 1
# Finding information about numbers from web resource numbersapi.com
# Reading numbers from the file and writing them into the list
n = []
with open('test_numbers.txt') as f:
    for line in f:
        n += [line.rstrip()]

# Url for sending requests to
api_url = 'http://numbersapi.com'  # Don't forget to add the number itself '/n/' to the url when doing requests

# Setting parameters for the request
params = {
    'type': 'math',
    'json': 'true'
}

# Creating a requests and writing results in the dictionary
d = {}
for i in range(len(n)):
    respond = requests.get(api_url+'/'+n[i]+'/', params=params)

    # Getting the dictionary from json data with 'json' library
    data = json.loads(respond.text)

    # All data that is received above contains key and the description can be found here
    # http://numbersapi.com

    # Writing results in the dictionary by the key 'found'
    if data['found'] == False:
        d[n[i]] = 'Boring'
    if data['found'] == True:
        d[n[i]] = 'Interesting'

# Writing results from dictionary in the new list in the same order they were found in the file
results = []
for i in range(len(n)):
    results += [d[n[i]]]

# Joining all the elements from the list with the symbol \n
content = '\n'.join(results)

# Writing content in the new file
with open('test_numbers_results.txt', 'w') as w:
    w.write(content)

    


# Implementing task 2
# Obtaining information about art workers from the web resource artsy.net
# As inputs there will be id of each art worker
# We need to get names of each worker and date of birth
# As output - show the names of workers sorted by dates of birth
# If for some of them the date is similar - sort these ones by alphabetic order

# Getting a token from web resource artsy.net with api
client_id = 'c106a77ee4dda462f463'
client_secret = '3aa6adfa54057aa5c4341152482a97ee'

# Creating a request
request = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# Getting the dictionary from json data with 'json' library
data = json.loads(request.text)

# Obtaining the token
token = data["token"]

# Creating header with our token
headers = {"X-Xapp-Token": token}

# Reading the id of art workers and writing the results into the list
with open("test_dataset.txt") as f:
    results = []
    for line in f:
        line = line.rstrip()  # Deleting any symbols at the end of the line
        # Creating a template for the request
        template = 'https://api.artsy.net/api/artists/{}'
        # Creating a request with header
        respond = requests.get(template.format(line), headers=headers)
        # Getting the results in 'utf-8' coding
        respond.encoding = 'utf-8'
        # Getting the dictionary from json data with 'json' library
        data = json.loads(respond.text)
        # Adding all data in the list
        results.append(data)

# Sorting results with method 'sorted' for list
# As an argument for this method we use 'key'
# As an value for this argument we use results of 'lambda' function
# Results of 'lambda' function in our case are birthdays and then names
# So, firstly method 'sorted' will sort by birthday
# And if there is the same value of birthday it will sort by name
sorted_results = sorted(results, key=lambda artist: (int(artist['birthday']), artist['name']))

# Showing the final results
for item in sorted_results:
    print(item['name']) 
