SolrAPI
========

* Python implementation of the basic operation in the Solr Rest
* License: BSD
* Compatible With: python 2.7, 3.2 and 3.4

[![Build Status](https://travis-ci.org/picleslivre/solrapi.svg)](https://travis-ci.org/picleslivre/solrapi)

See Build: https://travis-ci.org/picleslivre/solrapi

API Usage
---------

<pre>
<code>
>>>from SolrAPI import Solr
>>>s = Solr('http://some.solr.url')
</code>
</pre>

Using select method: <b>s.select(query)</b>:
<pre>
<code>
>>>s.select('id:34987782')
>>>s.select('collection:usa')
</code>
</pre>

Using delete method: <b>s.delete(query, commit=True/False)</b>:
<pre>
<code>
>>>s.delete('*:*')
>>>s.delete('id:08927973')
>>>s.delete('id:08927973', commit=True)
</code>
</pre>

Using update method: <b>s.delete(query, commit=True/False)</b>:
<pre>
<code>
>>>s.update('<doc><add><field name="id">XXX</field><field name="field_name">YYY</field></add></doc>')
>>>s.update('<doc><add><field name="id">XXX</field><field name="field_name">YYY</field></add></doc>', commit=True)
</code>
</pre>

Using commit method: <b>s.commit()</b>:
<pre>
<code>
>>>s.commit()
</code>
</pre>

How to Install?
=================
<pre>
<code>
>$ pip install solrAPI
</code>
</pre>

For develop version
====================

-e git+git@github.com:picleslivre/solrapi.git#egg=solrapi
