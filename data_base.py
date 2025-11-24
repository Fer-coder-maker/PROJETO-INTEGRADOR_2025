import mysql.connector
from mysql.connector import Error

# --------------------------------------------------------
# 1. Função de conexão
# --------------------------------------------------------
def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SUA_SENHA",
            database="planejaai"
        )
        return conn
    except Error as e:
        print("Erro ao conectar:", e)
        return None


# --------------------------------------------------------
# 2. Criar banco (se não existir)
# --------------------------------------------------------
def criar_banco():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SUA_SENHA"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS planejaai")
        print("Banco criado/verificado com sucesso.")
        cursor.close()
        conn.close()
    except Error as e:
        print("Erro:", e)


# --------------------------------------------------------
# 3. Criar tabelas do modelo físico
# --------------------------------------------------------
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    tabelas = [
        """
        CREATE TABLE IF NOT EXISTS eventos (
            id_evento INT AUTO_INCREMENT PRIMARY KEY,
            nome_evento VARCHAR(255) NOT NULL,
            data_evento DATE,
            local_evento VARCHAR(255),
            orcamento_total DECIMAL(10,2) DEFAULT 0
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS convidados (
            id_convidado INT AUTO_INCREMENT PRIMARY KEY,
            id_evento INT NOT NULL,
            nome_convidado VARCHAR(255) NOT NULL,
            telefone VARCHAR(20),
            email VARCHAR(255),
            status_presenca VARCHAR(50) DEFAULT 'Pendente',
            FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS fornecedores (
            id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
            nome_fornecedor VARCHAR(255) NOT NULL,
            categoria VARCHAR(100),
            telefone VARCHAR(20),
            email VARCHAR(255),
            preco_estimado DECIMAL(10,2)
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS evento_fornecedores (
            id_evento INT NOT NULL,
            id_fornecedor INT NOT NULL,
            papel VARCHAR(255),
            PRIMARY KEY (id_evento, id_fornecedor),
            FOREIGN KEY (id_evento) REFERENCES eventos(id_evento),
            FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
        )
        """
    ]

    for tabela in tabelas:
        cursor.execute(tabela)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tabelas criadas com sucesso!")


# --------------------------------------------------------
# 4. Funções CRUD (exemplos)
# --------------------------------------------------------
def inserir_evento(nome, data, local, orcamento):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO eventos (nome_evento, data_evento, local_evento, orcamento_total)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, data, local, orcamento))
    conn.commit()
    print("Evento inserido com sucesso!")
    cursor.close()
    conn.close()


def listar_eventos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eventos")
    eventos = cursor.fetchall()
    cursor.close()
    conn.close()
    return eventos


def atualizar_orcamento(id_evento, novo_valor):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE eventos SET orcamento_total = %s WHERE id_evento = %s"
    cursor.execute(sql, (novo_valor, id_evento))
    conn.commit()
    cursor.close()
    conn.close()
    print("Orçamento atualizado!")


def deletar_evento(id_evento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM eventos WHERE id_evento = %s", (id_evento,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Evento deletado com sucesso!")


# --------------------------------------------------------
# 5. Informações do sistema (versão, tabelas, colunas)
# --------------------------------------------------------
def mostrar_versao():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    versao = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    print("Versão do MySQL:", versao)


def listar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    cursor.close()
    conn.close()
    print("Tabelas no banco:")
    for t in tabelas:
        print("-", t[0])


def estrutura_tabela(nome_tabela):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {nome_tabela}")
    colunas = cursor.fetchall()
    cursor.close()
    conn.close()
    print(f"Estrutura da tabela {nome_tabela}:")
    for c in colunas:
        print(c)


# --------------------------------------------------------
# 6. Execução principal
# --------------------------------------------------------
if __name__ == "__main__":
    criar_banco()
    criar_tabelas()
    mostrar_versao()
    listar_tabelas()
    estrutura_tabela("eventos")

    # Exemplos
    inserir_evento("Festa Teste", "2025-08-10", "Salão Azul", 1500)
    print(listar_eventos())
