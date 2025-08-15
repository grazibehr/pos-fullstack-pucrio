# ============================================
# EXERCICIO 17 – SELECT / FROM - SQL
# --------------------------------------------
#  Liste todos os bares que aparecem na tabela Vendem
# ============================================
import sqlite3

def executar_sql():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # 1) Cria a tabela
    cur.execute('''
        CREATE TABLE Vendem (
            Bar TEXT,
            Cerveja TEXT
        )
    ''')

# 2) Insere  dados
    cur.executemany(
        'INSERT INTO Vendem (Bar, Cerveja) VALUES (?, ?)',
        [
            ('Bar do Viking', 'Itaipava'),
            ('BrazBar',    'Skol'),
            ('NightBar',   'Artesanal')
        ]
    )

    # 3) Executa o SELECT e imprime
    cur.execute('SELECT Bar FROM Vendem')
    bares = [row[0] for row in cur.fetchall()]

    print("Bares encontrados:")
    for bar in bares:
        print(" -", bar)

    # fecha conexão
    conn.close()

if __name__ == '__main__':
    executar_sql()

    