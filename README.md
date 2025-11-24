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



🎨 Protótipo e Evolução do Projeto
🖼 Primeiro Protótipo no Figma

O projeto começou com um protótipo inicial criado no Figma, focado em:

Estrutura visual das telas

Organização da navegação

Definição da identidade do aplicativo

Esse protótipo serviu como base para validar:

Fluxos iniciais

Posições de elementos

Primeiras ideias de usabilidade

Ele representou a visão inicial do Planejaaí antes da implementação técnica.

👉 [Acessar o protótipo no Figma](https://www.figma.com/proto/0GxTuWj14m4BvQ4K73J4Ub/PI-SENAC?node-id=5-707&p=f&t=7Qu2G4Sl7hA2GUdv-1&scaling=contain&content-scaling=fixed&page-id=0%3A1)




📲 Adaptação e Evolução para o App Final

Após a validação do protótipo, o layout foi adaptado e evoluído para o ambiente do Glide, considerando:

✔ Necessidades reais surgidas no processo de desenvolvimento

✔ Simplificação dos fluxos de cadastro (eventos, convidados e orçamento)

✔ Integração entre telas e experiências

✔ Limitações e possibilidades da plataforma Glide

Essa evolução transformou o design inicial em um aplicativo funcional, resultando em um MVP sólido, focado na entrega prática das funcionalidades essenciais.




### 🎥 Vídeo de Apresentação do MVP

👉 [Clique aqui para assistir no YouTube](https://www.youtube.com/shorts/jJLv3k5cb4g)


