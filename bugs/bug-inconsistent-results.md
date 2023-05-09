# Issue: Inconsistent results

## Severity (Critical/Major/Minor/Low): Critical

## Priority (High/Medium/Low): High

## Description:

Observing during test runs the service will return a different result.   Content-length matches the return, and the response returned is well formed json.  Assuming a server side issue.

From below,  the output of a successful and unsuccessful test run.

```
C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest>pytest -rA tests/test_top_param_gender.py::test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True]
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest, configfile: pyproject.toml
collected 1 item

tests\test_top_param_gender.py .                                                                                                                                                 [100%]

======================================================================================= PASSES ========================================================================================
______________________________________________________ test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True] _______________________________________________________
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '55', 'Connection': 'keep-alive', 'Date': 'Tue, 02 May 2023 21:28:52 GMT', 'x-amzn-RequestId': '0a46b804-3ee9-451f-a155-5f0cedc73902', 'x-amz-apigw-id': 'EUEHNHrZIAMFv8g=', 'X-Amzn-Trace-Id': 'Root=1-64518094-491ab0c87f13c5b5778925b2;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 5840e9664aef77d9be1f708259e60d56.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'gImSyBJbz6I2_bBumTCWKT1Us-Y62L2YQuyLE4_HUo1JITIYbLSu-A=='}
RESPONSE CONTENT:  b'[{"name":"female","value":2},{"name":"male","value":1}]'
EXPECTED GENDER RESULTS:  [{'name': 'female', 'value': 2}, {'name': 'male', 'value': 1}]
=============================================================================== short test summary info ===============================================================================
PASSED tests/test_top_param_gender.py::test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True]
================================================================================== 1 passed in 0.34s ==================================================================================

C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest>pytest -rA tests/test_top_param_gender.py::test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True]
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\JobSearch\Companies\NewClassroom\TakeHomeProject\newclassroom-takehome-project-pytest, configfile: pyproject.toml
collected 1 item

tests\test_top_param_gender.py F                                                                                                                                                 [100%]

====================================================================================== FAILURES =======================================================================================
______________________________________________________ test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True] _______________________________________________________

data = './tests/testdata/users_2_female_1_male.dat', top = 2, is_successful = True

    @pytest.mark.parametrize("data,top,is_successful",
                             [
                                 ("./tests/testdata/user_1_male.dat", 0, True),
                                 ("./tests/testdata/users_2_female_1_male.dat", None, True),
                                 ("./tests/testdata/users_2_female_1_male.dat", 2, True),
                                 ("./tests/testdata/users_2_female_1_male.dat", 3, True),
                                 ("./tests/testdata/users_2_female_1_male.dat", 1, True),
                                 ("./tests/testdata/users_1000.dat", 1, True),
                                 ("./tests/testdata/users_5000.dat", 2, True),
                                 ("./tests/testdata/users_3_unknown_2_female_1_male.dat", 2, True)
                             ])
    def test_top_param_gender(data, top, is_successful):
        sut = CensusToyService(data)
        sut_oracle = CensusToyResultsBuilder(sut.json_data)
        sut.actionType = ActionType.CountByGender.value
        response = sut.retrieve_gender_count(top)
        print('RESPONSE STATUS: ', response.status_code)
        print('RESPONSE HEADERS: ', response.headers)
        print('RESPONSE CONTENT: ', response.content)
        # expected HTTP status code
        if is_successful:
            assert response.status_code == 200
        else:
            assert response.status_code != 200
        # expected
        expected = sut_oracle.expected_gender_results(top)
>       assert response.json() == expected
E       AssertionError: assert [{'name': 'fe..., 'value': 2}] == [{'name': 'fe..., 'value': 1}]
E         Right contains one more item: {'name': 'male', 'value': 1}
E         Use -v to get more diff

tests\test_top_param_gender.py:32: AssertionError
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
RESPONSE STATUS:  200
RESPONSE HEADERS:  {'Content-Type': 'application/json', 'Content-Length': '29', 'Connection': 'keep-alive', 'Date': 'Tue, 02 May 2023 21:28:54 GMT', 'x-amzn-RequestId': '273ecbc7-76b5-4b08-b7e0-07c5e84279a6', 'x-amz-apigw-id': 'EUEHhEofIAMFeVQ=', 'X-Amzn-Trace-Id': 'Root=1-64518096-6a4ddcb34e9531f52a94d57a;Sampled=0;lineage=6e69f56a:0', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 1bd7d779bed244375679d82e1821cc3c.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'IAD89-P2', 'X-Amz-Cf-Id': 'RjWdjnutzlIC1al-HfRtXFNlmdZr2Ul4M3wLVgu3iVtKzOURQ3ZwTQ=='}
RESPONSE CONTENT:  b'[{"name":"female","value":2}]'
EXPECTED GENDER RESULTS:  [{'name': 'female', 'value': 2}, {'name': 'male', 'value': 1}]
=============================================================================== short test summary info ===============================================================================
FAILED tests/test_top_param_gender.py::test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True] - AssertionError: assert [{'name': 'fe..., 'value': 2}] == [{'name': 'fe..., 'value': 1}]
================================================================================== 1 failed in 0.41s ==================================================================================

```

## Steps to reproduce:

Run the following test repeatedly until a failure is observed:

```
pytest -rA --runxfail  tests/test_top_param_gender.py::test_top_param_gender[./tests/testdata/users_2_female_1_male.dat-2-True]
```



