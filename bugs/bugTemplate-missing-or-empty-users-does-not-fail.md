# Issue: Expecting a client error, HTTP status code 400 if the users array is missing or empty in the request.

## Severity (Critical/Major/Minor/Low): low

## Priority (High/Medium/Low): low

## Description:

The requirement indicate the users array must have 1 or more users specified.  Expecting if the users array is missing or is empty a 400 http status code would be returned.

observed a 200 status code was returned instead. 

Example requests:
```
{"actionType": null, "top": null, "users": [] }
```
```
{"actionType": null, "top": null }
```

response from server:

```
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '0', 'Connection': 'keep-alive', 'Date': 'Tue, 02 May 2023 23:41:43 GMT', 'x-amzn-RequestId': '66bda262-0e79-40ea-841e-d339086c0d38', 'x-amz-apigw-id': 'EUXkuGYIoAMFXEw=', 'X-Amzn-Trace-Id': 'Root=1-64519fb7-06c6a730727db7ce4488489c;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 0459f0f7053eeb224fd9fe0f5db5970a.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'UgBvrtYl72IgWmbjjFpSLWFVbOezTRetl8oh5-1JlXr1PcEcaAVGuw=='}
RESPONSE CONTENT:  b''
```

## Steps to reproduce:

run tests:

```
pytest -ra --runxfail tests/test_request_errors.py::test_request_errors[./tests/testdata/request_no_users_data.dat-400]
```
or
```
pytest --runxfail -rA tests/test_request_errors.py::test_request_errors[./tests/testdata/request_no_users_in_users_array.dat-400]
```



