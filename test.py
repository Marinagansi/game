import unittest
import login
import signuppage

class Test_loginCredential(unittest.TestCase):
    def test_set1(self):
        status = login.show_found_status("a", "r")
        self.assertEqual(status, "account found")
    def test_set2(self):
        status = login.show_found_status("bb", "nn")
        self.assertEqual(status, "account not found")

    def test_set3(self):
        status = signuppage.get_status(0)
        self.assertEqual(status,"signup failed")
    def test_set4(self):
        status = signuppage.get_status(1)
        self.assertEqual(status,"signup successfull")
    def test_set5(self):
        status = signuppage.set_status(1)
        self.assertEqual(status, "insert value completed")
    def test_set6(self):
        status = signuppage.set_status(0)
        self.assertEqual(status, "insert unsuccessful")



if __name__=='__main__':
    unittest.main()
