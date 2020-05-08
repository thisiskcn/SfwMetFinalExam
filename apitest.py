"""python script to test api"""
import unittest
import requests


class ApiTest(unittest.TestCase):
    """Class to test API"""
    def test_api(self):
        """Testing for the API"""
        url = "https://corona-virus-stats.herokuapp.com/api/v1/cases" \
              "/countries-search?search=Ukraine"
        testing_api = requests.get(url)
        status_code = testing_api.status_code
        expected_result = 200
        data = testing_api.json()

        status = data["status"]
        status_message = "success"

        self.assertEqual(status_code, expected_result)
        self.assertEqual(status, status_message)


if __name__ == '__main__':
    unittest.main()
