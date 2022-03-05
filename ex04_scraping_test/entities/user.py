import inspect
from dataclasses import dataclass, asdict


@dataclass
class User:
    '''
    Twitter user object
    '''
    id: int
    id_str: str
    name: str
    screen_name: str
    protected: bool
    verified: bool
    followers_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: int
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool
    withheld_in_countries: list
    profile_banner_url: str = None
    location: str = None
    derived: dict = None
    url: str = None
    description: str = None
    withheld_scope: str = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: v for k, v in data.items() if k in inspect.signature(cls).parameters})

    def dict(self):
        return asdict(self)