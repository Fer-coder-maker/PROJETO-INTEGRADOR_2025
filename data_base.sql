-- =========================================
-- BANCO DE DADOS
-- =========================================
CREATE DATABASE IF NOT EXISTS planejaai;
USE planejaai;

-- =========================================
-- TABELA: perfil
-- =========================================
CREATE TABLE IF NOT EXISTS perfil (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

-- =========================================
-- TABELA: eventos
-- =========================================
CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nome_evento VARCHAR(150) NOT NULL,
    data_evento DATE,
    local_evento VARCHAR(150),
    FOREIGN KEY (id_usuario) REFERENCES perfil(id_usuario)
);

-- =========================================
-- TABELA: convidados
-- =========================================
CREATE TABLE IF NOT EXISTS convidados (
    id_convidado INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    nome_convidado VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(150),
    status_presenca ENUM('Pendente','Respondido','Não Confirmado') DEFAULT 'Pendente',
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

-- =========================================
-- TABELA: orcamento
-- =========================================
CREATE TABLE IF NOT EXISTS orcamento (
    id_orcamento INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor_estimado DECIMAL(10,2) NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);
