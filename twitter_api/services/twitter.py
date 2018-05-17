from connector.twitter import TwitterConnector

class TwitterTweetService(object):
    def get_tweet_by_hash_tag(self, tag_str, item_count):
        tag_str = "#%s" % tag_str
        reply = TwitterConnector().get_tweet_by_hash_tag(tag_str, item_count)
        return reply

    def get_tweet_by_user(self, screen_name, item_count):
        reply = TwitterConnector().get_tweet_by_user(screen_name, item_count)
        return reply
