def __derivative_p(y: float, yd: float, w1: float, w2: float, x: float) -> float:
    return (y - yd) * (w1 / w1 + w2) * x


def __derivative_q(y: float, yd: float, w1: float, w2: float) -> float:
    return (y - yd) * (w1 / w1 + w2)


def __derivative_x(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                   sig_: float) -> float:
    return (y - yd) * w2 * (y1 - y2) / (w1 + w2) ** 2 * w1 * ((x - x_) / sig_ ** 2)


def __derivative_sigmoide(y: float, yd: float, y1: float, y2: float, w1: float, w2: float, x: float, x_: float,
                       sig_: float) -> float:
    return (y - yd) * w2 * ((y1 - y2) / (w1 + w2) ** 2 )* w1 * ((x - x_)**2 / sig_ ** 3)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
