import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # For reproducibility

def generate_poisson(lmbda, size=10000):
    """Generate Poisson-distributed random variables."""
    return np.random.poisson(lmbda, size)

def generate_exponential(lmbda, size=10000): 
    """Generate Exponentially-distributed random variables."""
    return np.random.exponential(1/lmbda, size)

def generate_normal(mu, sigma, size=10000):
    """Generate Normally-distributed random variables."""
    return np.random.normal(mu, sigma, size)

def poisson_theoretical(lmbda):
    return lmbda, lmbda

def exponential_theoretical(lmbda):
    mean = 1 / lmbda
    var = 1 / (lmbda ** 2)
    return mean, var

def normal_theoretical(mu, sigma):
    return mu, sigma**2

def empirical_stats(data):
    return np.mean(data), np.var(data)

def plot_hist(data, title):
    plt.hist(data, bins=50, density=True, alpha=0.7)
    plt.title(title)
    plt.show()


if __name__ == "__main__":

    # POISSON
    X = generate_poisson(5)
    theo_mean, theo_var = poisson_theoretical(5)
    emp_mean, emp_var = empirical_stats(X)
    print("Poisson - Teorik:", theo_mean, theo_var)
    print("Poisson - Hesaplanan:", emp_mean, emp_var)
    plot_hist(X, "Poisson Histogram")

    # EXPONENTIAL
    Y = generate_exponential(10)
    theo_mean, theo_var = exponential_theoretical(10)
    emp_mean, emp_var = empirical_stats(Y)
    print("Exponential - Teorik:", theo_mean, theo_var)
    print("Exponential - Hesaplanan:", emp_mean, emp_var)
    plot_hist(Y, "Exponential Histogram")

    # NORMAL
    Z = generate_normal(0, 1)
    theo_mean, theo_var = normal_theoretical(0, 1)
    emp_mean, emp_var = empirical_stats(Z)
    print("Normal - Teorik:", theo_mean, theo_var)
    print("Normal - Hesaplanan:", emp_mean, emp_var)
    plot_hist(Z, "Normal Histogram")
