from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.exceptions import APIException
from services.twitter import TwitterTweetService


class TweetSerializer(serializers.Serializer):
    pages_limit = serializers.IntegerField(required=False)

DEFAULT_PAGES_LIMIT = 20


@api_view(['GET'])
def api_root(request, format=None):
    default_hash_tags_kw = {'tag': 'googleio2018'}
    default_user_kw = {'screen_name': 'BaoLong_LeLong'}
    return Response({
        'hash_tags_tweet': reverse('hash_tags_tweet-list', request=request, format=format, kwargs=default_hash_tags_kw),
        'user_tweet': reverse('user_tweet-list', request=request, format=format, kwargs=default_user_kw),
    })


@api_view(['GET'])
def hashtags_tweet(request, tag, format=None):
    """
    Get the list of tweets with the given hashtag.

    **pages_limit**: specifies the number of pages to retrieve
    """
    serializer = TweetSerializer(data=request.query_params)
    if not serializer.is_valid():
        raise APIException(serializer.errors)
    pages_limit = serializer.validated_data.get('pages_limit', None)
    if not pages_limit:
        pages_limit = DEFAULT_PAGES_LIMIT
    response_data = TwitterTweetService().get_tweet_by_hash_tag(tag_str=tag, item_count=pages_limit)
    return Response(response_data)


@api_view(['GET'])
def user_tweet(request, screen_name, format=None):
    """
    Get the list of tweets that user has on his feed by user **screen name**

    **pages_limit**: specifies the number of pages to retrieve
    """
    serializer = TweetSerializer(data=request.query_params)
    if not serializer.is_valid():
        raise APIException(serializer.errors)
    pages_limit = serializer.validated_data.get('pages_limit', None)
    if not pages_limit:
        pages_limit = DEFAULT_PAGES_LIMIT
    response_data = TwitterTweetService().get_tweet_by_user(screen_name=screen_name, item_count=pages_limit)
    return Response(response_data)

