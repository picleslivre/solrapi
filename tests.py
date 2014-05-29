#!/usr/bin/env python
#coding: utf-8

import unittest

#compatibilizing python 2.x and 3.x
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


    @patch('SolrAPI.requests')
    def test_delete_method(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">37</int></lst></response>'
        response.status_code = 200

        self.assertEqual(self.solr.delete('*:*'), 0)


    @patch('SolrAPI.requests')
    def test_delete_method_commit_param(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">37</int></lst></response>'
        response.status_code = 200

        self.assertEqual(self.solr.delete('*:*', commit=True), 0)


    @patch('SolrAPI.requests')
    def test_delete_method_with_invalid_query_syntax(self, mock_requests):
        """
        With invalid query syntax the request must return response.status_code != 200
        """
        mock_requests.post.return_value = response = Mock()
        response.text = """<?xml version="1.0" encoding="UTF-8"?><response>
                          <lst name="responseHeader"><int name="status">400</int>
                          <int name="QTime">0</int></lst><lst name="error">
                          <str name="msg">no field name specified in query and
                          no default specified via \'df\' param</str>
                          <int name="code">400</int></lst>\n</response>"""
        response.status_code = 400

        self.assertEqual(self.solr.delete('*::blaus'), -1)


    @patch('SolrAPI.requests')
    def test_update_method(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int></lst></response>'
        response.status_code = 200

        add_xml = '<add><doc><field name="id">XXX</field><field name="field_name">YYY</field></doc></add>'

        self.assertEqual(self.solr.update(add_xml), 0)


    @patch('SolrAPI.requests')
    def test_update_method_commit_param(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int></lst></response>'
        response.status_code = 200

        add_xml = '<add><doc><field name="id">XXX</field><field name="field_name">YYY</field></doc></add>'

        self.assertEqual(self.solr.update(add_xml), 0)


    @patch('SolrAPI.requests')
    def test_update_method_nowellformat_xml(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = """<?xml version="1.0" encoding="UTF-8"?><response>
                        <lst name="responseHeader"><int name="status">400</int>
                        <int name="QTime">1</int></lst><lst name="error">
                        <str name="msg">Unexpected close tag &lt;/field&gt;;
                        expected &lt;/doc&gt;.at[row,col {unknown-source}]:
                        [1,36]</str><int name="code">400</int></lst></response>"""
        response.status_code = 200

        add_xml = '<add><doc>field name="id">XXX</field><field name="field_name">YYY</field></doc></add>'

        self.assertEqual(self.solr.update(add_xml), 400)


    @patch('SolrAPI.requests')
    def test_commit_method(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int></lst></response>'
        response.status_code = 200

        self.assertEqual(self.solr.commit(), 0)


    @patch('SolrAPI.requests')
    def test_commit_method_waitsearcher_param(self, mock_requests):
        mock_requests.post.return_value = response = Mock()
        response.text = '<?xml version="1.0" encoding="UTF-8"?><response><lst name="responseHeader"><int name="status">0</int><int name="QTime">1</int></lst></response>'
        response.status_code = 200

        self.assertEqual(self.solr.commit(waitsearcher=True), 0)

if __name__ == "__main__":
    unittest.main()
