from vendas import Vendas
from database import Database
from plot import Plot
from datetime import datetime
import pandas as pd


def main():
    db = Database(host="localhost", user="root",
                  password="", database="vendas")

    vendas = Vendas('./arquivos/vendas_mercadinho_agosto.xlsx')
    todas_vendas = vendas.obtenha_todas_vendas()

    for index, row in todas_vendas.iterrows():
        db.inserir_venda(row['Produto'], row['Quantidade'], row['DataVenda'])

    mes = datetime.now().strftime('%Y-%m')
    top10_vendas = db.consultar_top10_vendas(mes)

    plot = Plot(df=pd.DataFrame(
        top10_vendas, columns=['Produto', 'TotalVendas']))
    plot.plot_top10()


if __name__ == "__main__":
    main()
