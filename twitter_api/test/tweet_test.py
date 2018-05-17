from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetTweetTests(APITestCase):
    def test_get_tweet_by_hash_tags(self):
        """
        Ensure we can get tweet by hash tags.
        """
        url = reverse('hash_tags_tweet-list', kwargs={'tag': 'googleio2018'}),
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)

    def test_get_tweet_by_screen_name(self):
        """
        Ensure we can get tweet by user screen_name.
        """
        url = reverse('user_tweet-list', kwargs={'screen_name': 'BaoLong_LeLong'}),
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data) > 0, True)

