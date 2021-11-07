import math
import random

import numpy
from matplotlib import pyplot as plt
from typing import List, Optional

# CONSTANTS

DIMENSION = 2
COUNT_POINTS = 100
COUNT_EPOCHS = 1000
ADJUSTMENT = 1
ALPHA = 0.01


# GRAPHIC PROPERTIES
class GraphicProperties:
    BLUE_CIRCLE_MARKS = 'bo'
    GREEN_CIRCLE_MARKS = 'go'
    RED_CIRCLE_MARKS = 'ro'

    BLUE_SOLID_LINE = '-b'
    GREEN_SOLID_LINE = '-g'
    RED_SOLID_LINE = '-r'

    BLUE_DASHED_LINE = '--b'
    GREEN_DASHED_LINE = '--g'
    RED_DASHED_LINE = '--r'

    ORIGINAL_FUNCTION = 'FUNÇÃO ORIGINAL - X**2'
    FIRST_GAUSSIAN = "GAUSSIANA 1"
    SECOND_GAUSSIAN = 'GAUSSIANA 2'
    APPROXIMATE_FUNCTION = 'FUNÇÃO APROXIMADA'
    EPOCHS_ERROR = 'ERRO DAS ÉPOCAS - '


# INITIALIZE ARRAYS
x = [i for i in numpy.arange(-2, 2, 4 / COUNT_POINTS)]
x.sort()
y = [i ** 2 for i in x]


def run():
    sugeno()


def sugeno():
    # ENTRY VALUES
    # in
    x1 = 2
    sd1 = 1.7
    x2 = -2
    sd2 = 1.7

    # out
    p1 = -1.8
    q1 = 0.0
    p2 = 1.8
    q2 = 0.0

    initial_function_plot(x1, x2, sd1, sd2)

    epoch_error = list()

    for i in range(COUNT_EPOCHS):
        random.shuffle(x)
        error = 0.0
        for j in range(COUNT_POINTS):
            alpha = 0.01
            yd = x[j] ** 2

            w1, w2 = gauss_m_f(x[j], x1, x2, sd1, sd2)

            y1 = p1 * x[j] + q1
            y2 = p2 * x[j] + q2
            yo = __y(y1, y2, w1, w2)
            p1, p2, q1, q2, x1, x2, sd1, sd2 = gradient(x[j], x1, w1, x2, w2, p1, p2, q1, q2, yo, yd, y1, y2, alpha,
                                                        sd1, sd2)
            error += (yo - yd) ** 2 / 2
        epoch_error.append(error / COUNT_POINTS)
        print(error / COUNT_POINTS)
    error_plot(epoch_error)

    generated_y = list()
    x.sort()
    for i in range(COUNT_POINTS):
        w1, w2 = gauss_m_f(x[i], x1, x2, sd1, sd2)
        y1 = p1 * x[i] + q1
        y2 = p2 * x[i] + q2
        generated_y.append(__y(y1, y2, w1, w2))
    __plot(x, generated_y, x, y, GraphicProperties.RED_DASHED_LINE, GraphicProperties.APPROXIMATE_FUNCTION,
           GraphicProperties.BLUE_SOLID_LINE, GraphicProperties.ORIGINAL_FUNCTION)


def gradient(x: float, x1: float, w1: float, x2: float, w2: float, p1: float, p2: float,
             q1: float, q2: float, y: float, yd: float, y1: float, y2: float, alfa: float,
             sd1: float, sd2: float) -> \
        tuple[float, float, float, float, float, float, float, float]:
    pk1 = p1 - ALPHA * (__derivative_p(y, yd, w1, w2, x))
    pk2 = p2 - ALPHA * (__derivative_p(y, yd, w1, w2, x))

    qk1 = q1 - ALPHA * (__derivative_q(y, yd, w1, w2))
    qk2 = q2 - ALPHA * (__derivative_q(y, yd, w2, w1))

    xk1 = x1 - ALPHA * (__derivative_x(y, yd, y1, y2, w1, w2, x, x1, sd1))
    xk2 = x2 - ALPHA * (__derivative_x(y, yd, y1, y2, w1, w2, x, x2, sd2))

    sdk1 = sd1 - ALPHA * (__derivative_sigma(y, yd, y1, y2, w1, w2, x, x1, sd1))
    sdk2 = sd2 - ALPHA * (__derivative_sigma(y, yd, y1, y2, w1, w2, x, x2, sd2))

    return pk1, pk2, qk1, qk2, xk1, xk2, sdk1, sdk2


