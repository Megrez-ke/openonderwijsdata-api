from codebooks import Codebook
import csv
from itertools import islice, groupby
from scrapy.spider import BaseSpider
from scrapy.http import Request
import os
import urlparse, urllib

from onderwijsscrapers.items import ROASurvey


book = 'codebooks/roa/slgsd.csv'
field_dicts = list(csv.DictReader(open(book), delimiter=';'))
table_fields = Codebook(field_dicts, {'int': int})

source = os.path.abspath('../../../data/roa/roa-data.csv')

class ROASurveySpider(BaseSpider):
    name = 'roa_surveys'

    def start_requests(self):
        return [
            Request(
                # this is unnecessary but conceptually correct
                urlparse.urljoin('file:', urllib.pathname2url(source)), 
                self.parse_roa_results
            )
        ]

    def parse_roa_results(self, response):
        with open(source, 'r') as f:
            heads = (
                f.readline()
                .decode("utf-8-sig").encode("utf-8")
                .strip().split(';')
            )
            rows = islice((line.strip().split(';') for line in f), 2)

            data = table_fields.parse_table(heads, rows)
            for survey in data['per_code']:
                yield ROASurvey(**survey)