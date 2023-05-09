# Issue: CountPasswordComplexity is including numeric characters in the complexity calculation.

## Severity (Critical/Major/Minor/Low): C

## Priority (High/Medium/Low): H

## Description:
Password complexity calculation is supposed to count non-alphanumeric characters.   However, the password "123456789" has a  complexity value of 9, instead of 0.


```
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '338', 'Connection': 'keep-alive', 'Date': 'Tue, 09 May 2023 22:27:10 GMT', 'x-amzn-RequestId': '3bf7b177-e170-4439-9f14-1e028d36f9b8', 'x-amz-apigw-id': 'ErRN0EpZoAMF1VA=', 'X-Amzn-Trace-Id': 'Root=1-645ac8be-2def40267ca782237e140e46;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 782e548cb0b1b64c63d995fc59568b48.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'McE0GEvRCBzXpZ-ALVODpI_wrf4ttSvobfX2DWPjlNEVdAEXcR5B0w=='}
RESPONSE CONTENT:  b'[{"name":"123456789","value":9},{"name":"@3v3nty122!","value":7},{"name":"123AbC&_!","value":6},{"name":"duplicateComplexity12345","value":5},{"name":"duplicateComplexity12345VII","value":5},{"name":" spaces spaces ","value":3},{"name":"cc#1","value":2},{"name":"1bananas","value":1},{"name":"ninjas","value":0},{"name":"ozzy","value":0}]'
PASSWORD: "ninjas", len(password) 6
PASSWORD: "1bananas", len(password) 8
PASSWORD: "duplicateComplexity12345", len(password) 24
PASSWORD: "duplicateComplexity12345VII", len(password) 27
PASSWORD: "ozzy", len(password) 4
PASSWORD: "123AbC&_!", len(password) 9
PASSWORD: "@3v3nty122!", len(password) 11
PASSWORD: "123456789", len(password) 9
PASSWORD: " spaces spaces ", len(password) 15
PASSWORD: "cc#1", len(password) 4
EXPECTED PASSWORD COMPLEXITY RESULTS:  [{'name': '123AbC&_!', 'value': 3}, {'name': ' spaces spaces ', 'value': 3}, {'name': '@3v3nty122!', 'value': 2}, {'name': 'cc#1', 'value': 1}, {'name': 'ninjas', 'value': 0}, {'name': '1bananas', 'value': 0}, {'name': 'duplicateComplexity12345', 'value': 0}, {'name': 'duplicateComplexity12345VII', 'value': 0}, {'name': 'ozzy', 'value': 0}, {'name': '123456789', 'value': 0}]
RESPONSE:  [{'name': '123456789', 'value': 9}, {'name': '@3v3nty122!', 'value': 7}, {'name': '123AbC&_!', 'value': 6}, {'name': 'duplicateComplexity12345', 'value': 5}, {'name': 'duplicateComplexity12345VII', 'value': 5}, {'name': ' spaces spaces ', 'value': 3}, {'name': 'cc#1', 'value': 2}, {'name': '1bananas', 'value': 1}, {'name': 'ninjas', 'value': 0}, {'name': 'ozzy', 'value': 0}]
SIZE RESPONSE:  10
SIZE EXPECTED:  10
=============================================================================== short test summary info ===============================================================================
FAILED tests/test_count_password_complexity.py::test_count_password_complexity[./tests/testdata/users_multi_with_dups_password_complexities.dat-None-True] - AssertionError: assert [{'name': '12...lue': 3}, ...] == [{'name': '12...lue': 0}, ...]
================================================================================== 1 failed in 0.49s ==================================================================================

```

## Steps to reproduce:

Run the following test:

```
pytest -rA --runxfail tests/test_count_password_complexity.py::test_count_password_complexity[./tests/testdata/users_multi_with_dups_password_complexities.dat-None-True]
```




