SolrAPI
========
[![Build Status](https://secure.travis-ci.org/scieloorg/solrapi.png?branch=master)](https://travis-ci.org/scieloorg/solrapi)

API Usage
---------

The instance of <b>Solr</b> parses and validates the time of construction instance:
<pre>
<code>
>from SolAPI import Solr
>s = Solr('http://some.solr.url')
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
