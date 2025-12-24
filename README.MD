🗄️ Simulação de Banco de Dados com Python e SQLite3

Este projeto simula a criação e manipulação de um banco de dados utilizando Python e SQLite3, com foco em organização de código, orientação a objetos e persistência de dados.

O sistema realiza operações básicas de Create (inserção de dados) e Update (atualização de dados), servindo como base para projetos back-end mais completos.

🎯 Objetivo do Projeto

Entender como funciona a integração do Python com o SQLite3

Separar responsabilidades entre lógica de banco de dados e modelos

Criar e atualizar registros em um banco de dados local

Aplicar conceitos iniciais de orientação a objetos

Simular uma arquitetura simples usada em aplicações reais

🛠️ Tecnologias Utilizadas

Python 3

SQLite3 (biblioteca nativa do Python)

📂 Arquitetura do Projeto
📁 projeto-hotelplus
 ├── db.py            # Responsável pela conexão e execução dos comandos SQLite
 ├── Usuario.py       # Classe construtora do usuário (modelo)
 ├── HotelPlus.db     # Banco de dados SQLite
 └── README.md        # Documentação do projeto

📌 Descrição dos Arquivos

db.py
Contém toda a lógica relacionada ao banco de dados, como:

Conexão com o SQLite

Criação de tabelas

Execução de comandos SQL (INSERT e UPDATE)

Usuario.py
Define a classe Usuario, responsável por:

Representar os dados do usuário

Centralizar atributos e facilitar a manipulação dos registros

HotelPlus.db
Banco de dados SQLite onde as informações são persistidas.

⚙️ Funcionalidades Implementadas

✅ Criação de registros no banco de dados (Create)

✅ Atualização de registros existentes (Update)

❌ As operações de Read e Delete não foram implementadas neste projeto.

▶️ Como Executar o Projeto

Certifique-se de ter o Python 3 instalado

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


Acesse a pasta do projeto:

cd projeto-hotelplus


Execute o arquivo principal (ou testes existentes):

python db.py


O arquivo HotelPlus.db será criado automaticamente caso não exista.

📚 Conceitos Abordados

Conexão com banco de dados SQLite

Execução de comandos SQL no Python

Separação de responsabilidades (Database vs Model)

Orientação a objetos básica

Persistência de dados em aplicações back-end

🚀 Possíveis Melhorias Futuras

Implementar as operações Read e Delete (CRUD completo)

Adicionar tratamento de exceções

Criar validações de dados

Integrar com um framework web (RestAPI ou Django)

Utilizar ORM como SQLAlchemy

🧑‍💻 Autor

Victtor Oliveira
Projeto desenvolvido para fins de estudo e prática em desenvolvimento back-end com Python.