#!/usr/bin/env python

import urllib
import requests


# http://www.networktechinc.com/pdf/configure-splitmux-http-api.pdf
# https://www.dropbox.com/personal/Splitmux

layout1 = '''
<conf><lout>
<id>1</id>
<nm>RABBI MARC</nm>
<ch1>
<t>258</t>
<l>132</l>
<w>1082</w>
<h>549</h>
<ar>0</ar>
<vl>0</vl>
<vr>0</vr>
<tr>64</tr>
<umd>0</umd>
<nm>RABBI JOSH</nm>
<en>1</en>
<bc>0</bc>
<bw>1</bw>
<au>1</au>
<it>0</it>
<il>0</il>
<iw>0</iw>
<ih>0</ih>
<iz>100</iz>
<ct>258</ct><cl>132</cl><cw>1082</cw><ch>549</ch>
</ch1>
<cord><p1>1</p1><p2>4</p2><p3>2</p3><p4>3</p4><p5>5</p5></cord>
<logo><t>0</t><l>0</l><w>4</w><h>4</h><en>0</en></logo>
<sn>0</sn>
<r>10</r>
<c>10</c>
<en>1</en>
<res><w>1920</w><h>1080</h></res>
</lout>
</conf>
'''


layout2 = '''
<conf><lout>
<id>1</id>
<nm>RABBI MARC</nm>
<ch1>
<t>258</t>
<l>132</l>
<w>1082</w>
<h>549</h>
<ar>0</ar>
<vl>0</vl>
<vr>0</vr>
<tr>64</tr>
<umd>0</umd>
</ch1>
</lout>
</conf>
'''



URLROOT="http://192.168.10.12"
s = requests.Session()

def logmein(s, URLROOT):

    data = {"username":"SPP", "password":"production"}
    data = {"username":"marc", "password":"marc"}
    url = urllib.parse.urljoin(URLROOT, 'goform/login')
    r = s.post(url, data=data)
    print(r.content)
    print(r.text)
    print(r.status_code)
print('------------------ cut here -------------------')
logmein(s, URLROOT)
url = urllib.parse.urljoin(URLROOT, 'goform/getCustomConfig')
r = s.post(url, data={'callback': 'callbackfunc'})
print(r.status_code)
#print(r.content)
print('------------------ cut here -------------------')
logmein(s, URLROOT)
url = urllib.parse.urljoin(URLROOT, 'goform/saveLayout')
headers = {'Content-Type': 'application/xml'}
r = s.post(url, data=layout2, headers=headers)

print(r.content)
print(r.status_code)
print(r.json())
