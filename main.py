import math
import random

from matplotlib import pyplot as plt
from typing import List

# CONSTANTS

DIMENSION = 2
COUNT_POINTS = 100
COUNT_EPOCHS = 1000
ADJUSTMENT = 1
ALFA = 0.001

# INITIALIZE ARRAYS
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

    # generate gaussians
    w1, w2 = gaussians_generate(x1, x2, sd1, sd2)
    plot(x, w1, x, w2)

    w1_n = list()
    w2_n = list()

    for i in range(COUNT_POINTS):
        w1_n = w1[i] / w1[i] + w2[i]
        w2_n = w2[i] / w2[i] + w1[i]

    y1 = list()
    y2 = list()

    for x_n in x:
        y1.append(p1 * x_n + q1)
        y2.append(p2 * x_n + q2)

    yd = list()
    for i in range(COUNT_POINTS):
        yd.append(w1_n[i] * y1[i] - w2_n[i] * y2[i])

    y = list()
    for x_n in x:
        y.append(x_n ** 2)

    # calcule of initial error
    error = list()
    for i in range(COUNT_POINTS):
        error.append(((y[i] - yd[i]) ** 2) / 2)

    for i in range(COUNT_EPOCHS):
        for p in range(COUNT_POINTS):
            a = p


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

    return w1, w2


def curve_approximate_generate(w1: List[float], w2: List[float]) -> tuple[List: float, List: float]:


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
