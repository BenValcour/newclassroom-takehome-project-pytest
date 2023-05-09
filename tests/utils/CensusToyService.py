import requests
import json
from enum import Enum


class ActionType(Enum):
    '''List of possible action values to be used for testing.'''
    CountByGender = "CountByGender"
    CountByCountry = "CountByCountry"
    CountPasswordComplexity = "CountPasswordComplexity"
    Empty = ""
    Invalid = "NosuchAction"

# TODO - seems a lot of redundant code, refactor...


class CensusToyService:
    '''Supports end to end testing of the Census Toy API service.
        allows for submission of valid and invalid JSON for positive 
        and negative test cases
    '''

    _TOY_CENSUS_URL = "https://census-toy.nceng.net/prod/toy-census"

    def __init__(self, test_data_file):
        '''process test data form input file, assumed to be a json body for a post request 
            to the Census Toy Service.   For test purpose, it may be valid or invalid JSON.
        '''
        self.test_data_file = test_data_file
        self._test_data = None
        try:
            with open(test_data_file, 'r') as file:
                self._test_data = file.read()
            self._json_data = json.loads(self._test_data)
            if 'actionType' in self._json_data:
                self._actionType = self._json_data['actionType']
            if 'top' in self._json_data:
                self._top = self._json_data['top']
            self._is_valid_json = True
        except ValueError:
            self._json_data = None
            self._actionType = None
            self._top = None
            self._is_valid_json = False


# Getters/Setters

    @property
    def actionType(self):
        return self._actionType

    @actionType.setter
    def actionType(self, value: str):
        self._actionType = value
        if self._is_valid_json:
            self._set_actionType(value)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value
        if self._is_valid_json:
            self._set_top(value)

    def remove_top(self):
        ''' removes the top property from the request body
            if the top property does not exist, no error is returned.
            if the request body is not valid json, no error is returned.
        '''
        if self._is_valid_json:
            if "top" in self._json_data:
                del self._json_data["top"]

    @property
    def json_data(self):
        return self._json_data


# Private things

    def _set_actionType(self, value: str):
        self._json_data['actionType'] = value

    def _set_top(self, top):
        self._json_data['top'] = top

    def _post_toy_census_api(self, valid_json_body):
        '''Used to call the Census Toy API with valid json body'''
        response = requests.post(self._TOY_CENSUS_URL, json=valid_json_body)
        return response

    def _post_toy_census_api_raw(self, raw_body):
        '''Used to call the Census Toy API with a post body that can be anything
            and bypass json checks in requests
        '''
        override_headers = {"Content-Type": "application/json"}
        response = requests.post(self._TOY_CENSUS_URL,
                                 raw_body, headers=override_headers)
        return response


# Public things

    def retrieve_results(self):
        if self._is_valid_json:
            # print('REQUEST_DATA(valid): ', self._json_data)
            response = self._post_toy_census_api(self._json_data)
        else:
            # print('REQUEST_DATA(invalid): ', self._test_data)
            response = self._post_toy_census_api_raw(self._test_data)
        return response

    def retrieve_gender_count(self, top=None):
        self._set_actionType(ActionType.CountByGender.value)
        self._set_top(top)
        return self.retrieve_results()

    def retrieve_country_count(self, top=None):
        self._set_actionType(ActionType.CountByCountry.value)
        self._set_top(top)
        return self.retrieve_results()

    def retrieve_password_complexity(self, top=None):
        self._set_actionType(ActionType.CountPasswordComplexity.value)
        self._set_top(top)
        return self.retrieve_results()
