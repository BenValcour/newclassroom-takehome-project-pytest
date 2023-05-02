import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,top,is_successful",
                         [
                             ("./tests/testdata/user_1_CA.dat", 1, True),
                             ("./tests/testdata/users_2_US.dat", 2, True),
                             ("./tests/testdata/users_3_BG.dat", 3, True),
                             ("./tests/testdata/users_3_BG.dat", 2, True),
                             ("./tests/testdata/users_3_BG.dat", 0, True),
                             pytest.param("./tests/testdata/users_0100.dat", 10, True, marks=pytest.mark.xfail(
                                 reason="Not honoring sort, US entry appears first in the list regardless of count.")),
                             pytest.param("./tests/testdata/users_2_CA_1_BG_3_US.dat", 3, True, marks=pytest.mark.xfail(
                                 reason="Test not reliable, result is missing expected country")),
                             ("./tests/testdata/users_2_CA_1_BG_3_BR.dat", 2, True),
                             pytest.param("./tests/testdata/users_3_CA_1_BG_2_US.dat", 4, True, marks=pytest.mark.xfail(
                                 reason="Not honoring sort, US entry appears first in the list regardless of count.")),
                             ("./tests/testdata/users_2_CA_1_BG_3_US.dat", 4, True)
                         ])
def test_top_param_country(data, top, is_successful):
    sut = CensusToyService(data)
    sut_oracle = CensusToyResultsBuilder(sut.json_data)
    sut.actionType = ActionType.CountByCountry.value
    response = sut.retrieve_country_count(top)
    print('RESPONSE STATUS: ', response.status_code)
    print('RESPONSE HEADERS: ', response.headers)
    print('RESPONSE CONTENT: ', response.content)
    # expected HTTP status code
    if is_successful:
        assert response.status_code == 200
    else:
        assert response.status_code != 200
    # expected
    expected = sut_oracle.expected_country_results(top)
    assert response.json() == expected
