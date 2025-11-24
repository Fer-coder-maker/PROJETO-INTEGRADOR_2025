import mysql.connector

# ---------------------------
# CONEXÃO COM O BANCO
# ---------------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="planejaai"
    )

# ===========================
# CRUD – TABELA PERFIL
# ===========================
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
    perfis = cursor.fetchall()
    conn.close()
    return perfis

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


# ===========================
# CRUD – TABELA EVENTOS
# ===========================
def criar_evento(nome_evento, data_evento, local_evento, id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO eventos (nome_evento, data_evento, local_evento, id_usuario)
        VALUES (%s, %s, %s, %s)
    """, (nome_evento, data_evento, local_evento, id_usuario))
    conn.commit()
    conn.close()

def listar_eventos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eventos")
    eventos = cursor.fetchall()
    conn.close()
    return eventos

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


# ===========================
# CRUD – TABELA CONVIDADOS
# ===========================
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

    convidados = cursor.fetchall()
    conn.close()
    return convidados

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


# ===========================
# CRUD – TABELA ORÇAMENTO
# ===========================
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

    orc = cursor.fetchall()
    conn.close()
    return orc

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
