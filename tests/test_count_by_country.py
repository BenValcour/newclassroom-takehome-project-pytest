import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,top,is_successful",
                         [
                             ("./tests/testdata/users_0015.dat", None, True),
                             pytest.param("./tests/testdata/users_1000.dat", None, True, marks=pytest.mark.xfail(
                                 reason="Not honoring sort, US entry appears first in the list regardless of count.")),
                             ("./tests/testdata/user_1_CA.dat", None, True),
                             ("./tests/testdata/users_2_US.dat", None, True),
                             ("./tests/testdata/users_3_BG.dat", None, True),
                             ("./tests/testdata/user_invalid_country_code.dat", None, True),
                             pytest.param("./tests/testdata/users_no_countries.dat", None, True, marks=pytest.mark.xfail(
                                 reason="Check requirements: Service is counting missing nat properties.")),
                             ("./tests/testdata/users_2_CA_1_BG_3_US.dat", None, True),
                             pytest.param("./tests/testdata/users_3_CA_1_BG_2_US.dat", None, True, marks=pytest.mark.xfail(
                                 reason="Not honoring sort, US entry appears first in the list regardless of count."))
                         ])
def test_count_by_country(data, top, is_successful):
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
