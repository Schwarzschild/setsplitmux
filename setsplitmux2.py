#!/usr/bin/env python

import urllib
import requests
import json

# http://www.networktechinc.com/pdf/configure-splitmux-http-api.pdf
# https://www.dropbox.com/personal/Splitmux

layout1 = '<conf><lout><id>1</id><nm>layout1</nm><ch1><t>258</t><l>132</l><w>1082</w><h>549</h><ar>0</ar><vl>0</vl><vr>0</vr><tr>64</tr><umd>0</umd><nm>Channel1</nm><en>1</en><bc>0</bc><bw>1</bw><au>1</au><it>0</it><il>0</il><iw>0</iw><ih>0</ih><iz>100</iz><ct>258</ct><cl>132</cl><cw>1082</cw><ch>549</ch></ch1><ch2><t>0</t><l>964</l><w>1039</w><h>586</h><ar>1</ar><vl>0</vl><vr>0</vr><tr>64</tr><umd>0</umd><nm>Channel2</nm><en>1</en><bc>0</bc><bw>1</bw><au>1</au><it>0</it><il>0</il><iw>1920</iw><ih>1080</ih><iz>100</iz><ct>0</ct><cl>964</cl><cw>951</cw><ch>535</ch></ch2><ch3><t>601</t><l>78</l><w>1426</w><h>802</h><ar>1</ar><vl>0</vl><vr>0</vr><tr>64</tr><umd>0</umd><nm>Channel3</nm><en>1</en><bc>0</bc><bw>1</bw><au>0</au><it>87</it><il>105</il><iw>1920</iw><ih>1080</ih><iz>100</iz><ct>537</ct><cl>0</cl><cw>960</cw><ch>543</ch></ch3><ch4><t>539</t><l>964</l><w>971</w><h>539</h><ar>1</ar><vl>0</vl><vr>0</vr><tr>64</tr><umd>0</umd><nm>Channel4</nm><en>1</en><bc>0</bc><bw>1</bw><au>0</au><it>0</it><il>0</il><iw>0</iw><ih>0</ih><iz>100</iz><ct>539</ct><cl>964</cl><cw>954</cw><ch>530</ch></ch4><cord><p1>1</p1><p2>4</p2><p3>2</p3><p4>3</p4><p5>5</p5></cord><logo><t>0</t><l>0</l><w>4</w><h>4</h><en>0</en></logo><sn>0</sn><r>10</r><c>10</c><en>1</en><res><w>1920</w><h>1080</h></res></lout></conf>'

URLROOT="http://192.168.10.12"
data = {"username":"marc", "password":"marc"}
url = urllib.parse.urljoin(URLROOT, 'goform/login')
r = requests.post(url, data=data)
print(r.status_code)
result = json.loads(r.content.decode('utf-8'))

#get session cookie and pass it with post request
sessionId = result['cookie'][10:]
cookie = {'sessionId': sessionId}

url = urllib.parse.urljoin(URLROOT, 'goform/saveLayout')
headers = {'Content-Type': 'application/xml'}
r = requests.post(url, data=layout1, headers=headers, cookies = cookie)

print(r.content)
print(r.status_code)
print(r.json())
