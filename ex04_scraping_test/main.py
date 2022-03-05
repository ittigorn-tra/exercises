from requests.exceptions import HTTPError
from repositories.twitter_repository import TwitterRepository
from settings import logger


def get_user_follower_count(url: str):
    repo = TwitterRepository()

    screen_name = repo.parse_screen_name_from_url(url)
    if not screen_name:
        logger.error(f'Failed to get screen_name from url "{url}"')
        return None

    user = None
    try:
        user = repo.user_show(screen_name=screen_name)
    except HTTPError as e:
        logger.error(f'Failed to get user with screen_name "{screen_name}" : {str(e)}')
    return user.followers_count if user else None


if __name__ == '__main__':
    url = 'https://twitter.com/KMbappe'

    follower_count = get_user_follower_count(url)
    print('follower_count :', follower_count)
