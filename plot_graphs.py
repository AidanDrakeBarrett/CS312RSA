import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 2100, 250)
    coefficient = 166231.09 / (2048 ** 3)
    y = coefficient * (x**3)
    data = {
        64:3.98,
        128:25.34,
        256:64.64,
        512:474.19,
        1024:9992.62,
        2048:166231.09
    }

    plt.plot(data.keys(), data.values(), color = 'red', linestyle = '-', marker = 'o', label = "Actual Time")
    plt.plot(x, y, color='black', label="Theoretical Time")
    plt.xlabel('n')
    plt.ylabel("Runtime")
    plt.legend()
    plt.title("Large Prime Generation Runtime")
    plt.savefig("graph1.png")
    plt.clf()

    x = np.linspace(0, 2100, 250)
    coefficient = 198569.38 / (2048 ** 3)
    y = coefficient * (x ** 3)
    data = {
        64: 6.98,
        128: 68.86,
        256: 298.05,
        512: 2085.5,
        1024: 16636.14,
        2048: 198569.38
    }

    plt.plot(data.keys(), data.values(), color='red', linestyle='-', marker='o', label="Actual Time")
    plt.plot(x, y, color='black', label="Theoretical Time")
    plt.xlabel('n')
    plt.ylabel("Runtime")
    plt.legend()
    plt.title("Key Pair Generation Runtime")
    plt.savefig("graph2.png")

if __name__ == '__main__':
    main()