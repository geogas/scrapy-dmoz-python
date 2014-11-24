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

- IPv4 local connections:
host    all             all             127.0.0.1/32            md5
- IPv6 local connections:
host    all             all             ::1/128                 md5

------------------------------
| Postgres user and db setup |
------------------------------
$ createuser testuser -d -e -P

$ createdb scrapeDB -U testuser -W

---------------
| Preparation |
---------------
You should firstly execute the python script being responsible for creating
the Dmoz table. Simply run:

$ python dbscripts/prepare_db.py

-------------
| Execution |
-------------
$ scrapy crawl dmoz 

-----------
| Results |
-----------
The outcome of the above command can be found in the postgres Dmoz
table.

Connect to the database:

$ psql -d scrapeDB -U testuser -W 

You can check the result by following a simple SQL query like:

$ SELECT * FROM Dmoz;

-----------
| Cleanup |
----------
Execute the following command for dropping the Dmoz table:

$ python dbscript/destroy_db.py

