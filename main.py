import math
import random

from matplotlib import pyplot as plt
from typing import List

# CONSTANTS

DIMENSION = 2
COUNT_POINTS = 100
COUNT_EPOCHS = 1000
ADJUSTMENT = 1

# INITIALIZE ARRAYS
y = [0] * COUNT_POINTS
x = [random.uniform(-DIMENSION, DIMENSION) for i in range(COUNT_POINTS)]
x.sort()


def run():
    # TODO: add the plot of original function

    pass


def otimization():
    # ENTRY VALUES
    x1 = 2
    sd1 = 1.7
    x2 = -2
    sd2 = 1.7

    p1 = -1.8
    q1 = 0
    p2 = 1.8
    q2 = 0

    w1, w2 = gaussians_generate(x1, x2, sd1, sd2)
    plot(x, w1, x, w2)


def gradient(x1: float, sig1: float, x2: float, sig2: float, p1: float, p2: float, q1: float, q2: float, y: float,
             yd: float, alfa: float, ):
    pk1 = p1 - alfa * (__derivative_p(y, yd, sig1, sig2, x1))
    pk2 = p2 - alfa * (__derivative_p(y, yd, sig1, sig2, x2))

    qk1 = q1 - alfa * (__derivative_q(y, yd, sig1, sig2))
    qk2 = q2 - alfa * (__derivative_q(y, yd, sig2, sig1))

    y1 = pk1 * x1 + qk1
    y2 = pk2 * x1 + qk2


def gaussians_generate(x1: float, x2: float, sigma1: float, sigma2: float) -> tuple[List: float, List: float]:
    w1 = list()
    w2 = list()
    for i in x:
        w1.append(__gaussian(i, x1, sigma2))
        w2.append(__gaussian(i, x2, sigma2))
    return [w1, w2]


def plot(array_x1: List[float], array_y1: List[float], array_x2: List[float], array_y2: List[float]):
    plt.plot(array_x1, array_y1, 'bs', array_x2, array_y2, 'bs')
    plt.show()


def __derivative_p(y: float, yd: float, w1: float, w2: float, x: float) -> float:
    return (y - yd) * (w1 / w1 + w2) * x


def __derivative_q(y: float, yd: float, w1: float, w2: float) -> float:
    return (y - yd) * (w1 / w1 + w2)


def __derivative_x(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                   sig_: float) -> float:
    return (y - yd) * w2 * (y1 - y2) / (w1 + w2) ** 2 * w1 * ((x - x_) / sig_ ** 2)


def __derivative_sigmoide(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                          sig_: float) -> float:
    return (y - yd) * w2 * ((y1 - y2) / (w1 + w2) ** 2) * w1 * ((x - x_) ** 2 / sig_ ** 3)


def __y(y1: float, y2: float, w1: float, w2: float):
    return (w1 * y1 + w2 * y2) / w1 + w2


def __gaussian(x: float, mu: float, sigma: float) -> float:
    return math.exp(-1 / 2 * ((x - mu) / sigma) ** 2)


if __name__ == '__main__':
    otimization()
