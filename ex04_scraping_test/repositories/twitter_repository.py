import requests
from entities.user import User
from settings import TWITTER_BEARER_TOKEN, TWITTER_USER_SHOW_ENDPOINT

from repositories.twitter_repository_abc import TwitterRepositoryABC as BaseClass


class TwitterRepository(BaseClass):
    def __init__(self) -> None:
        self.bearer_token = TWITTER_BEARER_TOKEN
        self.user_show_endpoint = TWITTER_USER_SHOW_ENDPOINT

    def __include_bearer_token(self, req):
        req.headers["Authorization"] = f"Bearer {self.bearer_token}"
        return req

    def __make_get_request(self, url: str, query_params: dict = None) -> dict:
        response = requests.get(url, auth=self.__include_bearer_token, params=query_params)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def parse_screen_name_from_url(self, url: str) -> str:
        '''
        Parse screen name from URL path after the twitter domain name
        '''
        if (not url) or (not isinstance(url, str)):
            return None
        splitted = url.strip('/').split('/')
        domain_index = None
        try:
            domain_index = splitted.index('twitter.com')
        except ValueError:
            return None
        return splitted[domain_index + 1] if len(splitted) > domain_index + 1 else None

    def user_show(self, user_id: str = None, screen_name: str = None) -> User:
        '''
        Please provide either "user_id" or "screen_name" for this method
        '''
        if len([value for value in [user_id, screen_name] if value]) != 1:
            raise Exception('Please provide either "user_id" or "screen_name" for this method')

        query_params = {}
        for key, value in zip(['user_id', 'screen_name'], [user_id, screen_name]):
            if value:
                query_params[key] = value

        json_response = self.__make_get_request(url=self.user_show_endpoint, query_params=query_params)
        result = None
        if json_response:
            result = User.from_dict(json_response)

        return result
