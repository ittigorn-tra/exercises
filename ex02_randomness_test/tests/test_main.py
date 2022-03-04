from logging import getLogger

from lottery_config import LotteryConfig
from main import draw_lottery

logger = getLogger()


def test_draw_lottery():
    for test_count in range(10000):
        draw_results = draw_lottery()
        logger.info(f'Test #{str(test_count).ljust(4)} Draw Results : {draw_results}')

        # check if return type is as in the requirement
        assert isinstance(draw_results, list)

        # check if properties is as in config
        assert len(draw_results) == LotteryConfig.DRAW_SIZE.value
        assert min(draw_results) >= LotteryConfig.BALL_MIN_NO.value
        assert max(draw_results) <= LotteryConfig.BALL_MAX_NO.value

        # check that the previous ball is always less than current ball
        previous_ball = LotteryConfig.BALL_MIN_NO.value - 1
        for ball in draw_results:
            assert ball > previous_ball
            previous_ball = ball
