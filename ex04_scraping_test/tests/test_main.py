import pytest
from settings import logger
from main import get_user_follower_count


@pytest.fixture
def good_urls():
    return [
        'https://twitter.com/blakeshelton',
    ]


@pytest.fixture
def bad_urls():
    return [
        'https://twitter.com/',
        'https://twit.com/blakeshelton',
        '',
        None,
        123,
        14.27,
    ]


def test_good_urls(good_urls):
    for url in good_urls:
        logger.info(f'Testing with {type(url)} {url}')
        follower_count = get_user_follower_count(url)
        logger.info(follower_count)
        assert isinstance(follower_count, int)
        assert follower_count > 0


def test_bad_urls(bad_urls):
    for url in bad_urls:
        logger.info(f'Testing with {type(url)} {url}')
        follower_count = get_user_follower_count(url)
        assert follower_count is None
