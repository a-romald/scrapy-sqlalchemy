Scrapy project with images loading and mysql store with ORM SQLAlchemy.

Features

    Scrapy spider that crawles site, loads images and stores data in mysql database. 
    Requires Python 2.7    

Init project:

Install scrapy in Linux (Ubuntu):

    sudo pip install scrapy

Install SQLAlchemy:

    sudo pip install sqlalchemy

Install Scrapy-fake-useragent

    sudo pip install scrapy-fake-useragent

Create database in Mysql:

    CREATE DATABASE scrapy;

Create table `books` in mysql from scrapy.sql


Run spider and store data in json and mysql:

    scrapy crawl books -o books.json -s CLOSESPIDER_PAGECOUNT=5
