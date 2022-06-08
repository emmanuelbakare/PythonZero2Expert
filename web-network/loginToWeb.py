# login to skillshare
import requests

s=requests.Session()
payload={
    'email':'janetoadebo@yahoo.com',
    'password':'3nlaccordpage'
 
}
resp=s.post('https://www.skillshare.com/ajaxlogin', json=payload)
print(resp.text)