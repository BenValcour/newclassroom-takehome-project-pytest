import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,top,is_successful",
                         [
                             ("./tests/testdata/users_0010.dat", None, True),
                             ("./tests/testdata/users_0010.dat", 10, True),
                             ("./tests/testdata/users_0010.dat", 11, True),
                             ("./tests/testdata/users_0010.dat", 9, True),
                             ("./tests/testdata/users_0010.dat", 1, True),
                             ("./tests/testdata/users_0010.dat", 0, True),
                             ("./tests/testdata/users_0010.dat", -1, True)

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
    assert response.json() == expected
