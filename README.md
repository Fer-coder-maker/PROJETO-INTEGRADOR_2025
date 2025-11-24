# 🎉 PlanejaAí — MVP de Gestão de Eventos

O **PlanejaAí** é um MVP desenvolvido para facilitar o planejamento de eventos — especialmente festas infantis — permitindo organizar convidados, orçamento, fornecedores e informações do evento de forma simples e prática.

Este repositório contém:

- Estrutura do banco de dados (MySQL)
- CRUD completo das tabelas principais
- Scripts SQL para criação/atualização das tabelas
- Organização inicial do backend (para futuras integrações via API)

---

## 🚀 Funcionalidades do MVP

- Cadastro de usuários (perfil)
- Cadastro de eventos vinculados ao usuário
- Gestão de convidados com status de presença
- Controle de orçamento por categoria
- Base sólida para futuras integrações com Glide, Adalo, APIs e sistemas de envio de mensagens (WhatsApp, e-mail, SMS)

---

## 🗂️ Estrutura do Banco de Dados (MySQL)

O projeto utiliza **4 tabelas principais**:

### 1. `perfil`
Armazena informações de login e identificação do usuário.

| Campo        | Tipo          |
|--------------|---------------|
| id_usuario   | INT PK AI     |
| nome         | VARCHAR(100)  |
| email        | VARCHAR(120) UNIQUE |
| senha        | VARCHAR(255)  |

---

### 2. `eventos`
Eventos criados pelos usuários.

| Campo         | Tipo          |
|---------------|---------------|
| id_evento     | INT PK AI     |
| id_usuario    | INT FK        |
| nome_evento   | VARCHAR(150)  |
| data_evento   | DATE          |
| local_evento  | VARCHAR(150)  |

---

### 3. `convidados`
Gerenciamento da lista de convidados.

| Campo           | Tipo                                         |
|------------------|----------------------------------------------|
| id_convidado     | INT PK AI                                    |
| id_evento        | INT FK                                       |
| nome_convidado   | VARCHAR(150)                                 |
| telefone         | VARCHAR(20)                                  |
| email            | VARCHAR(150)                                 |
| status_presenca  | ENUM('Pendente','Respondido','Não Confirmado') |

---

### 4. `orcamento`
Organiza os custos e categorias do evento.

| Campo         | Tipo          |
|---------------|---------------|
| id_orcamento  | INT PK AI     |
| id_evento     | INT FK        |
| categoria     | VARCHAR(100)  |
| valor_estimado| DECIMAL(10,2) |
| observacoes   | TEXT          |

---

## 📄 Script SQL do Banco

O arquivo banco está disponível em:  
**`planejaai.sql`**

Esse script:

- Cria o banco `planejaai`
- Gera todas as tabelas
- Implementa relações via chave estrangeira
- Usa padrões adequados ao MySQL

---

## 🔧 CRUD Completo (Python + MySQL)

O arquivo principal é:  
**`planejaai_backend.py`**

Ele contém:

✔ conexão com MySQL  
✔ inicialização automática do banco  
✔ funções CRUD para:  
- perfil  
- eventos  
- convidados  
- orçamento  

### Exemplos do CRUD incluído:

#### ➤ Criar usuário
```python
criar_perfil("Carla Nogueira", "carla@gmail.com", "senha123")
