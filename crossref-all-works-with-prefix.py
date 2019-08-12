#! /usr/bin/env python

import click
from crossref_commons.iteration import iterate_publications_as_json
import requests
import time

@click.command()
@click.option('--prefix', default='10.22215', help='Crossref prefix')
def works_with_prefix(prefix):
    filter = {'prefix': prefix}
    for p in iterate_publications_as_json(max_results=100000, filter=filter):
        if 'URL' in p:
            click.echo(p['URL'] + "\t", nl=False)
            r = requests.head(p['URL'])
            if r.is_redirect:
                click.echo(r.headers['Location'])
        time.sleep(0.2)

if __name__ == '__main__':
    works_with_prefix()
