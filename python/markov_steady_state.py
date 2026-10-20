"""Markov market-share analysis for MzansiFit Uniforms & Services and two competitors.

Reproduces the steady state from the CMPG322 workbook and shows how many periods the
market takes to stabilise from the Monte Carlo starting vector.
"""
import numpy as np

# Transition matrix: rows = this period's supplier, columns = next period's supplier
# (MzansiFit, Competitor 1, Competitor 2)
P = np.array([
    [0.7, 0.1, 0.2],
    [0.3, 0.7, 0.0],
    [0.4, 0.2, 0.4],
])

# Steady state solves pi = pi P with the shares summing to 1
A = np.vstack([P.T - np.eye(3), np.ones(3)])
b = np.array([0, 0, 0, 1])
steady, *_ = np.linalg.lstsq(A, b, rcond=None)
print("Steady-state shares:", {n: round(float(v), 3) for n, v in zip(["MzansiFit", "Competitor 1", "Competitor 2"], steady)})

# Start from the simulated share pi1 = 0.745, split the remainder evenly
pi = np.array([0.745, 0.1275, 0.1275])
for period in range(1, 51):
    pi = pi @ P
    if np.allclose(pi, steady, atol=5e-4):
        print(f"Shares within 0.0005 of steady state after {period} periods:", pi.round(3))
        break
