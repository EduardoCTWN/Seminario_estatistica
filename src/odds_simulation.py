import pandas as pd
import formulas_estatistica as fe

def calculo_odds_total_goals(timeA, timeB, over_under):
    df = pd.read_csv(r'C:\COMP_UEL\Estatistica\dataset\2024_goal_stats.csv')

    tabela_time_A = df[df['Time'] == timeA].iloc[0]
    tabela_time_B = df[df['Time'] == timeB].iloc[0]

    gols_esperados_A = (tabela_time_A['Média Gols Feitos'] + tabela_time_B['Média Gols Sofridos']) / 2
    gols_esperados_B = (tabela_time_B['Média Gols Feitos'] + tabela_time_A['Média Gols Sofridos']) / 2

    max_gols = 6  # até 6 gols para simplificação
    prob_total_gols = {}

    for gols_A in range(max_gols + 1):
        for gols_B in range(max_gols + 1):

            total = gols_A + gols_B
            prob = fe.poisson_form(gols_A, gols_esperados_A) * fe.poisson_form(gols_B, gols_esperados_B)
            prob_total_gols[total] = prob_total_gols.get(total, 0) + prob

    range_over_under = int(over_under + 0.5)

    prob_under = sum(prob_total_gols[g] for g in range(0, range_over_under)) 
    prob_over = 1 - prob_under

    odds_under = fe.odds(prob_under)
    odds_over = fe.odds(prob_over)



    print(f"Probabilidade Under 2.5: {prob_under:.2%}")
    print(f"Probabilidade Over 2.5: {prob_over:.2%}")

    print(f"Odds Under {over_under}: {round(odds_under, 2)}")
    print(f"Odds Over {over_under}: {round(odds_over, 2)}")



calculo_odds_total_goals('Flamengo', 'Palmeiras', 1.5)