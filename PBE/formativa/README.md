🏫 Sistema de Gerenciamento de Professores e Ambientes
Este projeto tem como objetivo facilitar a gestão educacional em instituições de ensino por meio de um sistema que organiza o cadastro de professores, disciplinas e reservas de salas de aula. O sistema foi desenvolvido utilizando Django e Django REST Framework, com foco na separação de permissões entre gestores e professores.

📌 Contexto
A gestão educacional envolve desafios diários, como a organização de horários, professores, disciplinas e espaços físicos. Este sistema surge como solução para automatizar e centralizar essas informações, promovendo um ambiente educacional mais eficiente, transparente e menos sujeito a erros operacionais.

🎯 Objetivo
Desenvolver uma API RESTful para gerenciamento de:

Professores

Disciplinas

Reservas de Ambientes

A aplicação conta com autenticação e autorização de usuários, garantindo diferentes níveis de acesso:

Gestores: podem realizar todas as operações (CRUD).

Professores: acesso somente leitura às suas disciplinas e reservas.

⚙️ Tecnologias Utilizadas
Python

Django

Django REST Framework

MySQL

JWT (para autenticação)

Swagger/Postman (para documentação da API)

🗂️ Funcionalidades do Back-end
📚 Professores
 Criar professor

 Listar todos os professores

 Atualizar informações

 Deletar professor

📖 Disciplinas
 Criar disciplina

 Listar disciplinas

 Atualizar informações

 Deletar disciplina

🏫 Reservas de Ambiente
 Criar reserva

 Listar reservas

 Deletar reserva

🔐 Autenticação e Autorização
 Login com JWT

 Acesso restrito para professores (somente leitura)

 Permissões de CRUD exclusivas para gestores

🧱 Modelo de Dados
Professor
NI

Nome

E-mail

Telefone

Data de nascimento

Data de contratação

Disciplinas atribuídas

Disciplina
Nome

Curso

Carga horária

Descrição

Professor responsável

Reserva de Ambiente
Data de início e término

Período (manhã/tarde/noite)

Sala reservada

Professor responsável

Disciplina associada

🚀 Etapas do Projeto
Configuração do Ambiente

Instalação do Django e DRF

Configuração do banco MySQL

Modelagem e Endpoints

Criação de modelos, serializers e views

Implementação das regras de negócio e permissões

Autenticação

JWT e restrição por perfil de usuário

Validações e Testes

Verificação de fluxos e integridade dos dados

Documentação

Swagger ou Postman

📎 Instalação
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver