from logging import getLogger

import pytest
from main import Circle

logger = getLogger()


@pytest.fixture
def good_radius():
    return [1, 10, 100]


@pytest.fixture
def bad_radius():
    return [-1, 0, None, '', '-1', '0', '10']


def test_good_radius(good_radius):
    for radius in good_radius:
        logger.info(f'Testing with {type(radius)} {radius}')
        c = Circle(radius)
        area = c.area()
        assert(area > 0)


def test_bad_radius(bad_radius):
    for radius in bad_radius:
        logger.info(f'Testing with {type(radius)} {radius}')
        with pytest.raises(ValueError):
            c = Circle(radius)
