from testloader import TestLoader
from testrunner import TestRunner
from test_loader_test import TestLoaderTest

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)