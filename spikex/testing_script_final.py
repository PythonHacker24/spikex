#!/usr/share/python3 


shodan_api_var = 'SuzLHlefIIvCJpoTKQXQKD5QYmP0PY4J'

with open(".SHODAN_API_KEY", "r") as api_key:
    shodan_api = str(api_key.read())


print(len(shodan_api))
print(len(shodan_api_var))