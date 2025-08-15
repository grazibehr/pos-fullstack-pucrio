# ============================================
# EXERCICIO 18 – SELECT MULTIPLAS COLUNAS - SQL
# --------------------------------------------
#  Liste a cidade e o estado de cada consumidor
# ============================================

import sqlite3
import sqlite3

def executar_sql():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # 1) Cria a tabela
    cur.execute('''
        CREATE TABLE Consumidores (
            cpf VARCHAR,
            rg VARCHAR,
            nome VARCHAR,
            cidade VARCHAR,
            uf VARCHAR
        )
    ''')

    # 2) Insere dados
    cur.executemany(
        'INSERT INTO Consumidores (cpf, rg, nome, cidade, uf) VALUES (?, ?, ?, ?, ?)',
        [
            ('12345678901', 'MG0156521', 'Bianca Santos',   'Belo Horizonte',  'MG'),
            ('98765432100', 'SP2345678', 'Bruno Barbosa',   'Sao Paulo',       'SP'),
            ('55566677788', 'RJ3456789', 'Natália Ferreira','Rio de Janeiro',  'RJ'),
        ]
    )
    conn.commit()

    # 3) Executa o SELECT e imprime cidade e UF
    cur.execute('SELECT cidade, uf FROM Consumidores')
    consumidores = cur.fetchall()  # lista de tuplas (cidade, uf)

    print("Cidade & Estado de cada consumidor:")
    for cidade, uf in consumidores:
        print(f" - {cidade} / {uf}")

    conn.close()

if __name__ == '__main__':
    executar_sql()
