# 🎓 Sistema de Gerenciamento de Professores e Ambientes

Um sistema desenvolvido com **Django** e **Django REST Framework** que permite a gestão eficiente de professores, disciplinas e reservas de salas em instituições de ensino. Focado em facilitar o trabalho de **gestores** e oferecer uma interface segura de **visualização para professores**.

---

## 🧠 Contexto

A administração educacional envolve a organização de professores, disciplinas e espaços físicos. Com o aumento da complexidade das operações escolares, torna-se essencial o uso de sistemas tecnológicos para otimizar a gestão e garantir um ambiente mais organizado, eficiente e transparente.

---

## 🎯 Objetivo

Criar um sistema para:

- **Cadastrar, visualizar, atualizar e excluir** professores, disciplinas e reservas.
- Restringir permissões com autenticação:
  - **Gestores** têm acesso completo (CRUD).
  - **Professores** possuem acesso restrito à **visualização** das disciplinas e reservas relacionadas.

---

## ⚙️ Tecnologias Utilizadas

- 🐍 Python 3.x  
- 🌐 Django  
- 🔄 Django REST Framework  
- 🛡️ JWT (JSON Web Token)  
- 🗄️ MySQL  
- 📄 Swagger / Postman (Documentação da API)

---

## 🛠️ Funcionalidades

### 👨‍🏫 Professores (Gestores)

- [x] Criar
- [x] Listar
- [x] Atualizar
- [x] Excluir

### 📚 Disciplinas (Gestores)

- [x] Criar
- [x] Listar
- [x] Atualizar
- [x] Excluir

### 🏫 Reservas de Ambiente (Gestores)

- [x] Criar
- [x] Listar
- [x] Atualizar
- [x] Excluir

### 🔐 Autenticação e Permissões

- [x] Login com JWT
- [x] Permissões baseadas no tipo de usuário
- [x] Professores: apenas visualização de suas disciplinas e reservas

---

## 🗃️ Modelo de Dados

### 🔸 Professor

- NI  
- Nome  
- E-mail  
- Telefone  
- Data de nascimento  
- Data de contratação  
- Disciplinas atribuídas (relacionamento)

### 🔸 Disciplina

- Nome  
- Curso  
- Carga horária  
- Descrição  
- Professor responsável (relacionamento)

### 🔸 Reserva de Ambiente

- Data início / término  
- Período (Manhã, Tarde, Noite)  
- Sala reservada  
- Professor responsável (relacionamento)  
- Disciplina associada (relacionamento)

---

## 🚀 Etapas de Desenvolvimento

1. **Ambiente de Desenvolvimento**
   - Configuração do Django, DRF e MySQL

2. **Modelagem e API**
   - Criação dos modelos e endpoints RESTful (CRUD)

3. **Autenticação**
   - JWT para proteger rotas e dividir permissões

4. **Validações**
   - Validação de dados e regras de negócio

5. **Testes**
   - Testes dos fluxos principais (CRUD e autenticação)

6. **Documentação**
   - Swagger ou Postman para documentação da API

---

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados MySQL no settings.py

# Aplique as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver
