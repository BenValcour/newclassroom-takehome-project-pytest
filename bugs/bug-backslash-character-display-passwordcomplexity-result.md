# Issue: countPAsswordCompleixty return does not properly display the backslash character

## Severity (Critical/Major/Minor/Low): C

## Priority (High/Medium/Low): H

## Description:
invalid data is being returned, so results are not of value.

The  password "\5" returns a value of 2, when 1 is expected.

The request json must escape the password string for the backslash character to be valid. Thus the password appears as "\\\\5" in the users data.  The server does not appear to be properly decoding this json string encoding when calculating the passwword complexity.

Interestingly,  "\\\\X"  returns the expected complexity of 1, where as "5\\\\X" returns 2, when 1 was expected. 

```
REQUEST_DATA(valid):  {'actionType': 'CountPasswordComplexity', 'top': None, 'users': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Luukas', 'last': 'Ojala'}, 'location': {'street': {'number': 772, 'name': 'Itsenäisyydenkatu'}, 'city': 'Lahti', 'state': 'Northern Savonia', 'country': 'Finland', 'postcode': 63593, 'coordinates': {'latitude': '-21.8325', 'longitude': '-106.9966'}, 'timezone': {'offset': '+9:30', 'description': 'Adelaide, Darwin'}}, 'email': 'luukas.ojala@example.com', 'login': {'uuid': '8ae15679-98f9-454d-aa31-6a267298fc18', 'username': 'bluebutterfly463', 'password': '\\5', 'salt': 'JG7Kwt3N', 'md5': '9afc33532f50e3823ae06f269ec30421', 'sha1': '88826f143e0d49f6753aedaf926d78c2c113b7f6', 'sha256': 'a378f34b90eacf51a3774614d8921cf2309d4d71759c1e9c006cfe7f78564275'}, 'dob': {'date': '1981-05-27T14:03:52.063Z', 'age': 41}, 'registered': {'date': '2005-02-23T06:07:13.500Z', 'age': 18}, 'phone': '05-165-970', 'cell': '045-148-33-49', 'id': {'name': 'HETU', 'value': 'NaNNA123undefined'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/37.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/37.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/37.jpg'}, 'nat': 'FI'}]}
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '26', 'Connection': 'keep-alive', 'Date': 'Tue, 09 May 2023 21:51:49 GMT', 'x-amzn-RequestId': 'a5eabfda-6f93-44fa-82c3-ff3e10b08706', 'x-amz-apigw-id': 'ErMCdGrLoAMF0zg=', 'X-Amzn-Trace-Id': 'Root=1-645ac075-036559aa17540ab2515e6b3c;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 adb1632aa800f446f3f4e7b45c9dfd3e.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'T9JA44K3ac1gQTEIfLn-4C7MGhBaaSAHGiYbPYjIAw9ikYH9n5tGyw=='}
RESPONSE CONTENT:  b'[{"name":"\\\\5","value":2}]'
PASSWORD: "\5", len(password) 2
EXPECTED PASSWORD COMPLEXITY RESULTS:  [{'name': '\\5', 'value': 1}]
RESPONSE:  [{'name': '\\5', 'value': 2}]
SIZE RESPONSE:  1
SIZE EXPECTED:  1
=============================================================================== short test summary info ===============================================================================
FAILED tests/test_count_password_complexity.py::test_count_password_complexity[./tests/testdata/users_password_backslash_character.dat-None-True] - AssertionError: assert [{'name': '\\5', 'value': 2}] == [{'name': '\\5', 'value': 1}]
================================================================================== 1 failed in 0.52s ==================================================================================

```



## Steps to reproduce:

Run the following test:

```
pytest -rA --runxfail tests/test_count_password_complexity.py::test_count_password_complexity[./tests/testdata/users_password_backslash_character.dat-None-True]
```



