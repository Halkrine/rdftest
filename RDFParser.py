from rdflib import URIRef
from rdflib.namespace import RDF

from CRUD import CRUD

class RDFParser:
    def dataParse(self, dataset):

        print(dataset)


if __name__ == "__main__":
    parser = RDFParser()
    db = CRUD()
    db.set_graph_path()
    dataset = db.matchDB(alias='v',node='v_test',condition='1=1', returnAlias='v,e,n')
    parser.dataParse(dataset)