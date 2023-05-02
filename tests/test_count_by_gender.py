import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,top,is_successful",
                         [
                             ("./tests/testdata/user_1_female.dat", 1, True),
                             ("./tests/testdata/users_2_female_1_male.dat", 2, True)
                         ])
def test_count_by_gender(data, top, is_successful):
    sut = CensusToyService(data)
    sut_oracle = CensusToyResultsBuilder(sut.json_data)
    sut.actionType = ActionType.CountByGender.value
    response = sut.retrieve_gender_count(top)
    print('RESPONSE STATUS: ', response.status_code)
    print('RESPONSE CONTENT: ', response.content)
    # expected HTTP status code
    if is_successful:
        assert response.status_code == 200
    else:
        assert response.status_code != 200
    # expected
    expected = sut_oracle.expected_gender_results(top)
    assert response.json() == expected
