import numpy as np
from scipy.optimize import minimize

mu = np.array([1.0, 1.0, 3.0])

sigma1 = 2 * np.sqrt(2)
sigma3 = 4.0
rho13 = 0.75
cov13 = rho13 * sigma1 * sigma3

Sigma = np.array([
    [sigma1**2,          0,          cov13],
    [0,          sigma1**2,          cov13],
    [cov13,              cov13,   sigma3**2]
])

def objective(w):
    return -np.dot(mu, w)

def portfolio_std(w):
    return np.sqrt(w @ Sigma @ w)

# Ограничения
constraints = [
    {'type': 'eq',   'fun': lambda w: np.sum(w) - 1},                    # w1 + w2 + w3 = 1
    {'type': 'ineq', 'fun': lambda w: 2.5 - portfolio_std(w)}            # sigma(r) <= 2.5
]

bounds = [(0, None), (0, None), (0, None)]

w0 = np.array([0.333, 0.333, 0.333])

result = minimize(
    fun=objective,
    x0=w0,
    method='SLSQP',
    bounds=bounds,
    constraints=constraints,
    tol=1e-12
)

print(f"Оптимальные веса:")
print(f"  w1 (актив 1) = {result.x[0]:.8f}")
print(f"  w2 (актив 2) = {result.x[1]:.8f}")
print(f"  w3 (актив 3) = {result.x[2]:.8f}")
print(f"Максимальная средняя прибыль E[r_p] = {-result.fun:.6f}")
print(f"Риск портфеля σ(r_p)                = {portfolio_std(result.x):.6f}")
print(f"Сумма весов                         = {np.sum(result.x):.10f}")


"""
Оптимальные веса:
  w1 (актив 1) = 0.38372186
  w2 (актив 2) = 0.38372186
  w3 (актив 3) = 0.23255628
Максимальная средняя прибыль E[r_p] = 1.465113
Риск портфеля σ(r_p)                = 2.500000
Сумма весов                         = 1.0000000000
"""