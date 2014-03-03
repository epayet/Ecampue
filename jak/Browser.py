'''
Created on Nov 25, 2013

@author: manu
'''

import mechanize

class Browser(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.br = mechanize.Browser()
        
    def open(self, url):
        self.br.open(url)
        
    def select_form(self, formName):
        self.br.select_form(formName)