# :books: vasfe-cms
Source code for VASFE's website built with Wagtail, a Django Content Management System.

:brazil: [README em português](https://github.com/vitorgongora/vasfe-cms/blob/master/README.pt-BR.md)
## Installation instructions
### Linux (Ubuntu)
You should have at least Python 3.5 installed (check with ```python3 --version```).<br/>

Download the ZIP file or clone using git:<br/>
```bash
git clone https://github.com/vitorgongora/vasfe-cms.git
```

Install the necessary packages:
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
You should have at least Python 3.5 installed (check with ```python3 --version```).<br/>

Clone the files from the repository:<br/>
```bash
git clone https://github.com/vitorgongora/vasfe-cms.git
cd vasfe-cms
```
Install PostgreSQL 12 binary https://www.enterprisedb.com/downloads/postgres-postgresql-downloads<br/>

Install the necessary packages:
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

### Configuring database
#### Linux (Ubuntu)
```bash
sudo -i -u postgres
psql
CREATE USER wagtail_dev WITH PASSWORD 'admin';
CREATE DATABASE wagtail OWNER wagtail_dev;
\q
```

#### Windows
Create a database named wagtail using pgAdmin4 (GUI), already installed with the binary.
You can either create a new user using pgAdmin4 (username: wagtail_dev/password: admin) or use 
(username: postgres/password: *defined during installation*).

If you choose the latter make sure to change your credentials in ./cms/settings/base.py lines 100-101.

Alternatively add PostgreSQL to your environment variables and run the commands below.
```bash
psql
CREATE USER wagtail_dev WITH PASSWORD 'admin';
CREATE DATABASE wagtail OWNER wagtail_dev;
\q
```

## Running the application
```bash
source vasfe_cms_env/bin/activate
cd vasfe-cms
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

You can now access http://127.0.0.1:8000/admin with the superuser credentials.

## Setting up the pages
Inside the Admin Panel go to "Pages" and click on the only option.
Click on "Add subpage" and add a "Blog cat index page". On the content tab insert **title:** Posts por núcleo, on the
promote tab insert **slug:** cats.

Now repeat the exact same process for the following page types:

* "Blog index page", **title:** Blog, **slug:** blog

* "Blog tag index page", **title:** Tags, **slug:** tags

* "Cores page", **title:** Núcleos de Desenvolvimento, **slug:** nucleos

* "Std page", **title:** Como entrar em contato, **slug:** contato

To add a Blog Post hover over the "Blog index page" you just created and click on "Add Subpage", then select "Blog page".

To add a new "Núcleo" locate and click "Fragments" on the sidebar, click on "Núcleos" then click on "Add blog category".

:tada: You're all set up now!

## Contribution guidelines
You must create a fork and submit a pull request, direct merges to master aren't allowed.

There is a CD (Continuous Delivery) process that will push changes to the master branch to production.
