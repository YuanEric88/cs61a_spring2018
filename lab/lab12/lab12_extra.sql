.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
  from students as a, fa17students as b
  where a.date = b.date and 
        a.color = b.color and
        a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven from students as a, checkboxes as b
  where a.time = b.time and 
        a.number = 7 and 
        b."7" = "True";

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, count(*) from fa17students 
  group by number
  order by count(*) desc limit 1;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*) FROM fa17students
  GROUP BY pet ORDER BY count(*) DESC
  LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, count(*) FROM students
  GROUP BY pet ORDER BY count(*) DESC
  LIMIT 10;

CREATE TABLE sp18dog AS
  SELECT pet, count(*) FROM students
  WHERE pet = "dog";


CREATE TABLE sp18alldogs AS
  SELECT pet, count(*) FROM students
  WHERE pet LIKE '%dog%';

CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*) From students
  WHERE seven = '7'
  Group BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*) FROM students
  GROUP BY smallest
  ORDER BY smallest;
