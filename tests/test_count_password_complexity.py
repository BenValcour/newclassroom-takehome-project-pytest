import pytest
from utils.CensusToyService import CensusToyService, ActionType
from utils.CensusToyResultsBuilder import CensusToyResultsBuilder


@pytest.mark.parametrize("data,top,is_successful",
                         [
                             ("./tests/testdata/users_password_encoded_non-alphanumeric.dat", None, True),
                             ("./tests/testdata/users_1_password_complexity.dat", None, True),
                             ("./tests/testdata/users_multi_with_dups_password_complexities.dat", None, True),
                             ("./tests/testdata/users_non_english_password_complexity.dat", None, True),
                             pytest.param("./tests/testdata/users_all_US_keyboard_alphanumeric_complexity.dat", None, True,
                                          marks=pytest.mark.xfail(reason="Counting numeric characters.")),
                             ("./tests/testdata/users_all_US_keyboard_non-alphanumeric_complexity.dat", None, True),
                             pytest.param("./tests/testdata/users_1000.dat", None, True,
                                          marks=pytest.mark.xfail(reason="duplicate passwords are not de-duped.")),
                             pytest.param("./tests/testdata/users_5000.dat", None, True,
                                          marks=pytest.mark.xfail(reason="duplicate passwords are not de-duped.")),
                             ("./tests/testdata/user_no_password.dat", None, True),
                             pytest.param("./tests/testdata/users_passwords_duplicate.dat", None, True,
                                          marks=pytest.mark.xfail(reason="Duplicate passwords are not de-duped.")),
                             ("./tests/testdata/users_password_backslash_character_success.dat", None, True),
                             pytest.param("./tests/testdata/users_password_backslash_character_fails.dat", None, True,
                                          marks=pytest.mark.xfail(reason="Counts fail under certain sequences with backslash characters.")),
                             ("./tests/testdata/user_password_empty.dat", None, True)
                         ])
def test_count_password_complexity(data, top, is_successful):
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
    print('RESPONSE: ', response.json())
    print('SIZE RESPONSE: ', len(response.json()))
    print('SIZE EXPECTED: ', len(expected))
    assert response.json() == expected
