import plotly.express as px
import plotly.io as pio


class Plot:
    def __init__(self, df):
        self.df = df

    def plot_top10(self, title='Top 10 Produtos Mais Vendidos'):
        fig = px.bar(self.df, x='Produto', y='TotalVendas', title=title)
        fig.write_html('top10_vendas.html')
