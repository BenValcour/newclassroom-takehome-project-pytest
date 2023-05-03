# Issue: Sort order is not being honored for the CountByCountry

## Severity (Critical/Major/Minor/Low): Major

## Priority (High/Medium/Low): High

## Description:

With test data that has 3 country codes with the following counts:
US-2
CA-3
BR-1

Would expect the order to be:   CA, US, BR

Actual order reported is:  US, CA, BR

## Steps to reproduce:

Run the following test:

```
pytest --runxfail -rA tests/test_top_param_country.py::test_top_param_country[./tests/testdata/users_3_CA_1_BG_2_US.dat-4-True]
```



