import pandas as pd


df = pd.read_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\campeonato-brasileiro-full.csv')

df_2024 = df[df['ID'] >= 8406]

df_2024.to_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\campeonato-brasileiro-2024.csv', index=False)





