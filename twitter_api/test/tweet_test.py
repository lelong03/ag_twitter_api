import unittest
import requests
from rest_framework import status

HOST = "http://127.0.0.1:8000/"

def get_api(url, param=None): return requests.get(HOST + url, param)
def post_api(url, param=None): return requests.post(HOST + url, param)

class HashtagsTweetTest(unittest.TestCase):
    URL_STR = "hashtags/googleio2018"

    def test_connection(self):
        rep = get_api(self.URL_STR)
        self.assertEqual(rep.status_code, status.HTTP_200_OK)

    def test_type(self):
        rep = get_api(self.URL_STR)
        data = rep.json()
        self.assertEqual(type(data), list)

    def test_number_of(self):
        number = 3
        rep = get_api("%s?pages_limit=%s" % (self.URL_STR, number))
        data = rep.json()
        self.assertEqual(len(data), number)


class UserTweetTest(HashtagsTweetTest):
    URL_STR = "user/BaoLong_LeLong"


if __name__ == '__main__':
    unittest.main()
