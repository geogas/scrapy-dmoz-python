-----------------------
| Project Description | 
-----------------------
That is a simple project illustrating the use of Python Scrapy framework
along with the Postgres database. Our spider scraps the www.dmoz.org
website for books related to Python and Javascript (this can be tweaked
according to the reader needs). We persist the category of the book, the
title and the description.

--------------------------
| Postgres configuration |
--------------------------
vi /etc/postgresql/9.3/main/pg_hba.conf

# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5

------------------------------
| Postgres user and db setup |
------------------------------
$ createuser testuser -d -e -P

$ createdb scrapeDB -U testuser -W

$ psql -d scrapeDB -U testuser -W

-------------
| Execution |
-------------
$ scrapy crawl dmoz 
