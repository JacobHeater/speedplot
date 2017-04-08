import unittest
import sys

sys.path.append('./')

loader = unittest.TestLoader()
start_dir = './tests'
entity_suite = loader.discover(start_dir, 'entitytests.py')
db_suite = loader.discover(start_dir, 'databasetests.py')
test_suites = [entity_suite, db_suite]
runner = unittest.TextTestRunner()
success = True

for suite in test_suites:
    wasSuccessful = runner.run(suite).wasSuccessful()
    if not wasSuccessful:
        success = wasSuccessful

if not success:
    sys.exit(success)