from src import soporte as sp

df_v = sp.pd.read_csv('files/ventas.csv')
df_c = sp.pd.read_csv('files/clientes.csv')
df_p = sp.pd.read_csv('files/productos.csv', sep=';')

lista_df = [df_c, df_p, df_v]

for idx, df in enumerate(lista_df, 1):
    print(f"\nDataFrame {idx}: Primeras 5 filas\n")
    print(df.head())
    print('---'*20)

for idx, df in enumerate(lista_df, 1):
    print(f"\nDataFrame {idx}: info\n")
    print(df.info())
    print('---'*20)

for idx, df in enumerate(lista_df, 1):
    print(f"\nDataFrame {idx}: describe\n")
    print(df.describe())
    print('---'*20)

for idx, df in enumerate(lista_df, 1):
    print(f"\nDataFrame {idx}: duplicate\n")
    print(df.duplicated())
    print('---'*20)

for idx, df in enumerate(lista_df, 1):
    print(f"\nDataFrame {idx}: null\n")
    print(df.isna().sum())
    print('---'*20)
