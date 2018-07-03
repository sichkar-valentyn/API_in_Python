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




# Implementing the task
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
