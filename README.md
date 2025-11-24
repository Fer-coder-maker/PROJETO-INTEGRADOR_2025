# 📱 MVP – App de Gestão de Eventos, Convidados e Fornecedores - PlanejaAí

Este repositório contém o MVP de um sistema de gerenciamento de eventos
projetado para testes e validação com usuários reais.

O objetivo é permitir que organizadores de eventos controlem:
- Lista de convidados
- Status de presença
- Envio de convites por email e SMS
- Relação de fornecedores
- Organização geral do evento

---

## 🧱 Estrutura do Banco de Dados

O banco possui quatro tabelas principais:

1. **eventos**
2. **convidados**
3. **fornecedores**
4. **evento_fornecedores** (tabela de junção)

O diagrama lógico está disponível na pasta `/diagrams`.

---

## 📂 Arquivos SQL

### 📌 Modelo físico (CREATE TABLE)
Arquivo: `database/schema.sql`

Contém toda a estrutura do banco:
- criação de tabelas
- chaves primárias e estrangeiras
- relacionamentos

### 📌 CRUD completo
Arquivo: `database/crud.sql`

Inclui:
- INSERT
- SELECT
- UPDATE
- DELETE

### 📌 Dados de exemplo
Arquivo: `database/sample_data.sql`

---

## 📱 Fluxo CRUD no Glide / Adalo

Detalhes em `app/fluxo-glide.md`

Explica:
- Criação de registros (telas de formulário)
- Leitura (listas)
- Atualização (detalhes + edição)
- Exclusão (ações)
- Relacionamentos automáticos

---

## 🚀 Objetivo do MVP

Este MVP serve para:
- Validar a experiência do usuário final
- Testar envios automáticos de convites via email e SMS
- Controlar rapidamente a presença dos convidados
- Unificar o planejamento com fornecedores

---

## 🧪 Como usar

1. Importe o arquivo `schema.sql` para criar o banco.
2. Execute `crud.sql` para testar as operações.
3. Use a ferramenta Glide ou Adalo para conectar com uma planilha ou base SQL.

---

## 📝 Licença

Livre para estudo e desenvolvimento.

