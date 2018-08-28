#encoding=utf-8
import numpy as np

def main():
    #line
    import matplotlib.pyplot as plt
    x = np.linespace(-np.pi, np.pi, 256, endpoint = True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c)
    plt.plot(x, s)
    plt.show()
if __name__ == '__main__':
    main()