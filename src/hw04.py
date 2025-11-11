import numpy as np
import matplotlib.pyplot as plt

# the answer to the ultimate question of life, the universe, and everything
rng = np.random.default_rng(42)

# analytic values for Uniform[-1, 1]
analytic_mean = 0.0
analytic_var = (2.0**2) / 12.0  # (b - a)^2 / 12 = 1/3

# Problem 5a: REQUIRED
def plot_sample():
    x1 = rng.uniform(-1, 1, size=10)

    fig = plt.figure()
    plt.hist(x1, bins=10, range=(-1, 1), density=False)
    plt.title("Histogram of N=10 samples of Uniform[-1, 1]")
    plt.xlabel("x1")
    plt.ylabel("Count")

    return fig


# Problem 5b: REQUIRED
def compute_sample_stats():
    sample_N = []
    sample_mean = []
    sample_mean_err = []
    sample_variance = []
    sample_variance_err = []

    for i in range(1, 7):
        N = 10**i
        samples = rng.uniform(-1, 1, size=N)
        mean = float(np.mean(samples))
        variance = float(np.var(samples))

        sample_N.append(N)
        sample_mean.append(mean)
        sample_mean_err.append(abs(mean - analytic_mean))
        sample_variance.append(variance)
        sample_variance_err.append(abs(variance - analytic_var))


    return f"""
    N: {sample_N}
    Sample Mean: {sample_mean}
    Sample Variance: {sample_variance}
    Sample Mean Error: {sample_mean_err}
    Sample Variance Error: {sample_variance_err}
    The sample mean and variance converge toward 0 and 1/3 as N grows.
    The errors shrink similar to O(1/sqrt(N)).
    """


# Problem 5c: REQUIRED
def plot_new_variables():
    figs = []

    N = 100_000
    x1 = rng.uniform(-1, 1, size=N)
    x2 = rng.uniform(-1, 1, size=N)
    x3 = rng.uniform(-1, 1, size=N)
    x4 = rng.uniform(-1, 1, size=N)

    y1 = (x1 + x2) / 2.0
    y2 = (x1 + x2 + x3) / 3.0
    y3 = (x1 + x2 + x3 + x4) / 4.0

    globals().update(dict(x1=x1, x2=x2, x3=x3, x4=x4, y1=y1, y2=y2, y3=y3))

    for data, title in [
        (x1, "p(x1) ~ Uniform[-1,1]"),
        (y1, "p(y1) where y1=(x1+x2)/2"),
        (y2, "p(y2) where y2=(x1+x2+x3)/3"),
        (y3, "p(y3) where y3=(x1+x2+x3+x4)/4"),
    ]:
        fig = plt.figure()
        plt.hist(data, bins=50, range=(-1, 1), density=True)
        plt.title(title)
        plt.xlabel("value")
        plt.ylabel("Density")
        figs.append(fig)

    return figs


# Problem 5d: REQUIRED
def describe_new_variables():
    return """
    Averages of i.i.d. variables trend toward a normal distribution.
    As you average more uniform distributions, the histogram looks more Gaussian and its spread decreases similar to 1/sqrt(N).
    """


# Problem 5e: REQUIRED
def plot_transformations():
    figs = []

    y3 = globals()["y3"]
    z = 2.0 * y3 + 3.0
    q = np.exp(y3)

    globals().update(dict(z=z, q=q))

    fig = plt.figure()
    plt.hist(y3, bins=60, range=(-1, 1), density=True)
    plt.title("p(y3) (re-plotted for comparison)")
    plt.xlabel("y3")
    plt.ylabel("Density")
    figs.append(fig)

    # p(z)
    fig = plt.figure()
    plt.hist(z, bins=60, density=True)
    plt.title("p(z) where z = 2*y3 + 3")
    plt.xlabel("z")
    plt.ylabel("Density")
    figs.append(fig)

    # p(q)
    fig = plt.figure()
    plt.hist(q, bins=60, density=True)
    plt.title("p(q) where q = exp(y3)")
    plt.xlabel("q")
    plt.ylabel("Density")
    figs.append(fig)

    return figs


# Problem 5f: REQUIRED
def describe_transformations():
    return """
    Linear Transform (z):
        Same shape, shifted right by 3, stretched by factor of 2. Density scales by 1/|2|, so the peak is lower but the curve is simply shifted and stretched.
    Non-linear Transform (q):
        Monotone but not shape-preserving. Values within [-1, 1] map to [exp(-1), exp(1)]. The distribution becomes positively skewed, compressing on the left (near 1/e) and stretching on the right (towards e).
    """


if __name__ == "__main__":
    # 5a
    plot_sample().savefig("./outputs/figures/s05a.png", dpi=300)
    # 5b
    with open("./outputs/text/s05b.txt", "w", encoding="utf-8") as f:
        f.write(compute_sample_stats())
    # 5c
    figs5c = plot_new_variables()
    for i in range(0, len(figs5c)):
        figs5c[i].savefig(("./outputs/figures/s05c" + str(i + 1) + ".png"), dpi=300)
    # 5d
    with open("./outputs/text/s05d.txt", "w", encoding="utf-8") as f:
        f.write(describe_new_variables())
    # 5e
    figs5e = plot_transformations()
    for i in range(0, len(figs5e)):
        figs5c[i].savefig(("./outputs/figures/s05e" + str(i + 1) + ".png"), dpi=300)
    # 5f
    with open("./outputs/text/s05f.txt", "w", encoding="utf-8") as f:
        f.write(describe_transformations())

    # plt.show()
