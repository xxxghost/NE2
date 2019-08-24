import netconf
dev_ip="10.77.99.253"
usr='admin'
password='Admin@432!'
get_xml = """ 

 <top xmlns="http://www.h3c.com/netconf/data:1.0">


 <Ifmgr>
 <Interfaces>
 <Interface>
 <IfIndex>

 </IfIndex>
 <Name>

 </Name>
 </Interface>
 </Interfaces>
 </Ifmgr>
 </top>


 """
import time
if __name__ == '__main__':
 netconf.get_netconf(dev_ip, 830, usr, password,get_xml)
 print ("closed")
 time.sleep(1)