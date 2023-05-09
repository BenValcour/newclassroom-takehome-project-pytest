# Issue: A request with an invalid or missing actionType does not fail, and returns an empty result.

## Severity (Critical/Major/Minor/Low): Low

## Priority (High/Medium/Low): Low

## Description:

If a requset is submitted with an actionType value that is not one of the 3 valid actions, the expectations is that the request will fail with an http status code of 400

With and actionType of **"actionType": "no such action"** or not actionType property in the request, a 200  status code was returned.

```
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '0', 'Connection': 'keep-alive', 'Date': 'Wed, 03 May 2023 00:02:28 GMT', 'x-amzn-RequestId': 'ee676c87-393b-415f-b30d-e6564ce997bd', 'x-amz-apigw-id': 'EUanRHfqIAMFVtw=', 'X-Amzn-Trace-Id': 'Root=1-6451a494-33295e99288df73611e78c78;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 478e42d78af3de35728ba409bf63e348.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'jZh_3f2QmkTtNVdhSYLzxfAtjRoGwO2xbYf1LiOx2KTQ7i4VHb-rEQ=='}
RESPONSE CONTENT:  b''
```



## Steps to reproduce:

Run the following:

```
pytest -ra --runxfail tests/test_request_errors.py::test_request_errors[./tests/testdata/request_invalid_actiontype.dat-400]
```



