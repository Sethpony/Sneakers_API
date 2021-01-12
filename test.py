"""
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes":10, "name": "Seth", "views": 25})
print(response.json())
input()
response = requests.get(BASE+"video/1")
print(response.json())
#used to test certain HTTP request methods
"""




import requests

'''
#essentially this file is to set up the data and send the request(s) for testing
BASE = "http://127.0.0.1:5000/"

data = [{"likes": 25, "name":"Smell Farts", "views":100}, 
        {"likes": 200, "name":"Eat Farts", "views":1000},
        {"likes": 500, "name":"Lick Farts", "views":10000}]

#input the data by looping through multiple PUT requests
#PUT requests does this - Create if it doesnt exist or update it if it does
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
'''
BASE = "http://127.0.0.1:5000/"

input()
response = requests.get(BASE + "sneaker/0")
print(response.json())

'''
input()
response = requests.get(BASE+"video/2")
print(response.json())
'''
#used to test certain HTTP request methods



#Open csv file
'''
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
'''



