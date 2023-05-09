# Issue: CountPasswordComplexity is returning duplicate passwords

## Severity (Critical/Major/Minor/Low): Low

## Priority (High/Medium/Low): Low

## Description:

This is more of a clarification issue. The results of the CountPasswordComplexity has multiple entries for the same password.   This does not appear consistent with the requirements.  Not seeing value in reporting on the same password?

Given a request with two users with the same password. Expecting the results to have a single name/value entry.  Instead observed the same entry, duplicated.

## Steps to reproduce:

Run the following test:

```
pytest -rA --runxfail  tests/test_count_password_complexity.py::test_count_password_complexity[./tests/testdata/users_passwords_duplicate.dat-None-True]

```


