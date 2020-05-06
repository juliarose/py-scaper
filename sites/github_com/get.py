from sites import Site
from bs4 import BeautifulSoup

PARSER = 'lxml'
HOSTNAME = 'github.com'

class GithubCom(Site):
    def get_profile(self, username):
        def extract_data(response):
            parsed = BeautifulSoup(response, PARSER)
            name_element = parsed.select('span.vcard-fullname')[0]
            
            return {
                'name': name_element.text
            }
        
        response = self.get('/{}'.format(username))
        
        if response is not None:
            return extract_data(response)
        else:
            return None

githubCom = GithubCom(HOSTNAME)