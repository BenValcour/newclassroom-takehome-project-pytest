import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,http_response_code_level",
                         [
                             ("./tests/testdata/request_invalid_json.dat", 400),
                             pytest.param("./tests/testdata/request_no_users_in_users_array.dat", 400, marks=pytest.mark.xfail(
                                 reason="Bug - expected request with empty users array to return 400 status code")),
                             pytest.param("./tests/testdata/request_missing_required_field.dat", 400, marks=pytest.mark.xfail(
                                 reason="Bug - expected missing actionType to return 400 status code")),
                             pytest.param("./tests/testdata/request_invalid_actiontype.dat", 400, marks=pytest.mark.xfail(
                                 reason="Bug - expected invalid actionType to return 400 status code")),
                             pytest.param("./tests/testdata/request_no_users_data.dat", 400, marks=pytest.mark.xfail(
                                 reason="Bug - expected request with not users array to return 400 status code"))
                         ])
def test_request_errors(data, http_response_code_level):
    sut = CensusToyService(data)
    response = sut.retrieve_results()
    print('RESPONSE STATUS: ', response.status_code)
    print('RESPONSE HEADERS: ', response.headers)
    print('RESPONSE CONTENT: ', response.content)
    assert response.status_code == http_response_code_level
