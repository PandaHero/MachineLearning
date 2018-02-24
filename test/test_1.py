import ssl
import urllib.request

host = 'https://ali-barcode.showapi.com'
path = '/barcode'
method = 'GET'
appcode = '807cc5a8c3644173a0fcccb724bda651'
querys = 'code=6938166920785'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content.decode('utf-8'))
