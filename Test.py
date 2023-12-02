import unittest


def run_all_test():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(loader.discover("TestClass"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_all_test()
