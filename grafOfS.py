import matplotlib.pyplot as plt
import numpy as np

def grafOfMove(v0, a, t):
    """
        функция выводит график перемещения
        v0 - начальная скорость;
        a - ускорение;
        t - время;
    """

    maxSeconds = 60 # установить предел для секунд
    seconds = np.linspace(0, t, maxSeconds)
    s = [(v0 * t + (a * (sec**2)) / 2) for sec in seconds]
    plt.plot(seconds, s)

    ax = plt.gca()
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

grafOfMove(24, 1, 12) # указать в порядке : v0, a, t
