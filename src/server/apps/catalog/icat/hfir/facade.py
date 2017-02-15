#from .communication import HFIRICat
from server.apps.catalog.icat.hfir.communication import HFIRICat

import json
import logging

from django.utils import dateparse
from pprint import pformat, pprint


logger = logging.getLogger('catalog.icat.hfir')

class Catalog(object):
    '''
    Custom functionality to ICAT!
    '''
    def __init__(self):
        '''
        '''
        self.icat = HFIRICat()


    def get_experiments(self, instrument):
        '''
        [{'exp': ['exp305',
                'exp320',
                'exp327',
                'exp338',
                'exp357',
                'exp367',
                'exp368',
                'exp369',
                'exp380'],
        'ipts': 'IPTS-0000'},

        '''
        response = self.icat.get_experiments(instrument)
        result = None
        if response is not None:
            result = [{'ipts': entry['name'],
                       'exp' : sorted([
                           tag.split('/')[1]
                           for tag in entry['tags'] ])}
                      for entry in  response]
        return result
    
    def get_runs(self, instrument, ipts, exp):
        '''
        return a list of:
        {'end_time': '2017-02-06 10:03:18',
        'filename': 'BioSANS_exp379_scan0500_0001.xml',
        'location': '/HFIR/CG3/IPTS-18347/exp379/Datafiles/BioSANS_exp379_scan0500_0001.xml',
        'sample_background': {'buffer D2O': '35'},
        'sample_info': {'Sample type': 'd25'},
        'sample_parameters': {'Chiller Temp (C)': '20.000000',
                                'Min Wait (sec)': '1.000000'},
        'title': 'DAS Test 6(IC: DAS_test_SVP_p0015top8_Banjo S: 0.003-0.8 P:[ '
                'Chiller Temp (C): 20.000000 Min Wait (sec): 1.000000])'}]

        '''
        response = self.icat.get_runs(instrument, ipts, exp)
        result = None
        if response is not None:
            #result = response
            result = [dict(
                {
                    # subset
                    k: entry[k] for k in ('location', 'thumbnails')
                }, **{
                    # Metadata here:
                    'filename': entry['metadata']['spicerack']['@filename'],
                    'end_time':  entry['metadata']['spicerack']['header']['end_time'],
                    'title': entry['metadata']['spicerack']['header']['scan_title'],
                    'sample_info': entry['metadata']['spicerack']['sample_info']['sample']['field']
                                   if entry['metadata']['spicerack']['sample_info']['sample'] else None,
                    'sample_background': entry['metadata']['spicerack']['sample_info']['background']['field']
                                         if entry['metadata']['spicerack']['sample_info']['background'] else None,
                    'sample_parameters': entry['metadata']['spicerack']['sample_info']['parameters']['field']
                                         if entry['metadata']['spicerack']['sample_info']['parameters'] else None,
                    'metadata' : entry['metadata']['spicerack']['header']
                })
                      for entry in response
                     ]
        return result
    
    def run_info(self, instrument, ipts, file_location):
        '''

        '''

        response = self.icat.run_info(instrument, ipts, file_location)
        result = None
        if response is not None:
            # result = response
            entry = response
            result = dict(
                {
                    # subset
                    k: entry[k] for k in ('location', 'thumbnails')
                }, **{
                    # Metadata here:
                    'filename': entry['metadata']['spicerack']['@filename'],
                    'metadata' : entry['metadata']['spicerack']['header']
                })
        return result


if __name__ == "__main__":
    icat = Catalog()
    # res = icat.get_experiments("CG3")
    # pprint(res)
    # res = icat.get_runs("CG3", 'IPTS-18347','exp379') 
    # pprint(res)
    res = icat.run_info("CG3", 'IPTS-18347', '/HFIR/CG3/IPTS-18347/exp379/Datafiles/BioSANS_exp379_scan0500_0001.xml') 
    pprint(res)