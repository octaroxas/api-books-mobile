<img align="right" src="http://www.ufopa.edu.br/ppge/images/ppge/imagens/Ufopa_braso_PNG_fundo_transparente.png" style="width: 80px;" alt="UFOPA's Logo" />

# _Égua, onde eu tava?_
> Versão atual: v0.1.5 (2023-06-12).

<img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Python-292e33?style=flat-square&logo=Python&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Docker-292e33?style=flat-square&logo=Docker&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/FastAPI-292e33?style=flat-square&logo=FastAPI&logoColor=fff"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/PostgreSQL-292e33?style=flat-square&logo=Postgresql&logoColor=fff">

> `Backend` feito com ❤️ por Lucas Rodrigues (<a href="https://github.com/NepZR/" target="_blank">@NepZR</a>). Repositório associado e desenvolvido para o projeto da disciplina de "Tópicos Especiais em Computação Móvel", no Semestre 2022.2 da UFOPA. Para acessar o `Frontend`, <a href="https://github.com/octaroxas/mobile-books-app">clique aqui</a>.

#### ⚠️ Disclaimer: o código desta parte do projeto está sendo desenvolvido em paralelo com as aulas e também, quando possível, durante os slots de tempo livre fora das aulas. Este documento (README) será mantido atualizado conforme novas alterações forem realizadas no repositório.

---

### 📂 Estrutura do repositório
- `docs/`: as documentações específicas para cada módulo que compõe o backend e a API estarão disponíveis dentro deste diretório, todos em formato `Markdown (.MD)` e padronizados conforme o modelo deste README. 
- `database/`: itens relacionados à base de dados estarão dentro deste diretório, como diagramas e Scripts SQL.
- `api/`: os pacotes, módulos e códigos associados ao backend/API do aplicativo estarão nesta pasta.

---

### 🚀 Guia de início
<a href="https://docs.docker.com/get-docker/"><img style="width: auto; padding-right: 5px;" src="https://img.shields.io/badge/Docker (Compose)-292e33?style=flat-square&logo=Docker&logoColor=fff"><br></a>

#### 1. Clonar este repositório via SSH ou HTTPS
~~~bash
git clone git@github.com:octaroxas/api-books-mobile.git
~~~
~~~bash
git clone https://github.com/octaroxas/api-books-mobile.git
~~~

#### 2. Acessar a raiz do repositório
~~~bash
cd api-books-mobile
~~~

#### 3. Iniciar o backend localmente
~~~bash
docker-compose -f docker-compose-local.yaml up -d --build
~~~
> Isso inicializará, simultaneamente, o banco de dados (PostgreSQL) e o servidor de backend via Uvicorn no Python 3.11.

#### 4. Acessar o endpoint com a documentação da API
~~~bash
http://localhost:5000/documentation
~~~

#### Para interromper, utilize o comando abaixo
~~~bash
docker-compose -f docker-compose-local.yaml down
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
