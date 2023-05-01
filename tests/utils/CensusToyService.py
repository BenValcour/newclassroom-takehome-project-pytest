import requests
import json
from enum import Enum


class ActionType(Enum):
    CountByGender = "CountByGender"
    CountByCoutry = "CountByCoutry"
    CountPasswordComplexity = "CountPasswordComplexity"
    Empty = ""
    Invalid = "NosuchAction"


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
            self._actionType = self._json_data['actionType']
            self._top = self._json_data['top']
            self.is_valid_json = True
        except ValueError:
            self._json_data = None
            self._actionType = None
            self._top = None
            self.is_valid_json = False

# Getters/Setters
    @property
    def actionType(self):
        return self._actionType

    @actionType.setter
    def actionType(self, value):
        self._actionType = value
        if self.is_valid_json:
            self._set_actionType(value)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value
        if self.is_valid_json:
            self._set_top(value)

    @property
    def json_data(self):
        return self._json_data

# Private things
    def _set_actionType(self, value):
        print("JSON DATA:\n", self._json_data)
        self._json_data['actionType'] = value

    def _set_top(self, top):
        self._json_data['top'] = top

    def _retrieve_results(self):
        if self.is_valid_json:
            response = self.post_toy_census_api(self._json_data)
        else:
            response = self.post_toy_census_api_raw(self._test_data)
        return response

# Public things
    def post_toy_census_api(self, valid_json_body):
        '''Used to call the Census Toy API with valid json body'''
        response = requests.post(self._TOY_CENSUS_URL, json=valid_json_body)
        return response

    def post_api_raw(self, raw_body):
        '''Used to call the Census Toy API with a post body that can be anything
            and bypass json checks in requests
        '''
        override_headers = {"Content-Type": "application/json"}
        response = requests.post(self._TOY_CENSUS_URL,
                                 raw_body, headers=override_headers)
        return response

    def retrieve_gender_count(self, top=None):
        self._set_actionType(ActionType.CountByGender.value)
        self._set_top(top)
        return self._retrieve_results()

    def fetch_country_count(self, top=None):
        self._set_actionType(ActionType.CountByCoutry.value)
        return self._retrieve_results()

    def fetch_password_complexity(self, top=None):
        self._set_actionType(ActionType.CountPasswordComplexity.value)
        return self._retrieve_results()
