import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
import time
def my_unknown_host_cb(host, figerprint):
 return True
def get_netconf(host, port, user, pwd,get_xml):
 with manager.connect_ssh(host=host,
 port=port,
 username=user,
 password=pwd,
 unknown_host_cb=my_unknown_host_cb,
 device_params = {'name':'h3c'}) as m:


    print (m.get(('subtree', get_xml)))


'''from ncclient import manager
host='10.77.99.253'
user='admin'
m= manager.connect(host=host, port=830,password='Admin@432!',
                     username=user, hostkey_verify=False,
                     device_params={'name':'h3c'})
c =m.get_config(source='running').data_xml

print(c)

'''