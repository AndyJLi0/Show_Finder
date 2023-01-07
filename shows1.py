'''
This program uses a REST API to search popular shows
Author: Kyle
November 18, 2022
'''
import requests

# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    response = requests.get(f'{BASE_URL}search/shows?q={query}')
    if response.status_code == 200:
        data = response.json()
        return data

def main():
    """
    Main function 
    """
    query = input("Search for a show: ")
    results = get_shows(query)
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        for result in results:
            show = result["show"]
            print(f"{n}. {show['name']}")
            n += 1 

if __name__ == '__main__':
    main()