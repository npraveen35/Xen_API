# Xen_API

Developer: Praveen.Nagegowda@infinite.com

## XenServer 7.0.0  API python works using SDK

**My Work Environment Details:**

The python script custom_list_vms.py displays the tabular list of virtual machines hosted on your XenServer.

uname -a =>
Linux infics-praveen-odl 4.4.0-34-generic #53~14.04.1-Ubuntu SMP Wed Jul 27 16:56:40 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

pip 8.1.2

virtualenv 15.0.3

XenServer-7.0.0-SDK.zip

**Usage:**

1] make the script executable 

*chmod +x custom_list_vms.py*

2] Run the script as  

*./custom_list_vms.py IP USER PASSWORD*

Replace IP with your XenServer IP address and USER & PASSWORD with login username & password of XenServer.

Example Usage: *./custom_list_vms.py http://172.27.3.50 root MY_PASSWORD*







References:
https://www.citrix.com/downloads/xenserver/product-software/xenserver-70-standard-edition.html

