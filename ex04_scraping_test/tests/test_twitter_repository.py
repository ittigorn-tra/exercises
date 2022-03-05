import pytest
from entities.user import User
from repositories.twitter_repository import TwitterRepository
from settings import logger


@pytest.fixture
def repo():
    return TwitterRepository()


@pytest.fixture
def good_urls():
    return [
        ['https://twitter.com/KMbappe', 'KMbappe'],
        ['https://twitter.com/blakeshelton', 'blakeshelton'],
        ['https://twitter.com/ChrisStapleton', 'ChrisStapleton'],
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


@pytest.fixture
def screen_name():
    return 'KMbappe'


def test_good_urls(repo, good_urls):
    for url, expected_result in good_urls:
        logger.info(f'Testing with {type(url)} {url}')
        screen_name = repo.parse_screen_name_from_url(url)
        assert screen_name == expected_result


def test_bad_urls(repo, bad_urls):
    for url in bad_urls:
        logger.info(f'Testing with {type(url)} {url}')
        screen_name = repo.parse_screen_name_from_url(url)
        assert screen_name is None


def test_user_get(repo, screen_name):
    user = repo.user_show(screen_name=screen_name)
    logger.info(user.dict())
    assert isinstance(user, User)
