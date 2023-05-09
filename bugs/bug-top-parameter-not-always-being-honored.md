# Issue: Top parameter is nto always being honored for CountPasswordComplexity

## Severity (Critical/Major/Minor/Low): Minor

## Priority (High/Medium/Low): Low

## Description:

This issue reproduces some percentage of the time.

Given a request with top set to 10 and  distinct passwords > 10.

Expected a result of 10:

```
[{'name': '515000', 'value': 6}, {'name': '336699', 'value': 6}, {'name': '303030', 'value': 6}, {'name': '1223', 'value': 4}, {'name': '2005', 'value': 4}, {'name': 'rush2112', 'value': 4}, {'name': '2001', 'value': 4}, {'name': '5555', 'value': 4}, {'name': '23skidoo', 'value': 2}, {'name': 'm5wkqf', 'value': 1}]
```

Actual result during failure, will get a result of 11:

```
[{"name":"515000","value":6},{"name":"336699","value":6},{"name":"303030","value":6},{"name":"1223","value":4},{"name":"2005","value":4},{"name":"rush2112","value":4},
{"name":"2001","value":4},{"name":"5555","value":4},{"name":"23skidoo","value":2},{"name":"m5wkqf","value":1},{"name":"stephen1","value":1}]
```

Example of  successful and unsuccessful run:

```
:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest>pytest -rA tests/test_top_param_password_complexity.py::test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True]
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest, configfile: pyproject.toml
collected 1 item

tests\test_top_param_password_complexity.py .                                                                                                                                    [100%]

======================================================================================= PASSES ========================================================================================
_____________________________________________________ test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True] _____________________________________________________
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '277', 'Connection': 'keep-alive', 'Date': 'Tue, 02 May 2023 23:08:41 GMT', 'x-amzn-RequestId': '365678ab-a8d3-4097-b73f-0b0a77215118', 'x-amz-apigw-id': 'EUSvCHl4IAMFa_Q=', 'X-Amzn-Trace-Id': 'Root=1-645197f9-63e7118b0450ebbf5631ac0a;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 573f3bf892e6baf323888f7038237db2.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': '1MA9Fplytk8eA3b7-2qVHiVN07x5jQ3FZcb7-WSpa5gp8LDIYD4xnQ=='}
RESPONSE CONTENT:  b'[{"name":"515000","value":6},{"name":"336699","value":6},{"name":"303030","value":6},{"name":"1223","value":4},{"name":"2005","value":4},{"name":"rush2112","value":4},{"name":"2001","value":4},{"name":"5555","value":4},{"name":"23skidoo","value":2},{"name":"m5wkqf","value":1}]'
EXPECTED PASSWORD COMPLEXITY RESULTS:  [{'name': '515000', 'value': 6}, {'name': '336699', 'value': 6}, {'name': '303030', 'value': 6}, {'name': '1223', 'value': 4}, {'name': '2005', 'value': 4}, {'name': 'rush2112', 'value': 4}, {'name': '2001', 'value': 4}, {'name': '5555', 'value': 4}, {'name': '23skidoo', 'value': 2}, {'name': 'm5wkqf', 'value': 1}]
=============================================================================== short test summary info ===============================================================================
PASSED tests/test_top_param_password_complexity.py::test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True]
================================================================================== 1 passed in 0.39s ==================================================================================

C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest>pytest -rA tests/test_top_param_password_complexity.py::test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True]
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest, configfile: pyproject.toml
collected 1 item

tests\test_top_param_password_complexity.py F                                                                                                                                    [100%]

====================================================================================== FAILURES =======================================================================================
_____________________________________________________ test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True] _____________________________________________________

data = './tests/testdata/users_0100.dat', top = 10, is_successful = True

    @pytest.mark.parametrize("data,top,is_successful",
                             [
                                 ("./tests/testdata/users_1_password_complexity.dat", None, True),
                                 ("./tests/testdata/users_multi_with_dups_password_complexities.dat", None, True),
                                 ("./tests/testdata/users_non_english_password_complexity.dat", None, True),
                                 ("./tests/testdata/users_all_US_keyboard_nonalpha_complexity.dat", None, True),
                                 ("./tests/testdata/users_0100.dat", 10, True)

                             ])
    def test_top_param_password_complexity(data, top, is_successful):
        sut = CensusToyService(data)
        sut_oracle = CensusToyResultsBuilder(sut.json_data)
        sut.actionType = ActionType.CountPasswordComplexity.value
        response = sut.retrieve_password_complexity(top)
        print('RESPONSE STATUS: ', response.status_code)
        print('RESPONSE HEADERS: ', response.headers)
        print('RESPONSE CONTENT: ', response.content)
        # expected HTTP status code
        if is_successful:
            assert response.status_code == 200
        else:
            assert response.status_code != 200
        # expected
        expected = sut_oracle.expected_password_complexity_results(top)
>       assert response.json() == expected
E       AssertionError: assert [{'name': '51...lue': 4}, ...] == [{'name': '51...lue': 4}, ...]
E         Left contains one more item: {'name': 'stephen1', 'value': 1}
E         Use -v to get more diff

tests\test_top_param_password_complexity.py:30: AssertionError
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Date': 'Tue, 02 May 2023 23:08:43 GMT', 'x-amzn-RequestId': 'e79bf242-7f6c-43bb-8d49-2ec87ef44bfb', 'x-amz-apigw-id': 'EUSvVHvpoAMF07Q=', 'X-Amzn-Trace-Id': 'Root=1-645197fb-1ef038444c0455a9438577b3;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 2b0c54ffe9876882253b010d44184bdc.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'eOyDVxm8F8dY9JVij8yUxeB7pZb2Y8F5-TzObadl8ybSwSzjIJudRw=='}
RESPONSE CONTENT:  b'[{"name":"515000","value":6},{"name":"336699","value":6},{"name":"303030","value":6},{"name":"1223","value":4},{"name":"2005","value":4},{"name":"rush2112","value":4},{"name":"2001","value":4},{"name":"5555","value":4},{"name":"23skidoo","value":2},{"name":"m5wkqf","value":1},{"name":"stephen1","value":1}]'
EXPECTED PASSWORD COMPLEXITY RESULTS:  [{'name': '515000', 'value': 6}, {'name': '336699', 'value': 6}, {'name': '303030', 'value': 6}, {'name': '1223', 'value': 4}, {'name': '2005', 'value': 4}, {'name': 'rush2112', 'value': 4}, {'name': '2001', 'value': 4}, {'name': '5555', 'value': 4}, {'name': '23skidoo', 'value': 2}, {'name': 'm5wkqf', 'value': 1}]
=============================================================================== short test summary info ===============================================================================
FAILED tests/test_top_param_password_complexity.py::test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True] - AssertionError: assert [{'name': '51...lue': 4}, ...] == [{'name': '51...lue': 4}, ...]
================================================================================== 1 failed in 0.52s ==================================================================================

```
## Steps to reproduce:

Run the following repeatedly:

```
pytest -rA --runxfail  tests/test_top_param_password_complexity.py::test_top_param_password_complexity[./tests/testdata/users_0100.dat-10-True]
```



