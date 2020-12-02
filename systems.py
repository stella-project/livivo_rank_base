import requests

class Ranker(object):

    def __init__(self):
        self.idx = None
        self.connector_url = 'http://astral.zbmed.de:8000'

    def index(self):
        pass

    def rank_publications(self, query, page=0, rpp=10):
        
        num_found = 0
        itemlist = []


        if(query):
            response = requests.get(f'{self.connector_url}/ranking?query={query}&page={page}&rpp={rpp}')
            if (response.status_code == 200):
                result = response.json()
                itemlist = result['itemlist']
                num_found = result['num_found']
        return {
            'page': page,
            'rpp': rpp,
            'query': query,
            'itemlist': itemlist,
            'num_found': num_found
        }


class Recommender(object):

    def __init__(self):
        self.idx = None

    def index(self):
        pass

    def recommend_datasets(self, item_id, page, rpp):

        itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }

    def recommend_publications(self, item_id, page, rpp):

        itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }
