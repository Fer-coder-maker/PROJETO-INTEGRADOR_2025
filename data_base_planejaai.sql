CREATE TABLE eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome_evento VARCHAR(255) NOT NULL,
    data_evento DATE,
    local_evento VARCHAR(255),
    orcamento_total DECIMAL(10,2) DEFAULT 0
);

CREATE TABLE convidados (
    id_convidado INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT NOT NULL,
    nome_convidado VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(255),
    status_presenca VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

CREATE TABLE fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(255),
    preco_estimado DECIMAL(10,2)
);

CREATE TABLE evento_fornecedores (
    id_evento INT NOT NULL,
    id_fornecedor INT NOT NULL,
    papel VARCHAR(255),
    PRIMARY KEY (id_evento, id_fornecedor),
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
);

