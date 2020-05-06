from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
    print('GET: %s' % url)
    try:
        with closing(get(url, stream=True)) as response:
            if is_good_response(response):
                return response.content
            else:
                return None
    
    except RequestException as e:
        log_error('Error getting request {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(response):
    return response.status_code == 200

def log_error(e):
    print(e)
