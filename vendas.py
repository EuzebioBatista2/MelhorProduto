import pandas as pd


class Vendas:
    def __init__(self, arquivo_excel):
        self.df = pd.read_excel(arquivo_excel)

    def obtenha_todas_vendas(self):
        return self.df

    def obtenha_top10_vendas(self):
        df_produtos = self.df.groupby(
            'Produto')['Quantidade'].sum().reset_index()
        df_produtos = df_produtos.sort_values(by='Quantidade', ascending=False)
        return df_produtos.head(10)
