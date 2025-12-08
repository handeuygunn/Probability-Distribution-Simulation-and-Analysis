# Probability-Distribution-Simulation-and-Analysis

This project demonstrates how to generate random samples from **Poisson**, **Exponential**, and **Normal** probability distributions using Python and NumPy, analyze their statistical properties, and compare **theoretical** and **empirical** results.  
Additionally, histogram visualizations are produced to observe the shape and behavior of these distributions.

The experiment helps illustrate the **Law of Large Numbers**, which states that sample statistics (mean and variance) converge to theoretical values as the number of samples increases.

---

## 📌 Project Structure and Purpose

The program:

- Generates **10,000 samples** from each of the three distributions.
- Computes **theoretical mean and variance** using distribution formulas.
- Computes **empirical mean and variance** from the generated data.
- Visualizes results using **histograms**.
- Uses a fixed **random seed** to ensure reproducibility.

This setup allows a direct comparison between theory and simulation.

---

## 📘 Probability Distributions Overview

Before analyzing the code, it's important to understand the three probability distributions used.

---

## 1️⃣ Poisson Distribution

Poisson distribution models the **number of events** occurring within a fixed time interval or spatial region. It is widely used in fields such as queueing theory, telecommunications, and biology.

- **Parameter:** λ (lambda), average event rate  
- **Data type:** Integer count (0, 1, 2, …)

### **Theoretical Properties**
- **Mean:** \( E[X] = \lambda \)
- **Variance:** \( Var(X) = \lambda \)

This means Poisson distribution always has **equal mean and variance** — a key property.

### 📌 Code Implementation

```python
def generate_poisson(lmbda, size=10000):
    return np.random.poisson(lmbda, size)
```
The theoretical values for the Poisson distribution are computed as:

```python
def poisson_theoretical(lmbda):
    return lmbda, lmbda
```

In this project, the Poisson distribution is used to generate 10,000 event counts with λ = 5.  
Because Poisson has equal mean and variance, the empirical values should closely match 5 — and the results confirm this.

---

## 2️⃣ Exponential Distribution

The Exponential distribution models the **waiting time between events** in a Poisson process. It always produces positive continuous values and has a characteristic right-skewed shape.

- **Parameter:** λ (lambda), the event rate  
- **NumPy scale parameter:** `scale = 1 / λ`

### **Theoretical Properties**
- **Mean:** \( \frac{1}{\lambda} \)  
- **Variance:** \( \frac{1}{\lambda^2} \)

### 📌 Code Implementation

```python
def generate_exponential(lmbda, size=10000):
    return np.random.exponential(1/lmbda, size)
```

Theoretical mean and variance are calculated as:

```python
def exponential_theoretical(lmbda):
    mean = 1 / lmbda
    var = 1 / (lmbda ** 2)
    return mean, var
```

This ensures the generated exponential data matches the correct mathematical formulation.

---

## 3️⃣ Normal Distribution

The Normal (Gaussian) distribution is symmetric and bell-shaped. It models natural continuous variables such as height, standardized test scores, and measurement noise.

- **Parameters:**  
  - μ (mean)  
  - σ (standard deviation)

### **Theoretical Properties**
- **Mean:** \( \mu \)  
- **Variance:** \( \sigma^2 \)

### 📌 Code Implementation

```python
def generate_normal(mu, sigma, size=10000):
    return np.random.normal(mu, sigma, size)
```

Theoretical values:

```python
def normal_theoretical(mu, sigma):
    return mu, sigma**2
```

With a sample size of 10,000, the empirical distribution closely resembles the true Gaussian curve.

---

## 📊 Computing Empirical Statistics

To compare theoretical expectations with simulated data, the program computes mean and variance from the generated samples:

```python
def empirical_stats(data):
    return np.mean(data), np.var(data)
```

These empirical results help evaluate how accurately the simulation reflects the original distribution.

---

## 📈 Histogram Visualization

To visualize distribution behavior, histograms are generated:

```python
def plot_hist(data, title):
    plt.hist(data, bins=50, density=True, alpha=0.7)
    plt.title(title)
    plt.show()
```

Histograms reveal:

- **Poisson:** discrete and slightly right-skewed  
- **Exponential:** highly right-skewed  
- **Normal:** symmetric and smooth  

---

## 🧪 Running the Full Experiment

The main section of the script ties everything together:

```python
if __name__ == "__main__":
```

Inside, the program:

- Generates Poisson, Exponential, and Normal datasets  
- Computes theoretical and empirical statistics  
- Prints comparisons  
- Displays histograms  

An example from the Poisson experiment:

```python
X = generate_poisson(5)
theo_mean, theo_var = poisson_theoretical(5)
emp_mean, emp_var = empirical_stats(X)
```

This structure keeps the logic clean and easy to maintain.

---

## 📐 Results: Theoretical vs Empirical Comparison

### **Poisson Distribution (λ = 5)**

| Metric     | Theoretical | Empirical     |
|------------|-------------|----------------|
| Mean       | 5           | 5.0005        |
| Variance   | 5           | 5.00329975    |

---

### **Exponential Distribution (λ = 10)**

| Metric     | Theoretical | Empirical        |
|------------|-------------|------------------|
| Mean       | 0.1         | 0.09964155       |
| Variance   | 0.01        | 0.00957246       |

---

### **Normal Distribution (μ = 0, σ = 1)**

| Metric     | Theoretical | Empirical        |
|------------|-------------|------------------|
| Mean       | 0           | -0.0011172       |
| Variance   | 1           | 1.00797          |

---

## 🧾 Interpretation of Results

- All empirical results closely match their theoretical expectations.  
- Small deviations are normal due to sampling randomness.  
- With 10,000 samples, the **Law of Large Numbers** ensures convergence.  
- Histograms visually confirm correct distribution behavior.  
- The exponential distribution required careful handling of NumPy’s `scale` parameter (`1/λ`).  

---

## 🚀 Conclusion

This project successfully demonstrates:

- How probability distributions behave in practice  
- How to generate samples using NumPy  
- How theoretical and empirical statistics compare  
- How distribution shapes appear visually  
- How sampling size affects accuracy  

The results validate both the mathematical properties of Poisson, Exponential, and Normal distributions, and the correctness of the Python implementation.

---

### ✨ Acknowledgment

This document was partially assisted by ChatGPT-5 for text generation and grammar refinement.

