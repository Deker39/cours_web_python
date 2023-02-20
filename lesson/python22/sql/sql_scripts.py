CREATE_DB = "CREATE DATABASE IF NOT EXISTS`p22`;"
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
# COUNT, AVG, SUM, MIN, MAX
SELECT_FROM_AND_COUNT = 'select COUNT(DISTINCT {}) as counts from {};'
SELECT_FROM_AND_AVG = 'select AVG({}) as counts from {};'
SELECT_FROM_AND_SUM = 'select SUM({}) as counts from {};'
SELECT_FROM_AND_MIN = 'select MIN({}) as counts from {};'
SELECT_FROM_AND_MAX = 'select MAX({}) as counts from {};'
SELECT_FROM_AND_MAX_AND_MIN = 'select MAX({}), MIN({}) counts from {};'
# GROUP BY, HAVING
SELECT_FROM_GROUP_BY = 'select count({}), {} from {} group by {};'
SELECT_FROM_GROUP_BY_HAVING = 'select count({}), {} from {} group by {} having count({}) >= 2;'
# JOIN
SELECT_FROM_TOP_BY_LIMIT = 'select `title`, avg(`rating`) as avg_rating from rating inner join movie ' \
                           'on movie.id = rating.movie_id group by movie_id ' \
                           'order by avg_rating desc  limit 5;'
# EXISTS, ALL, ANY/SOME
SELECT_FROM_WHERE_WITHOUT_EXIST = 'select `first_name` from `reviewer`, `rating` where rating.reviewer_id = reviewer.id'
SELECT_FROM_WHERE_EXISTS = 'select `first_name` from `reviewer` where ' \
                           'exists(select * from rating where rating.reviewer_id = reviewer.id)'
SELECT_FROM_WHERE_ANY = 'select `first_name` from `reviewer` where reviewer.id = ' \
                           'any(select `reviewer_id` from rating where rating.reviewer_id = reviewer.id)'
SELECT_FROM_WHERE_ALL = 'select * from reviewer, rating where reviewer.id = rating.reviewer_id and ' \
                         'rating.rating > all(select avg(`rating`) from rating)'


