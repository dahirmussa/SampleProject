import unittest

import urllib.request


class BasicTests(unittest.TestCase):



    def test_main_page(self):
        
        status_code = urllib.request.urlopen("http://localhost:5000").getcode()

   
        self.assertEqual(status_code, 200)
   

    def test_page2(self):
        
        status_code = urllib.request.urlopen("http://localhost:5000/page2").getcode()

   
        self.assertEqual(status_code, 200)
   

if __name__ == "__main__":
    unittest.main()