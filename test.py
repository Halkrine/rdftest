from rdflib import URIRef
from rdflib.namespace import RDF
bob = URIRef("http://example.org/people/bob")
if ( bob, RDF.type, FOAF.Person ) in graph:
    print "This graph knows that Bob is a person!"