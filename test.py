import unittest
import login


class Test_loginCredential(unittest.TestCase):
    def test_set1(self):
        status = login.show_found_status("slaxmi", "sita1")
        self.assertEqual(status, "account found")
    def test_set2(self):
        status = login.show_found_status("bb", "nn")
        self.assertEqual(status, "account not found")


if __name__=='__main__':
    unittest.main()
