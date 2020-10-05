#!/usr/bin/env python

import urllib
import requests


# http://www.networktechinc.com/pdf/configure-splitmux-http-api.pdf
# https://www.dropbox.com/personal/Splitmux

layout1 = '''
<?xml version="1.0" encoding="utf-8"?><nm>SPKR RABBI
SPLIT</nm><ch1><t>0</t><l>0</l><w>1920</w><h>1080</h><ar>1</ar><vl>0</vl><vr
>0</vr><umd>0</umd><nm>Channel
1</nm><en>0</en><bc>0</bc><bw>0</bw><au>0</au><tr>64</tr><it>0</it><il>0</il><
ih>1080</ih><iw>1920</iw><iz>100</iz><ct>0</ct><cl>0</cl><cw>1920</cw><ch>108
0</ch></ch1><ch2><t>282</t><l>1054</l><w>757</w><h>513</h><ar>0</ar><vl>0</v
l><vr>0</vr><umd>0</umd><nm>GALLERY</nm><en>0</en><bc>0</bc><bw>0</bw
><au>0</au><tr>64</tr><it>0</it><il>0</il><ih>1080</ih><iw>1920</iw><iz>100</iz><
ct>282</ct><cl>1054</cl><cw>757</cw><ch>513</ch></ch2><ch3><t>295</t><l>1001
</l><w>866</w><h>487</h><ar>1</ar><vl>0</vl><vr>0</vr><umd>0</umd><nm>SPE
AKER
1</nm><en>1</en><bc>0</bc><bw>0</bw><au>0</au><tr>64</tr><it>0</it><il>0</il><
ih>1080</ih><iw>1920</iw><iz>100</iz><ct>295</ct><cl>1001</cl><cw>866</cw><ch
>487</ch></ch3><ch4><t>295</t><l>64</l><w>864</w><h>485</h><ar>1</ar><vl>0</
vl><vr>0</vr><umd>0</umd><nm>RABBI</nm><en>1</en><bc>0</bc><bw>0</bw><
au>0</au><tr>64</tr><it>0</it><il>5</il><ih>1080</ih><iw>1920</iw><iz>100</iz><ct>
295</ct><cl>66</cl><cw>864</cw><ch>485</ch></ch4><logo><t>0</t><l>0</l><w>0</
w><h>0</h><ar>0</ar><vl>0</vl><vr>0</vr><umd>0</umd><nm>default</nm><en>0<
/en><bc>0</bc><bw>0</bw><au>0</au><tr>0</tr><it>0</it><il>0</il><ih>0</ih><iw>0<
/iw><iz>100</iz><ct>0</ct><cl>0</cl><cw>20</cw><ch>20</ch></logo><chroma><cen
>0</cen><ainv>0</ainv><nr>0</nr><msub>0</msub><mback>0</mback><rl>0</rl><rh
>16</rh><gl>0</gl><gh>16</gh><bl>0</bl><bh>16</bh><tnotk>64</tnotk><tk>0</tk><
tout>0</tout><tin>0</tin></chroma><cord><p1>1</p1><p2>2</p2><p3>3</p3><p4>4</
p4><p5>5</p5></cord><sn>0</sn><r>10</r><c>10</c><en>0</en><res><w>1920</w
><h>1080</h></res>
'''


URLROOT="http://192.168.10.12"

s = requests.Session()
data = {"username":"SPP", "password":"production"}
url = urllib.parse.urljoin(URLROOT, 'goform/login')
r = s.post(url, data=data)
print(r.content)

print('------------------ cut here -------------------')

url = urllib.parse.urljoin(URLROOT, 'goform/getCustomConfig')
r = s.post(url, data={'callback': 'callbackfunc'})
print(r.content)
`
print('------------------ cut here -------------------')

# url = urllib.parse.urljoin(URLROOT, 'goform/saveLayout')
# headers = {'Content-Type': 'application/xml'}
# r = s.post(url, data=layout1, headers=headers)
# print(r.content)
