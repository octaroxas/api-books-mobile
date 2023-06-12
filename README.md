<img align="right" src="http://www.ufopa.edu.br/ppge/images/ppge/imagens/Ufopa_braso_PNG_fundo_transparente.png" style="width: 80px;" alt="UFOPA's Logo" />

# _Égua, onde eu tava_

<img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Python-292e33?style=flat-square&logo=Python&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Pipenv-292e33?style=flat-square&logo=Python&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Miniconda-292e33?style=flat-square&logo=Anaconda&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Docker-292e33?style=flat-square&logo=Docker&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/FastAPI-292e33?style=flat-square&logo=FastAPI&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/PostgreSQL-292e33?style=flat-square&logo=Postgresql&logoColor=fff">

> `Backend` feito com ❤️ por Lucas Rodrigues (<a href="https://github.com/NepZR/" target="_blank">@NepZR</a>). Repositório associado e desenvolvido para o projeto da disciplina de "Tópicos Especiais em Computação Móvel", no Semestre 2022.2 da UFOPA. Para acessar o `Frontend`, <a href="https://github.com/octaroxas/mobile-books-app">clique aqui</a>.

#### ⚠️ Disclaimer: o código desta parte do projeto está sendo desenvolvido em paralelo com as aulas e também, quando possível, durante os slots de tempo livre fora das aulas. Este documento (README) será mantido atualizado conforme novas alterações forem realizadas no repositório.

---

### 📂 Estrutura do repositório
- `docs/`: as documentações específicas para cada módulo que compõe o backend e a API estarão disponíveis dentro deste diretório, todos em formato `Markdown (.MD)` e padronizados conforme o modelo deste README. 
- `database/`: arquivos, como relacionados ao Docker - para o PostgreSQL, por exemplo - e outros itens relacionados à base de dados estarão dentro deste diretório.
- `api/`: os pacotes, módulos e códigos associados ao backend/API do aplicativo estarão nesta pasta.

---

### 🚀 Guia de início
<img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Pipenv-292e33?style=flat-square&logo=Python&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Miniconda-292e33?style=flat-square&logo=Anaconda&logoColor=fff"><br>
> Será considerado que o Python 3.11 e o Python Package Manager (PIP) estão instalados no sistema alvo. Caso não tenha instalado, clique <a href="https://wiki.python.org/moin/BeginnersGuide/Download">aqui</a> e siga as instruções de instalação conforme a documentação oficial. Também é possível configurar o ambiente com o Miniconda, acesse <a href="https://conda.io/en/latest/miniconda">aqui</a>. Além disso, será necessária a instalação do Docker e Docker-Compose no sistema. Para isso, siga as instruções disponíveis <a href="https://docs.docker.com/get-docker/">aqui</a>.

#### 1. Instalar o Python Environment Shell (`pipenv`) OU criar um Miniconda Environment para o projeto (`conda`)
~~~bash
pip install pipenv
~~~
~~~bash
conda create -n api_books_mobile python=3.11 -y && conda activate api_books_mobile
~~~

#### 2. Clonar este repositório via SSH ou HTTPS
~~~bash
git clone git@github.com:octaroxas/api-books-mobile.git
~~~
~~~bash
git clone https://github.com/octaroxas/api-books-mobile.git
~~~

#### 3. Acessar a raiz do repositório
~~~bash
cd api-books-mobile
~~~

#### 4. Inicializar o ambiente via Pipenv (primeiro comando) OU instalar as dependências, caso esteja via Miniconda (segundo comando)
~~~bash
pipenv shell && pipenv install
~~~
> Esse comando cria, localmente, um ambiente isolado com o Python 3.11 para o projeto e, automaticamente, configura todas as bibliotecas e dependências para a correta execução.

~~~bash
pip install -r requirements.txt
~~~

---

### 🚀 Executando o projeto
> Será considerado que os passos da seção `🚀 Guia de início` foram executados previamente.

#### 1. Acessar a pasta do projeto
~~~bash
cd api-books-mobile
~~~

#### 2. Iniciar o banco de dados (PostgreSQL, Docker)
~~~bash
docker-compose -f database/docker/docker-compose.yaml up -d --build 
~~~

#### 3. Entrar no ambiente Pipenv do projeto OU ativar o environment via Miniconda
> Certifique-se de executar este comando **sempre** na raiz do repositório: `api-books-mobile`.
~~~bash
pipenv shell
~~~
~~~bash
conda activate api_books_mobile
~~~

#### 4. Iniciar o backend/API com o Uvicorn
~~~bash
uvicorn books_mobile:app --host 0.0.0.0 --port 5000
~~~

---

<h3 style="text-align: justify;">
  👨🏻‍💻 Repository Maintainer
</h3>

<table style="display: flex;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Data Engineer | Python Dev.</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr"><sub><b>LinkedIn (lucasdfr)</b></sub></a></td>
  </tr>
<table>

---

<h3 style="text-align: justify;">
  👨🏻‍💻 Full Development Team
</h3>

<table style="display: flex;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Data Engineer | Python Dev.</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr"><sub><b>LinkedIn (lucasdfr)</b></sub></a></td>
    <td align="center"><a href="https://github.com/octaroxas"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/46870808?v=4" width="100px;" alt=""/><br /><sub><b>Octacílio Carvalho de Almeida</b></sub></a><br /><sub><b>Full Stack Dev.</sub></a><br /><a href="https://www.linkedin.com/in/octacilio-c-almeida"><sub><b>LinkedIn (octacilio-c-almeida)</b></sub></a></td>
    <td align="center"><a href="https://github.com/J-NSC"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/58124203?v=4" width="100px;" alt=""/><br /><sub><b>João Paulo Nascimento da Costa</b></sub></a><br /><sub><b>C# Dev. | Unity Engine Dev.</sub></a><br /><a href="https://www.linkedin.com/in/joao-devunity"><sub><b>LinkedIn (joao-devunity)</b></sub></a></td>
  </tr>
<table>
