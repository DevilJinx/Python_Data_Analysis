#encoding=utf-8
import numpy as np

def main():
    #line
    import matplotlib.pyplot as plt
    '''x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color = "blue", linewidth = 1.0, linestyle = "-", label = "COS", alpha = 0.5)
    plt.plot(x, s, "r*", label = "SIN")
    plt.title("COS & SIN")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$2$', r'$+\pi/2$', r'$+\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint = True))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor = "white", edgecolor = "none", alpha = 0.2))
    plt.legend("loc = upper left")
    plt.grid()
    # plt.axis([-1, 1, -0.5, 1])
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color = "green", alpha = 0.25)
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linewidth = 3, linestyle = "--")
    plt.annotate("cos(1)", xy = (t, np.cos(1)), xycoords = "data", xytext = (+10, +30), textcoords = "offset points",
                 arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3, rad = .2"))
    plt.show()
    '''
    #scatter
    fig = plt.figure()
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    ax.scatter(X, Y, s = 75, c = T, alpha = .5)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")

    #bar
    fig.add_subplot(332)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.bar(X, +Y1, facecolor = "#9999ff", edgecolor = "white")
    plt.bar(X, -Y2, facecolor = "#ff9999", edgecolor = "white")
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, "%.2f" % y, ha = "center", va = "bottom")
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, "%.2f" % y, ha = "center", va = "top")

    #pie
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    plt.pie(Z, explode = Z * .05, colors = ['%f' % (i / float(n)) for i in range(n)],
            labels = ["%.2f" % (i / float(n)) for i in range(n)])
    plt.gca().set_aspect("equal")
    plt.xticks([]), plt.yticks([])
    plt.show()
if __name__ == '__main__':
    main()