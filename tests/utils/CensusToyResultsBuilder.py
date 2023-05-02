import json
import re

# TODO - seems a lot of redundant code, refactor...


class CensusToyResultsBuilder:
    ''' CensusToyResultsBuilder is the oracle that provides expected results
        based on the test data provided.
    '''

    def __init__(self, user_data):
        ''' user_data is expected to be valid json format (aka Python Dictionary). 
        '''
        self._json_data = user_data


# Private methods


    def _get_gender_results(self):
        counts = {}
        results = []

        for user in self._json_data['users']:
            if user['gender'] in counts:
                counts[user['gender']] += 1
            else:
                counts[user['gender']] = 1

        for key in counts:
            results.append({"name": key, "value": counts[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        print('EXPECTED GENDER RESULTS: ', results)

        return results

    def _get_country_results(self):
        counts = {}
        results = []

        for user in self._json_data['users']:
            if user['nat'] in counts:
                counts[user['nat']] += 1
            else:
                counts[user['nat']] = 1
        for key in counts:
            results.append({"name": key, "value": counts[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        print('EXPECTED COUNTRY RESULTS: ', results)

        return results

    def _get_password_complexity_results(self):
        counts = {}
        results = []

        for user in self._json_data['users']:
            complexity = self._calculate_complexity(user["login"]["password"])
            if complexity in counts:
                counts[complexity] += 1
            else:
                counts[complexity] = 1

        for key in counts:
            results.append({"name": key, "value": counts[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        print('EXPECTED PASSWORD COMPLEXITY RESULTS: ', results)

        return results

    def _calculate_complexity(self, password):
        return len(password) - len(re.findall(r'[^\W\d_]{1}', password))

# Public methods
    def expected_gender_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (gender), and value (count).
            If top is None, returns the entire results.  Otherwise,
            returns the first top results.            
        '''
        gender_counts = self._get_gender_results()
        return gender_counts[:top]

    def expected_country_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (nat), and value (count)
            If top is None, returns the entire results.  Otherwise,
            returns the first top results.
        '''
        country_counts = self._get_country_results()
        return country_counts[:top]

    def expected_password_complexity_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (complexity), and value (count).
            If top is None, returns the entire results.  Otherwise,
            returns the first top results.
        '''
        country_counts = self._get_password_complexity_results()
        return country_counts[:top]