def gauss_m_f(x: float, x1: float, x2: float, sigma1: float, sigma2: float) -> tuple[float, float]:
    w1 = __gaussian_membership_function(x, x1, sigma1)
    w2 = __gaussian_membership_function(x, x2, sigma2)
    return w1, w2


def initial_function_plot(x1: float, x2: float, sd1: float, sd2: float):
    points_w1 = list()
    points_w2 = list()
    for i in range(COUNT_POINTS):
        w1, w2 = gauss_m_f(x[i], x1, x2, sd1, sd2)
        points_w1.append(w1)
        points_w2.append(w2)
    x.sort()
    __plot(x, points_w1, x, points_w2, GraphicProperties.GREEN_SOLID_LINE, GraphicProperties.FIRST_GAUSSIAN,
           GraphicProperties.GREEN_SOLID_LINE, GraphicProperties.SECOND_GAUSSIAN)


def original_function_plot():
    __plot(x, y, None, None, GraphicProperties.BLUE_CIRCLE_MARKS, GraphicProperties.ORIGINAL_FUNCTION)


def error_plot(errors: List[float]):
    epochs = [i for i in range(COUNT_EPOCHS)]
    errors.sort()
    errors.reverse()
    __plot(epochs, errors, None, None, GraphicProperties.RED_SOLID_LINE,
           GraphicProperties.EPOCHS_ERROR + str(errors[len(errors) - 1]))


def __plot(array_x1: Optional[List[float]] = None,
           array_y1: Optional[List[float]] = None,
           array_x2: Optional[List[float]] = None,
           array_y2: Optional[List[float]] = None,
           type_line1: Optional[str] = '',
           label_text1: Optional[str] = '',
           type_line2: Optional[str] = '',
           label_text2: Optional[str] = ''
           ):
    if array_x1 and array_x2 and array_y1 and array_y2:
        fig, ax = plt.subplots()
        ax.plot(array_x1, array_y1, type_line1, label=label_text1)
        ax.plot(array_x2, array_y2, type_line2, label=label_text2)
        ax.axis('equal')
        leg = ax.legend()
        plt.show()
        return

    if array_x1 and array_y1:
        fig, ax = plt.subplots()
        ax.plot(array_x1, array_y1, type_line1, label=label_text1)
        ax.axis('equal')
        leg = ax.legend()
        plt.show()
        return


def __derivative_p(y: float, yd: float, w1: float, w2: float, x: float) -> float:
    return (y - yd) * (w1 / w1 + w2) * x


def __derivative_q(y: float, yd: float, w1: float, w2: float) -> float:
    if y and yd and w1 and w2:
        return (y - yd) * (w1 / w1 + w2)
    return 0.0


def __derivative_x(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                   sig_: float) -> float:
    return (y - yd) * w2 * (y1 - y2) / (w1 + w2) ** 2 * w1 * ((x - x_) / sig_ ** 2)


def __derivative_sigma(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                       sig_: float) -> float:
    return (y - yd) * w2 * ((y1 - y2) / (w1 + w2) ** 2) * w1 * ((x - x_) ** 2 / sig_ ** 3)


def __y(y1: float, y2: float, w1: float, w2: float):
    return (w1 * y1 + w2 * y2) / w1 + w2


def __gaussian_membership_function(x: float, mu: float, sigma: float) -> float:
    return math.exp(-1 / 2 * ((x - mu) / sigma) ** 2)


if __name__ == '__main__':
    run()
