SolrAPI
========

* Python implementation of the basic operation in the Solr Rest
* License: BSD
* Compatible With: python 2.7, 3.2 and 3.3

.. image:: https://travis-ci.org/picleslivre/solrapi.svg
    :target: https://travis-ci.org/picleslivre/solrapi

API Usage
---------

<pre>
<code>
>from SolAPI import Solr
>s = Solr('http://some.solr.url')
</code>
</pre>

Using select method: <b>s.select(query) return any int (-1 any error)</b>:
<pre>
<code>
>>>s.select('id:34987782')
0 (success)
>>>s.select('collection:usa')
-1 (error)
</code>
</pre>

Using delete method: <b>s.delete(query, commit=True/False) return any int by Solr otherwise -1(error)</b>:
<pre>
<code>
>>>s.delete('*:*')
0 (success delete all index)
>>>s.delete('id:08927973')
0 (success mark index with id=08927973 to be deleted)
>>>s.delete('id:08927973', commit=True)
0 (success delete index with id=08927973)
</code>
</pre>

Using update method: <b>s.delete(query, commit=True/False) return any int by Solr otherwise -1(error)</b>:
<pre>
<code>
>>>s.update('<doc><add><field name="id">XXX</field><field name="field_name">YYY</field></add></doc>')
0 (marked to change the value of filed field_name from the index with id=08927973)
>>>s.update('<doc><add><field name="id">XXX</field><field name="field_name">YYY</field></add></doc>', commit=True)
0 (changed the value of filed field_name from the index with id=08927973)
</code>
</pre>

Using commit method: <b>s.commit() return any int by Solr otherwise -1(error)</b>:
<pre>
<code>
>>>s.commit()
0 (all changed wil be done)
</code>
</pre>

How to Install?
=================
<pre>
<code>
>$ pip install solrAPI
</code>
</pre>
