# Issue: users data that has no countable property is returning results

## Severity (Critical/Major/Minor/Low): Low

## Priority (High/Medium/Low): Low

## Description:

user data was adjusted so that no user entries had a nat property.  Same was done for gender test data.

expectation:  no results would be returned.

observed the following result (for missing 'nat' property):

```
Response content:  [{"name":null,"value":2}]
```

expected content:  []

Similar behavior observed for the CountByGender action. 

## Steps to reproduce:

Run the following test to observe the behavior.

```
pytest -rA tests/test_count_by_country.py::test_count_by_country[./tests/testdata/users_no_countries.dat-None-True]
```

or

```
pytest -rA tests/test_count_by_gender.py::test_count_by_gender[./tests/testdata/users_no_genders.dat-None-True]
```


