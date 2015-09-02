#!/usr/bin/env python
# coding: utf-8

import unittest

# compatibilizing python 2.x and 3.x
try:
    from mock import Mock, patch
except ImportError:
    from unittest.mock import Mock, patch

from SolrAPI import Solr


class TestSolr(unittest.TestCase):

    def setUp(self):
        self.solr = Solr('http://some.url')

    def tearDown(self):
        pass

    @patch('SolrAPI.requests')
    def test_select_method(self, mock_requests):
        mock_requests.get.return_value = response = Mock()
        response.text = '{"responseHeader":{"status":0,"QTime":1,"params":{"q":"pickles","wt":"json"}},"{response": {"numFound": 1, "start": 0,"docs": []}}'
        response.status_code = 200

        self.assertEqual(self.solr.select(params={'q': 'pickles'}), '{"responseHeader":{"status":0,"QTime":1,"params":{"q":"pickles","wt":"json"}},"{response": {"numFound": 1, "start": 0,"docs": []}}')

    @patch('SolrAPI.requests')
    def test_select_method_without_params(self, mock_requests):
        mock_requests.get.return_value = response = Mock()
        response.text = '{"responseHeader":{"status":0,"QTime":1,"params":{"wt":"json"}},"response":{"numFound":0,"start":0,"docs":[]}}}'
        response.status_code = 200

        self.assertEqual(self.solr.select({}), '{"responseHeader":{"status":0,"QTime":1,"params":{"wt":"json"}},"response":{"numFound":0,"start":0,"docs":[]}}}')

    @patch('SolrAPI.requests')
    def test_select_method_change_return_format(self, mock_requests):
        mock_requests.get.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int><lst name="params"><str name="q">pickles</str<str name="wt">xml</str></lst></lst><result name="response" numFound="0" start="0"></result></lst></response>'
        response.status_code = 200

        self.assertEqual(self.solr.select({'q': 'pickles'}, format='xml'), '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int><lst name="params"><str name="q">pickles</str<str name="wt">xml</str></lst></lst><result name="response" numFound="0" start="0"></result></lst></response>')

if __name__ == "__main__":
    unittest.main()
