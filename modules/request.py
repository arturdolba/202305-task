'''HTTP operations module'''

import requests


def get_page_content(url):
    '''
    Gets content of page from given URL.
    It uses GET method for HTTP/HTTPS connections.
    '''
    try:
        response = requests.get(url,timeout=300)
        if response.status_code == 200:
            return response.text
        else:
            print("Request returned status - %d" % response.status_code)
            return
    except requests.HTTPError:
        print("Can't load content from given URL.")
    except requests.exceptions.MissingSchema:
        print("URL is not valid http or https address.")
    except requests.exceptions.ConnectTimeout:
        print("Server timeout. Try again later or check URL.")
    except requests.exceptions.ConnectionError:
        print("Can't connect to server. Try again later or check URL")
