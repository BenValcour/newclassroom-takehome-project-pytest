import json


class CensusToyResultsBuilder:
    ''' CensusToyResultsBuilder is the oracle that provides expected results
        based on the test data provided.
    '''

    def __init__(self, user_data):
        self._json_data = user_data


# Private methods


    def _get_gender_results(self):
        print('_get_gender_results - Enter ')
        counts = {}
        results = []

        print('_get_gender_results - for -1 ')

        for user in self._json_data['users']:
            if user['gender'] in counts:
                counts[user['gender']] += 1
            else:
                counts[user['gender']] = 1

        print('_get_gender_results - for -2 ')

        for key in counts:
            results.append({"name": key, "value": counts[key]})

        print('_get_gender_results - Exit ')

        print('COUNTS: ', counts)

        print('RESULTS: ', results)
        return results

    def _get_country_results(self):
        counts = {}
        results = []

        for user in self._json_data['users']:
            if user['nat'] in counts:
                counts[user['nat']] += 1
            else:
                counts[user['nat']] = 1

        for nat, count in counts:
            results.append({"name": nat, "value": count})

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

        for complexity, count in counts:
            results.append({"name": complexity, "value": count})

        return results

    def _calculate_complexity(self, password):
        return 0

# Public methods
    def expected_gender_results(self, top):
        ''' Returns an array of dictionaries, each dictionary 
            has two items, name (gender), and value (count)
        '''
        print('expected_gender_results - Enter ')
        gender_counts = self._get_gender_results()
        return gender_counts[:top]

    def expected_country_results(self, top):
        pass

    def expected_password_complexity_results(self, top):
        pass
