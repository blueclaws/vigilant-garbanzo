import unittest
import mod

class TestMod(unittest.TestCase):

    def setUP(self):
        print("setting up...\n")

    def tearDown(self):
        print('Tearing down...\n')

    def test_func(self):
        self.assertIn(mod.func(), mod.x)
    
    def test_imlol(self):
        self.assertEqual(mod.imlol(), 'Shiet nigga')

    @unittest.skip("SKIPPING")
    def test_div(self):
        self.assertEqual(mod.div(1, 2), 0)
    
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMod('test_div'))
    #suite.addTest(TestMod('test_func'))
    #suite.addTest(TestMod('test_imlol'))
    return suite


if __name__ == '__main__':
    #unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())