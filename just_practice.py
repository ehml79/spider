#import urllib.request


#response = urllib.request.urlopen('https://www.python.org')

# print(response.read().decode('utf-8'))

#print(type(response))


########################################################################################################################
#import urllib.parse
#import  urllib.request
#
#data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#print(response.read())
########################################################################################################################

#import socket
#import urllib.request
#import urllib.error
#
#try:
#    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
#except urllib.error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print('TIME OUT')


########################################################################################################################

from urllib import request, parse

url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
