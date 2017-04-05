import unittest

loader = unittest.TestLoader()
start_dir = './tests'
entity_suite = loader.discover(start_dir, 'entitytests.py')
db_suite = loader.discover(start_dir, 'databasetests.py')

runner = unittest.TextTestRunner()
runner.run(entity_suite)
runner.run(db_suite)