from scipy.stats import poisson

# Etapa 1: médias de gols esperados
gols_esperados_A = (time_A['gols_marcados'] + time_B['gols_sofridos']) / 2  # ex: 1.6
gols_esperados_B = (time_B['gols_marcados'] + time_A['gols_sofridos']) / 2  # ex: 1.2

# Etapa 2: Probabilidades conjuntas de total de gols
max_gols = 6  # até 6 gols para simplificação
prob_total_gols = {}

for gols_A in range(max_gols + 1):
    for gols_B in range(max_gols + 1):
        total = gols_A + gols_B
        prob = poisson.pmf(gols_A, gols_esperados_A) * poisson.pmf(gols_B, gols_esperados_B)
        prob_total_gols[total] = prob_total_gols.get(total, 0) + prob

# Etapa 3: Soma das probabilidades
prob_under_2_5 = sum(prob_total_gols[g] for g in range(0, 3))  # 0,1,2 gols
prob_over_2_5 = 1 - prob_under_2_5

print(f"Probabilidade Under 2.5: {prob_under_2_5:.2%}")
print(f"Probabilidade Over 2.5: {prob_over_2_5:.2%}")
