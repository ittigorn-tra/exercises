import numpy as np

from lottery_config import LotteryConfig


def draw_lottery() -> list:
    container = np.arange(LotteryConfig.BALL_MIN_NO.value, LotteryConfig.BALL_MAX_NO.value + 1)
    result = np.random.choice(container, size=LotteryConfig.DRAW_SIZE.value, replace=False)
    result = np.sort(result)
    return result.tolist()


if __name__ == '__main__':
    result = draw_lottery()
    print(result)
