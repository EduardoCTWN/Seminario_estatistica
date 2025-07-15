import pandas as pd
import formulas_estatistica as fe

def calculo_odds_total_goals(timeA, timeB, over_under):
    df = pd.read_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\2024_goal_stats.csv')

    tabela_time_A = df[df['Time'] == timeA].iloc[0]
    tabela_time_B = df[df['Time'] == timeB].iloc[0]

    gols_esperados_A = (tabela_time_A['Média Gols Feitos'] + tabela_time_B['Média Gols Sofridos']) / 2
    gols_esperados_B = (tabela_time_B['Média Gols Feitos'] + tabela_time_A['Média Gols Sofridos']) / 2

    max_gols = 7  # até 6 gols para simplificação
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



    print(f"Probabilidade Under {over_under}: {prob_under:.2%}")
    print(f"Probabilidade Over {over_under}: {prob_over:.2%}")

    print(f"Odds Under {over_under}: {round(odds_under, 2)}")
    print(f"Odds Over {over_under}: {round(odds_over, 2)}\n")




def calcular_probabilidades_poisson(media_gols_A, media_gols_B):
    """
    Calcula as probabilidades de vitória, empate e derrota para o time A
    usando o modelo de Poisson bivariado.
    
    Parâmetros:
    - media_gols_A: gols esperados do time A
    - media_gols_B: gols esperados do time B
    - max_gols: número máximo de gols considerados por time
    
    Retorna:
    - dicionário com probabilidades de vitória A, empate, vitória B
    """

    max_gols = 7
    prob_vitoria_A = 0
    prob_empate = 0
    prob_vitoria_B = 0

    for gols_A in range(max_gols + 1):
        for gols_B in range(max_gols + 1):
            prob = fe.poisson_form(gols_A, media_gols_A) * fe.poisson_form(gols_B, media_gols_B)
            if gols_A > gols_B:
                prob_vitoria_A += prob
            elif gols_A == gols_B:
                prob_empate += prob
            else:
                prob_vitoria_B += prob

    return {
        "vitoria_A": prob_vitoria_A,
        "empate": prob_empate,
        "vitoria_B": prob_vitoria_B
    }


def calculo_odds_resultado(timeA, timeB):
    df = pd.read_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\2024_goal_stats.csv')

    tabela_time_A = df[df['Time'] == timeA].iloc[0]
    tabela_time_B = df[df['Time'] == timeB].iloc[0]

    gols_esperados_A = (tabela_time_A['Média Gols Feitos'] + tabela_time_B['Média Gols Sofridos']) / 2
    gols_esperados_B = (tabela_time_B['Média Gols Feitos'] + tabela_time_A['Média Gols Sofridos']) / 2

    probabilidades = calcular_probabilidades_poisson(gols_esperados_A, gols_esperados_B)

    prob_vitoria_A = probabilidades.get("vitoria_A")
    prob_empate = probabilidades.get("empate")
    prob_vitoria_B = probabilidades.get("vitoria_B")

    print(f"Probabilidade Vitoria {timeA}: {prob_vitoria_A:.2%}")
    print(f"Probabilidade Empate: {prob_empate:.2%}")
    print(f"Probabilidade Vitoria {timeB}: {prob_vitoria_B:.2%}")

    odds_A = fe.odds(prob_vitoria_A) * 0.95
    odds_empate = fe.odds(prob_empate) * 0.95
    odds_B = fe.odds(prob_vitoria_B)* 0.95

    print(f"Odds Vitoria {timeA}: {round(odds_A, 2)}")
    print(f"Odds Empate: {round(odds_empate, 2)}")
    print(f"Odds Vitoria {timeB}: {round(odds_B, 2)}\n")






