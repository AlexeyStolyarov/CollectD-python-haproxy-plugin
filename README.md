python-haproxy collectD plugin
==============


based on python-haproxy `git clone https://github.com/nl5887/python-haproxy.git`

Read haproxy stats using socket 
before using it in CollectD 
replace 
```import collectd_mockup  as collectd```
to 
```#import collectd```


and comment out  at the bottom
```read_callback()```


data returnded to collectD looks like:
```
instance/type/type_instance: master-prod/BW_server_192.168.99.203_25036_2@test_sql_r36/qcur =  0
instance/type/type_instance: master-prod/BW_server_192.168.99.203_25036_1@be_test_sql_r37/qcur =  0
instance/type/type_instance: master-prod/BW_server_192.168.99.203_25036_1@test_sql_r36/qcur =  0
instance/type/type_instance: master-prod/BW_server_192.168.99.203_25036_2@be_test_sql_r37/qcur =  0
instance/type/type_instance: master-prod/BE_test_sql_r36/qcur =  0
instance/type/type_instance: master-prod/FE_test_r36/qcur =  
instance/type/type_instance: master-prod/FE_fe_test_r37/qcur =  

```


# Info from python-haproxy 

## Install
There are a few different ways you can install pyechonest:

* Use setuptools: `easy_install -U python-haproxy`
* Checkout the source: `git clone https://github.com/nl5887/python-haproxy.git` and install it yourself.

based on [http://www.gefira.pl/blog/2011/07/01/accessing-haproxy-statistics-with-python/] (http://www.gefira.pl/blog/2011/07/01/accessing-haproxy-statistics-with-python)


## Examples

```python
from haproxy import haproxy
stats = haproxy.HAProxyStats('/tmp/haproxy.sock')
stats.execute('show info')
[u'Name: HAProxy', u'Version: 1.4.18', u'Release_date: 2011/09/16', u'Nbproc: 1', u'Process_num: 1', u'Pid: 19234', u'Uptime: 0d 6h18m11s', u'Uptime_sec: 22691', u'Memmax_MB: 0', u'Ulimit-n: 8210', u'Maxsock: 8210', u'Maxconn: 4096', u'Maxpipes: 0', u'CurrConns: 1', u'PipesUsed: 0', u'PipesFree: 0', u'Tasks: 7', u'Run_queue: 1', u'node: ip-10-0-0-45', u'description: ', u'']
```

## Options
```
clear counters : clear max statistics counters (add 'all' for all counters)
help           : this message
prompt         : toggle interactive mode with prompt
quit           : disconnect
show info      : report information about the running process
show stat      : report counters for each proxy and server
show errors    : report last request and response errors for each proxy
show sess [id] : report the list of current sessions or dump this session
get weight     : report a server's current weight
set weight     : change a server's weight  
set timeout    : change a timeout setting
disable server : set a server in maintenance mode
enable server  : re-enable a server that was previously in maintenance mode
```

