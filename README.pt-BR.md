# :books: vasfe-cms
Código fonte para o site do VASFE, criado com o Wagtail, um CMS baseado em Django.

:us: [README in English](https://github.com/vitorgongora/vasfe-cms/blob/master/README.pt-BR.md)
## Instruções de instalação
### Linux (Ubuntu)
Você deve ter no mínimo Python 3.5 instalado (cheque com ``python3 --version```).<br/>

Baixe o arquivo ZIP ou clone usando git:<br/>
```bash
git clone https://github.com/vitorgongora/vasfe-cms.git
```

Instale os pacotes necessários:
```bash
sudo apt install postgresql-12
sudo apt install libjpeg-dev
python3 -m pip install --upgrade pip
python3 -m pip install --user virtualenv
virtualenv vasfe_cms_env
source vasfe_cms_env/bin/activate
python3 -m pip install --upgrade Pillow
python3 -m pip install django===2.2
python3 -m pip install wagtail===2.4
python3 -m pip install psycopg2-binary
```

### Windows
Você deve ter no mínimo Python 3.5 instalado (cheque com ``python3 --version```).<br/>

Baixe o arquivo ZIP ou clone usando git:<br/>
```bash
git clone https://github.com/vitorgongora/vasfe-cms.git
cd vasfe-cms
```
Instale o binário dp PostgreSQL 12 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads<br/>

Instale os pacotes necessários:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --user virtualenv
virtualenv vasfe_cms_env
source vasfe_cms_env/bin/activate
python3 -m pip install --upgrade Pillow
python3 -m pip install django===2.2
python3 -m pip install wagtail===2.4
python3 -m pip install psycopg2-binary
```

### Configurando o banco de dados
#### Linux (Ubuntu)
```bash
sudo -i -u postgres
psql
CREATE USER wagtail_dev WITH PASSWORD 'admin';
CREATE DATABASE wagtail OWNER wagtail_dev;
\q
```

#### Windows
Crie um banco de dados com o nome wagtail usando a GUI do pgAdmin4, já instalado com o binário. Você pode criar um novo usuário com o pgAdmin4 (username: wagtail_dev/password: admin) ou usar (username: postgres/password: *definido durante instalação*).

Se escolher a última opção altere suas credenciais em ./cms/settings/base.py linhas 100-101.

Alternativamente adicione PostgreSQL nas variáveis de ambiente (environment variables) e execute os comandos abaixo:
```bash
psql
CREATE USER wagtail_dev WITH PASSWORD 'admin';
CREATE DATABASE wagtail OWNER wagtail_dev;
\q
```

## Iniciando a aplicação
```bash
source vasfe_cms_env/bin/activate
cd vasfe-cms
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Você consegue agora acessar http://127.0.0.1:8000/admin com as credenciais do superuser.

## Configurando as páginas
Dentro do painel de Administração clique em “Páginas” e clique na única opção.
Clique em “Adicionar sub página” e adicione “Blog cat index page”. Na aba “Conteúdo” insira **título:** Posts por núcleo, na aba “Promover” insira **slug:** cats. 

Repita exatamente o mesmo processo para as páginas abaixo:

* "Blog index page", **título:** Blog, **slug:** blog

* "Blog tag index page", **título:** Tags, **slug:** tags

* "Cores page", **título:** Núcleos de Desenvolvimento, **slug:** nucleos

* "Std page", **título:** Como entrar em contato, **slug:** contato

Para adicionar um Post no Blog coloque o cursor do mouse em cima da página do tipo “Blog index page” que você acabou de criar, clique em “Adicionar sub página” e selecione “Blog page”.

Para adicionar um novo núcleo localize e clique em “Fragmentos” na barra lateral, clique em “Núcleos” e clique em “Add blog category”.

:tada: Tudo configurado!

## Diretrizes de contribuição
É preciso criar um fork e enviar um pull request, merges diretos para a branch master não são permitidos.

Existe um processo de CD (Entrega contínua) que envia as mudanças na branch master para o ambiente de produção.
