import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def connect(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

    def inserir_venda(self, produto, quantidade, data_venda):
        self.connect()
        self.cursor.execute("INSERT INTO historico (produto, quantidade, data_venda) VALUES (%s, %s, %s)",
                            (produto, quantidade, data_venda))
        self.conexao.commit()
        self.disconnect()

    def consultar_top10_vendas(self, mes):
        self.connect()
        self.cursor.execute("""
        SELECT produto, SUM(quantidade) as total_vendas
        FROM historico
        WHERE DATE_FORMAT(data_venda, '%Y-%m') = %s
        GROUP BY produto
        ORDER BY total_vendas DESC
        LIMIT 10
        """, (mes,))
        resultados = self.cursor.fetchall()
        self.disconnect()
        return resultados
