## Environment

Ubuntu 18.04, Python 3.6, Django 2.1

## Setting up

### Docker

```
$ git clone https://github.com/t-cool/tcool.git
$ cd tcool
$ docker build -t tcool/tcool:1.0 .
$ docker run -v `pwd`:/root/work -it -p 8000:8000 tcool/tcool:1.0 /bin/bash
#\ python3 manage.py migrate
#\ python3 manage.py createsuperuser
#\ python3 manage.py runserver 0:8000
```

### Docker Compose

```
$ git clone https://github.com/t-cool/tcool.git
$ cd tcool
$ docker-compose up
```

### Manual steps

1. clone the app locally:

```bash
$ git clone https://github.com/t-cool/tcool.git
```

2. install all the dependencies:

```bash
$ cd tcool
$ pip install -r requirements/local.txt
```

3. download the textblob corpus and NLTK data:

```bash
$ python -m textblob.download_corpora
$ python -m nltk.downloader all
```

4. run the database migrations:

```bash
$ python manage.py migrate
```

5.  create admin user

```bash
$ python manage.py createsuperuser
```

6. start the application:

```bash
$ python manage.py runserver
```

Then access to [http://localhost:8000](http://localhost:8000) on a browser.
