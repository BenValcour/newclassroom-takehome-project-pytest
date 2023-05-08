# newclassroom-takehome-project-pytest
 QA automation engineer take home test pytest implementation.

 This project supports the testing of the Census Toy Service API as described in the project definition.

## Test results

### What works:

- Each of the actionTypes work for general use cases.
- The top parameter works for most requests.
- The calculation of password complexity seems to work as expected.
- Requests with 1000 and 5000 users was successfully processed.

### What does not work:

See the [bugs](bugs) folder for details:

- The sorting of the results is not functional for countByCountry.  US seems to always have priority when present.
- Occasionally, the service returns unexpected results. That is more or fewer results than expected.  On some occasions observed an empty results when non-empty was expected.
- Duplicate passwords are reported for CountPasswordComplexity.  This might be by design, but seems inconsistent with other actionTypes
- The service does not respond with client errors status code (400) when a request is sent with invalid or missing required fields. 
- For countByCountry the service will count users that do not have a 'nat' property. May not be an issue, as expected behavior is not defined for this case.

### Comment on features

- For security reasons, the countPasswordComplexity action should probably not be reporting passwords in the results. It might be of more value to report the complexity as the 'name' property, and the 'value' property as the frequency of complexity value occurring in the users array.  This would provide users with a sorted summary of how complex the passwords are for the given users array.  It would also be consistent with other service actionType behaviors.

## How to run

Tests were developed on a Windows 10 platform.  VS Code was used as the IDE. It is suggested you use same. To run the tests:

1. clone the repo
2. install the following python modules and versions
- python 3.11.2
- pytest 7.2.2
- requests 2.29.0
3. position to the project folder, so that the tests folder is in the current working directory.
4. run pytest [-v|-rA], use **-rA** for detailed test output.  Use **--runxfail** to run tests marked as failed.

 ## Testing approach and assumptions

The testing approach is constrained to functional testing of the Census Toy Service call.   This includes both positive and negative behaviors.  Testing approach looked at the domain of the inputs and applied boundary value test case.  Testing did not include non-functional evaluation.  For example, no performance, load, reliability, or security testing was performed.

### Five primary items were considered for testing:

1. actionType property - This property was viewed as a string value that has 3 valid inputs and anything else would be invalid (client error).  
2. top property - This property was viewed as an  int value that  was valid for values > 0.   For all other values, the value was invalid (client error). For example values of -1 and 0 are expected to return a client error.  Performed boundary value testing for integer values (-1,0,1,2,n) Where n was relevant to the users data and the results generated. n == size(results), n < size(results), and n > size(results)
3. users array - The length of the array must be > 0.   missing or empty users array is invalid (client error)  Array lengths of 1,2,n were tested.   Additionally, the test data was modified for specific test cases to create an expectation to match the test case.   For example:  test data that would return count by country of 5 countries each with differing counts (for sort verification) was created.
4. The content of the request (request body) - testing of this was for both valid and invalid json.  Invalid json formatted body should return a client error.
5. The content of the response - Verifying client errors, invalid requests/values, return an expected 400 level response.

### General testing includes:
- For error cases for the properties consider:  missing, empty strings or arrays, and no value, (null)
- Client errors are assumed to return a non-200 response.  Specifically, looking for responses in the 400 range as part of expectations.

###  Test assumptions

- The "nat" property is the value used to control the  countByCountry action.  The "country" property in the "location" object is ignored as part of testing.
- The value of the "password" property is assumed to be valid keyboard input. Consideration is made for testing of passwords that have non-English language alphabetic characters.
- For countPasswordComplexity results, it is assumed the name is the password, and the value is its complexity. It is assumed the result set should not contain duplicate name entries.
- The users data may be incomplete.  That is, for a successful user response, the user object will have all properties present, but may contain properties with empty values.  For example, Users[0]["Gender"] might be null or an empty string.  These scenarios are considered for error cases and verifying service behavior with missing/unexpected values.

 ## Implementation

The tests are implemented using python/pytest with the requests module.   The test data is static, located in the test data folder, and was created using the https://randomuser.me/api site for the initial data and then modified for specific test cases.

Why did I use python: 
- Quick and simple to implement using open-source SW
- Supports the functional testing only assumption
- Easy to share with others
- requests module support submission of valid/invalid post requests
- pytest gives a simple and well-known reporting model
- Python was one of the languages raised in the job description :-) 

bugs  - Potential defects. Defines any issues encountered with the service under test (SUT).   Failing tests are marked with xfail.

#### Folders:

- tests - test case code
- tests\testdata - test data files
- tests\utils - class(es) used by the test harness, and some helper tools for creating test data.

### Classes of interest

#### CensusToyService

Provides an abstraction of the Census Toy Service implementation to hide API changes from the test.   The class does also provide the ability to specify 'raw'  HTTP POST request body content.   The later can be used for error testing. Such as sending invalid JSON content.

#### CensusToyResultsBuilder

Provides the expectations, which are calculated  at run time. Expectations are based on the content of the test data file, and the value of the optional **top** parameter.   Took this approach to avoid having implementation details in the actual test case code.  This provides a single location, class, that would have to be updated if/when minor changes in the service API  expectations are implemented.

## To add more tests

Most of the tests are data driven, thus adding new tests consists of creating a data set.
In the utils folder there are the scripts: **get_testdata.py** and **get_expectations.py**.  
- **get_testdata.py** can be used to create test data files that contain a json object that can be used to query the Census Toy Service.   
- **get_expectations.py** takes an argument of a valid test data file, and optionally a value for the top parameter, and reports the expectations based on the data in the file.

## TODOs

- The tests were broken up into functional areas.   This resulted in some duplicate code within the test cases.  Probably worth a refactor.

- The two classes mentioned above also suffer from common boilerplate code.  Refactoring might be advised.

- The test data files could be better organized.  A naming convention could be defined and used.

- As there is a "contract" between the Census service and the format of the users object returned by the randomuser service, it would be of value to identify any breaking changes in the randomuser service.  A test case that confirms the  schema of the users data  from the randomuser service has not introduced a breaking change should be implemented.