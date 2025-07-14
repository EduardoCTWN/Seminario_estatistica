import numpy as np
from scipy.special import factorial


def poisson_form(k, lambda_):
  return (np.power(lambda_, k) * np.exp(-lambda_)) / factorial(k)



def calcular_ev(real_probability, odd, bet_value):
  loosing_probability = 1 - real_probability
  profit_if_win = bet_value * (odd - 1)

  loss_if_loss = bet_value 

  ev = (real_probability * profit_if_win) - (loosing_probability * loss_if_loss)
  return ev



def odds(probability):
  return 1 / probability
