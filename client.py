import requests

url='http://localhost:5001'
uploads={'file1':open('bb.jpg','rb')}

print 'pull %s...'%url
req=requests.post(url,files=uploads)
print 'result: %s'%req.status_code
