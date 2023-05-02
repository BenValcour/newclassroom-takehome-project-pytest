# newclassroom-takehome-project-pytest
 Qa automation engineer take home test pytest implementation.

 This project supports the testing of the Census Toy Service API as described in the project definition.

 ## How to run

Tests were developed on a Windows 10 platform.  It is suggested you use same. To run the tests:

1. clone the repo
2. install the following python modules and versions
- python 3.11.2
- pytest 7.2.2
- requests 2.29.0
3. position to the project folder, so that the tests folder is in the curent working directory.
4. run pytest [-v]

 ## Testing approach and assumptions

The testing approach is constrained to functional testing of the Census Toy Service call.   This includes both positive and negative behaviors.   Testing does not include non-functional evaluation.  For example, no performance, load, reliability, or security testing was performed.

### Five primary items were considered for testing:

1. actionType property - This property was viewed as a string value that has 3 valid inputs and anything else would be invalid (client error).  
2. top property - This property was viewed as an  int value that  was valid for values > 0.   For all other values, the value was invalid (client error). For example values of -1 and 0 are expected to return a client error.  Performed boundary value testing for integer values (-1,0,1,2,n) Where n was relevant to the users data and the results generated. n == size(results), n < size(results), and n > size(results)
3. users array - The length of the array must be > 0.   missing or empty users array is invalid (client error)  Array lengths of 1,2,n were tested.   Additionally, the testdata was modified for specific test cases to create an expectation to match the test case.   For example:  test data that would return count by country of 5 countries each with differing counts (for sort verification) was created.
4. The content of the request (request body) - testing of this was for both valid and invalid json.  Invalid json formatted body should return a client error.
5. The content of the response - 

### General testing includes:
- For error cases for the properties consider:  missing, empty strings or arrays, and no value, (null)
- Client errors are assumed to return a non-200 response.  Specifically, looking for responses in the 400 range as part of expectations.

###  Test assumptions

- The "nat" property is the value used to control the  CountByCountry feature.  The "country" property in the location object is ignored as part of testing.
- The value of the "password" property is assumed to be valid US keyboard input.
- The users data may be incomplete.  That is, for a successful user response, the user object will have all properties present, but may contain properties with empty values.  For example, Users[0]["Gender"] might be null or an empty string.  These scenarios are considered for error cases and validating service behavior with missing/unepxected values.

 ## Implementation

The tests are implemented using python/pytest with the requests module.   The test data is static and was created using the https://randomuser.me/api site for the initial data and then modified for specific test cases.

Why did I use python: 
- Quick and simple to implement using open source SW
- Supports the functional testing only assumption
- Easy to share with others
- requests module support submission of valid/invalid post requests
- pytest gives a simple and well known reporting model
- Python was one of the languages raised in the job description :-) 

bugs  - defines any issues encountered with the service under test (SUT).   Failing tests are marked with xfail.
tests - test case code
tests\testdata - test data files
tests\utils - class(es) used by the test harness, and some helper tools for creating test data.

