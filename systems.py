import pysolr

class Ranker(object):

    def __init__(self):
        self.idx = None
        self.solr = pysolr.Solr('http://134.95.56.177:8080/solr/default/')

    def index(self):
        pass

    def rank_publications(self, query, page, rpp):
        
        # Actually only working from ZBMED intranet due to firewall restrictions

        hits = 0
        itemlist = []

        if(query):
            res = self.solr.search(f'FS:{query}',**{'fl':'DBRECORDID','start':page*rpp,'rows':rpp})
            itemlist = [r['DBRECORDID'] for r in res]
            hits = res.hits

        return {
            'page': page,
            'rpp': rpp,
            'query': query,
            'itemlist': itemlist,
            'num_found': hits
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
