#!/usr/bin/env python
#-*-coding:utf8-*-

import unittest

from pyunisend import PyUniSend

APIKEY = 'add your apikey here'

class SimpleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.APIKEY = APIKEY
        
    def testPyUniSendSecure(self):
        secure_url = 'https://www.unisender.com/ru/api/'
        api = PyUniSend(self.APIKEY, secure=True, test_mode=True)
        self.assertEqual(api.base_api_url, secure_url)

    def testPyUniSendNoSecure(self):
        secure_url = 'http://api.unisender.com/ru/api/'
        api = PyUniSend(self.APIKEY, secure=False, test_mode=True)
        self.assertEqual(api.base_api_url, secure_url)

class MethodTestCase(unittest.TestCase):

    def setUp(self):
        self.APIKEY = APIKEY
        self.api = PyUniSend(self.APIKEY, secure=True, test_mode=True)

    def testMethodGetLists(self):
        title = u'Рассылка'
        lists = self.api.getLists()
        self.assertTrue(title in lists['result'][0]['title'])

    def testMethodCreateList(self):
        newlist = self.api.createList(title='NewList')
        self.assertTrue(newlist['result']['id'] > 0 )

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(SimpleTestCase))
	suite.addTest(unittest.makeSuite(MethodTestCase))	
	return suite
		
if __name__ == '__main__':
    unittest.main(defaultTest='suite')            
