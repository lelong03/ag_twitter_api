import tweepy
import json, time

# Twitter APIs Configs
CONSUMER_KEY = 'd7gdxpbOIpimj20mIWLQYUhnS'
CONSUMER_KEY_SECRET = 'WUyiK12UOLUVGn9jv3ODXFssrdpKLv3vYi42IeoA3F399gKtIF'
ACCESS_TOKEN = '570534552-dT1cV6AGW5B4p8XNhEJm62wbnuygnStQ6Rf9oo5V'
ACCESS_TOKEN_SECRET = 'ojIu80CK9nCPFa6YePPxJVLs1DLS0gF8fj6050zsJbAo6'


class TwitterConnector(object):
    auth, api = None, None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def get_tweet_by_hash_tag(self, tag_str, item_count):
        params = {
            'q': tag_str,
            'lang': "en",
            'count': 100, #this is the maximum value for searching tweet
        }
        response = []
        parser = TweetParser()
        for tweet in tweepy.Cursor(self.api.search, **params).items(item_count):
            response.append(parser.parse(tweet._json))
        return response

    def get_tweet_by_user(self, screen_name, item_count):
        params = {
            'screen_name': screen_name,
            'count': 200, #this is the maximum value for getting user tweets
        }
        response = []
        parser = TweetParser()
        for tweet in tweepy.Cursor(self.api.user_timeline, **params).items(item_count):
            response.append(parser.parse(tweet._json))
        return response


class TweetParser(object):
    def parse_account(self, tweet):
        if ('user' not in tweet) or (tweet.get('user', None) is None):
            return {}
        user = tweet.get('user', None)
        return {
                'full_name': user.get('name', ''),
                'href': user.get('url', ''),
                'id': user.get('id', ''),
        }

    def parse_hashtags(self, tweet):
        entities = tweet.get('entities', {})
        hashtags = entities.get('hashtags', [])
        if len(hashtags) == 0:
            return []
        return ["#%s" % tag.get('text') for tag in hashtags]


    def get_reply_count(self, tweet):
        # with premium subscription, we can get reply_count
        if 'reply_count' in tweet:
            return tweet.get('reply_count')
        return None


    def parse(self, tweet):
        account = self.parse_account(tweet)
        hashtags = self.parse_hashtags(tweet)
        created_at = tweet.get('created_at', '')
        if created_at:
            created_at = time.strftime('%H:%M %p - %d %b %Y', time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y'))
        result = {
            'account': account,
            'date': created_at,
            'hashtags': hashtags,
            'likes': tweet.get('favorite_count', 0),
            "replies": self.get_reply_count(tweet),
            "retweets": tweet.get('retweet_count', 0),
            'text': tweet.get('text', ''),
        }
        return result
