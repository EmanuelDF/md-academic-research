# Twitter Academic Research

Academic researchers with specific research objectives like NLP (Natural Language Processing) can retrieve information from Twitter.
Twitter API V2, Full-archive search, have a rate limit of 300 request in a 15 min window. 

### MySQL running on Docker 

```docker run -p 3306:3306 --name=mysql -d mysql/mysql-server:8.0.21
docker logs mysql 2>&1 | grep GENERATED
docker exec -it mysql mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'mysql';
update mysql.user set host = '%' where user='root';
docker restart mysql

SHOW DATABASES;
CREATE DATABASE <name_you_prefer>;
USE <name_you_prefer>;

jdbc:mysql://localhost:3306/<name_you_prefer>
```

### Prerequisites
- Bearer token on academic research level.
- Python 3 running with all packages from code installed.