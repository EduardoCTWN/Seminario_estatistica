import pandas as pd


# Carregamento dados filtrados somente para o campeonato brasileiro 2024
df = pd.read_csv(r'C:\COMP_UEL\Estatistica\dataset\campeoanato-brasileiro-2024.csv')

# Definicao dos times participantes do campeonato brasileiro 2024
times = ['Flamengo', 'Palmeiras', 'Botafogo-RJ', 'Fortaleza', 'Internacional',
         'Sao Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
         'Vitoria', 'Atletico-MG', 'Fluminense', 'Gremio', 'Juventude',
         'Bragantino', 'Athletico-PR', 'Criciuma', 'Atletico-GO', 'Cuiaba']

# Criacao do dataframe de stats basicos de cada time
df_stats = pd.DataFrame({
    'Time': times,
    'Total Jogos': 0,
    'Gols Feitos': 0,
    'Gols Sofridos': 0,
    'Média Gols Feitos': 0.0,
    'Média Gols Sofridos': 0.0
})

# Preenchimento dos dados e estatisticas dos times individualmente
for time in times:
    mandante = df[df['mandante'] == time]
    visitante = df[df['visitante'] == time]

    total_jogos = len(mandante) + len(visitante)

    gols_feitos = mandante['mandante_Placar'].sum() + visitante['visitante_Placar'].sum()
    gols_sofridos = mandante['visitante_Placar'].sum() + visitante['mandante_Placar'].sum()

    df_stats.loc[df_stats['Time'] == time, 'Total Jogos'] = total_jogos
    df_stats.loc[df_stats['Time'] == time, 'Gols Feitos'] = gols_feitos
    df_stats.loc[df_stats['Time'] == time, 'Gols Sofridos'] = gols_sofridos
    df_stats.loc[df_stats['Time'] == time, 'Média Gols Feitos'] = gols_feitos / total_jogos if total_jogos else 0
    df_stats.loc[df_stats['Time'] == time, 'Média Gols Sofridos'] = gols_sofridos / total_jogos if total_jogos else 0

# Salvamento do dataframe dos stats
df_stats.to_csv(r'C:\COMP_UEL\Estatistica\dataset\2024_goal_stats.csv', index=False)
