import mysql.connector

# ==========================================
# CONEXÃO
# ==========================================
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="planejaai"
    )

# ==========================================
# SQL COMPLETO (TABELAS ATUALIZADAS)
# ==========================================
sql_schema = """
CREATE DATABASE IF NOT EXISTS planejaai;
USE planejaai;

CREATE TABLE IF NOT EXISTS perfil (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nome_evento VARCHAR(150) NOT NULL,
    data_evento DATE,
    local_evento VARCHAR(150),
    FOREIGN KEY (id_usuario) REFERENCES perfil(id_usuario)
);

CREATE TABLE IF NOT EXISTS convidados (
    id_convidado INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    nome_convidado VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(150),
    status_presenca ENUM('Pendente','Respondido','Não Confirmado') DEFAULT 'Pendente',
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

CREATE TABLE IF NOT EXISTS orcamento (
    id_orcamento INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor_estimado DECIMAL(10,2) NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);
"""

# ==========================================
# EXECUTAR CRIAÇÃO/ATUALIZAÇÃO DO BANCO
# ==========================================
def inicializar_banco():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA"
    )
    cursor = conn.cursor()
    for comando in sql_schema.split(";"):
        c = comando.strip()
        if c:
            cursor.execute(c)
    conn.commit()
    conn.close()
    print("Banco atualizado com sucesso!")

# ==========================================
# CRUD — PERFIL
# ==========================================
def criar_perfil(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO perfil (nome, email, senha)
        VALUES (%s, %s, %s)
    """, (nome, email, senha))
    conn.commit()
    conn.close()

def listar_perfis():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM perfil")
    data = cursor.fetchall()
    conn.close()
    return data

def atualizar_perfil(id_usuario, nome=None, email=None, senha=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE perfil
        SET nome = COALESCE(%s, nome),
            email = COALESCE(%s, email),
            senha = COALESCE(%s, senha)
        WHERE id_usuario = %s
    """, (nome, email, senha, id_usuario))
    conn.commit()
    conn.close()

def deletar_perfil(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM perfil WHERE id_usuario = %s", (id_usuario,))
    conn.commit()
    conn.close()

# ==========================================
# CRUD — EVENTOS
# ==========================================
def criar_evento(id_usuario, nome_evento, data_evento, local_evento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO eventos (id_usuario, nome_evento, data_evento, local_evento)
        VALUES (%s, %s, %s, %s)
    """, (id_usuario, nome_evento, data_evento, local_evento))
    conn.commit()
    conn.close()

def listar_eventos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eventos")
    data = cursor.fetchall()
    conn.close()
    return data

def atualizar_evento(id_evento, nome=None, data=None, local=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE eventos
        SET nome_evento = COALESCE(%s, nome_evento),
            data_evento = COALESCE(%s, data_evento),
            local_evento = COALESCE(%s, local_evento)
        WHERE id_evento = %s
    """, (nome, data, local, id_evento))
    conn.commit()
    conn.close()

def deletar_evento(id_evento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM eventos WHERE id_evento = %s", (id_evento,))
    conn.commit()
    conn.close()

# ==========================================
# CRUD — CONVIDADOS
# ==========================================
def criar_convidado(id_evento, nome, telefone, email, status="Pendente"):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO convidados (id_evento, nome_convidado, telefone, email, status_presenca)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_evento, nome, telefone, email, status))
    conn.commit()
    conn.close()

def listar_convidados(id_evento=None):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    if id_evento:
        cursor.execute("SELECT * FROM convidados WHERE id_evento = %s", (id_evento,))
    else:
        cursor.execute("SELECT * FROM convidados")
    data = cursor.fetchall()
    conn.close()
    return data

def atualizar_convidado(id_convidado, nome=None, telefone=None, email=None, status=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE convidados
        SET nome_convidado = COALESCE(%s, nome_convidado),
            telefone = COALESCE(%s, telefone),
            email = COALESCE(%s, email),
            status_presenca = COALESCE(%s, status_presenca)
        WHERE id_convidado = %s
    """, (nome, telefone, email, status, id_convidado))
    conn.commit()
    conn.close()

def deletar_convidado(id_convidado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM convidados WHERE id_convidado = %s", (id_convidado,))
    conn.commit()
    conn.close()

# ==========================================
# CRUD — ORÇAMENTO
# ==========================================
def criar_orcamento(id_evento, categoria, valor_estimado, observacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orcamento (id_evento, categoria, valor_estimado, observacoes)
        VALUES (%s, %s, %s, %s)
    """, (id_evento, categoria, valor_estimado, observacoes))
    conn.commit()
    conn.close()

def listar_orcamentos(id_evento=None):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    if id_evento:
        cursor.execute("SELECT * FROM orcamento WHERE id_evento = %s", (id_evento,))
    else:
        cursor.execute("SELECT * FROM orcamento")
    data = cursor.fetchall()
    conn.close()
    return data

def atualizar_orcamento(id_orcamento, categoria=None, valor=None, obs=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE orcamento
        SET categoria = COALESCE(%s, categoria),
            valor_estimado = COALESCE(%s, valor_estimado),
            observacoes = COALESCE(%s, observacoes)
        WHERE id_orcamento = %s
    """, (categoria, valor, obs, id_orcamento))
    conn.commit()
    conn.close()

def deletar_orcamento(id_orcamento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orcamento WHERE id_orcamento = %s", (id_orcamento,))
    conn.commit()
    conn.close()


# ==========================================
# EXECUTAR AO RODAR O ARQUIVO
# ==========================================
if __name__ == "__main__":
    inicializar_banco()
    print("Sistema pronto!")
