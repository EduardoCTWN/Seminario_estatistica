import pandas as pd

# Leitura do dataset relacionado ao dados do campeonato brasilreiro de 2003-2024
df = pd.read_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\campeonato-brasileiro-full.csv')

# Filtro somente para o ano de 2024
df_2024 = df[df['ID'] >= 8406]

# Salvar dataset campeonato brasileiro 2024
df_2024.to_csv(r'C:\COMP_UEL\Estatistica\Seminario_estatistica\dataset\campeonato-brasileiro-2024.csv', index=False)





