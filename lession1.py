import requests
import json

#first_task
def user_repositories(username):
    repos = requests.get(f'https://api.github.com/users/{username}/repos')
    with open('repos_json.json', 'w') as f:
        json.dumps(repos.json())

    repos_list = []
    for r in repos.json():
        repos_list.append(r['html_url'])
    return repos_list

print(user_repositories('olihma'))



# #second task
city = input('Write name of the city you are interested in')

def current_weather(city):
    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=11ac6d109ee1f7309970dbd33cf677d5')
    url_json = url.json()
    if url_json['cod']=='404':
        return ('city not found')
    else:
        weather_list = {}
        for item in url_json['weather'][0].items():
            weather_list[item[0]] =item[1]
        for item in url_json['main'].items():
            weather_list[item[0]] = item[1]
        return weather_list

print(f'Current weather for {city}: {current_weather(city)}')







