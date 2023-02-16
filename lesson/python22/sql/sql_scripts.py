CREATE_DB = 'CREATE DATABASE IF NOT EXISTS`p22`;'
SHOW_DB = 'SHOW DATABASES;'
CREATE_TABLE_MOVIE = 'CREATE TABLE `movie` ( ' \
                     'id int auto_increment primary key,' \
                     'title varchar(255),' \
                     'release_year year,' \
                     'genre varchar(100)' \
                     ');'
CREATE_TABLE_REVIEWER = 'CREATE TABLE `reviewer` ( ' \
                     'id int auto_increment primary key,' \
                     'first_name varchar(255),' \
                     'last_name varchar(255)' \
                     ');'
CREATE_TABLE_RATING = 'CREATE TABLE `rating`(' \
                      'movie_id int,' \
                      ' reviewer_id int,' \
                      ' rating int,' \
                      ' foreign key(movie_id) references movie(id),' \
                      ' foreign key(reviewer_id) references reviewer(id),' \
                      ' primary key (movie_id, reviewer_id)' \
                      ');'
SHOW_TABLE_QUERY = 'DESCRIBE `{}`;'
INSERT_INTO_MOVIE = 'insert into `movie` (title, release_year, genre) values(%s, %s, %s);'
INSERT_INTO_REVIEWER = 'insert into `reviewer` (first_name, last_name) values(%s, %s);'
INSERT_INTO_RATING = 'insert into `rating` (movie_id, reviewer_id, rating) values(%s, %s, %s);'

SELECT_FROM_BY_LIMIT = 'select {} from {} limit {};'
