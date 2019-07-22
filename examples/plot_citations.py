"""
Example - Citation Data
===========================

Scraping citation data from OpenCitations.
"""

###################################################################################################

from lisc.collect import collect_citations

###################################################################################################

dois = ['10.1007/s00228-017-2226-2', '10.1186/1756-8722-6-59']
citations = collect_citations(dois)

###################################################################################################

for doi, n_cites in citations.items():
    print(doi, n_cites)

###################################################################################################