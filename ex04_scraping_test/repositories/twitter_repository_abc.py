from abc import ABC, abstractmethod


class TwitterRepositoryABC(ABC):
    @abstractmethod
    def __include_bearer_token(self, req):
        pass

    @abstractmethod
    def __make_get_request(self, url: str, query_params: dict) -> dict:
        pass

    @abstractmethod
    def parse_screen_name_from_url(url: str) -> str:
        pass

    @abstractmethod
    def user_show(self, user_id: str = None, screen_name: str = None) -> dict:
        pass
