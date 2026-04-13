from testcase import TestCase
from testresult import TestResult

class MyTest(TestCase):

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")


result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())