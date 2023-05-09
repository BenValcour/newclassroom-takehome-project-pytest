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
            if 'gender' in user:
                if user['gender'] in counts:
                    counts[user['gender']] += 1
                else:
                    counts[user['gender']] = 1

        for key in counts:
            results.append({"name": key, "value": counts[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        return results

    def _get_country_results(self):
        counts = {}
        results = []

        for user in self._json_data['users']:
            if 'nat' in user:
                if user['nat'] in counts:
                    counts[user['nat']] += 1
                else:
                    counts[user['nat']] = 1

        for key in counts:
            results.append({"name": key, "value": counts[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        return results

    def _get_password_complexity_results(self):
        passwords = {}
        results = []

        for user in self._json_data['users']:
            if 'login' in user and 'password' in user['login']:
                complexity = self._calculate_complexity(
                    user["login"]["password"])
                passwords[user["login"]["password"]] = complexity

        for key in passwords:
            results.append({"name": key, "value": passwords[key]})

        # sort to match  expectations
        results.sort(key=lambda x: x['value'], reverse=True)

        return results

    def _calculate_complexity(self, password):
        ''' calculate how many non alpha numeric values exist in the password.
            'w'  is any alphanumeric (any language) including the underscore, '_".
             However, "_" adds to the complexity calculation.
            So then find "_" and add them back into the complexity calculation
        '''
        # return len(password) - len(re.findall(r'[^\W\d_]{1}', password))
        alnum_and_underscores = len(re.findall(r'[\w]', password))
        underscores_only = len(re.findall(r'[_]', password))
        print(f"PASSWORD: \"{password}\", len(password)", len(password))
        return len(password) - alnum_and_underscores + underscores_only

# Public methods
    def expected_gender_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (gender), and value (count).
            If top is None, or top <= 0, returns the entire results.  Otherwise,
            returns the first top results.          
        '''
        gender_counts = self._get_gender_results()
        if (top != None) and (top > 0):
            results = gender_counts[:top]
        else:
            results = gender_counts

        print('EXPECTED GENDER RESULTS: ', results)
        return results

    def expected_country_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (nat), and value (count)
            If top is None, or top <= 0, returns the entire results.  Otherwise,
            returns the first top results.
        '''
        country_counts = self._get_country_results()
        if (top != None) and (top > 0):
            results = country_counts[:top]
        else:
            results = country_counts

        print('EXPECTED COUNTRY RESULTS: ', results)
        return results

    def expected_password_complexity_results(self, top=None):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (password), and value (complexity).
            If top is None, or top <= 0, returns the entire results.  Otherwise,
            returns the first top results.
        '''
        passwords = self._get_password_complexity_results()
        if (top != None) and (top > 0):
            results = passwords[:top]
        else:
            results = passwords

        print('EXPECTED PASSWORD COMPLEXITY RESULTS: ', results)
        return results
