import requests
import json
import os
import sys
import argparse

from CensusToyResultsBuilder import CensusToyResultsBuilder


if __name__ == '__main__':
    '''Given a testdata file.  Process the file  to report the expectations
      for each actionType.
    '''
    parser = argparse.ArgumentParser(
        description="Reports expectations for a given, valid, test data file.")
    parser.add_argument(
        '-top', help='If TOP is supplied, the expected results will be truncated accordingly.')

    parser.add_argument(
        'file', help='Valid test data file from get_testdata.py.')
    args = parser.parse_args()
    print(args)
    file_name = args.file.strip()

    if args.top:
        top = int(args.top.strip())
    else:
        top = None
    with open(file_name, 'r') as file:
        test_data = file.read()
    json_data = json.loads(test_data)

    builder = CensusToyResultsBuilder(json_data)

    # relying on the class having print statements for expectations.
    # if not, wrap these in print() stmts.
    builder.expected_gender_results(top)
    builder.expected_country_results(top)
    builder.expected_password_complexity_results(top)
