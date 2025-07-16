import numpy as np
from scipy.special import factorial


def poisson_form(k, lambda_):
  return (np.power(lambda_, k) * np.exp(-lambda_)) / factorial(k)

def odds(probability):
  return 1 / probability
