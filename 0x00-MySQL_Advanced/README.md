# 0x00. MySQL advanced

**INTRODUCTION**

The project encompassed a range of MySQL database-related topics. It covered the creation of tables with constraints, optimizing query performance by adding indexes, and the implementation of stored procedures and functions in MySQL.
Additionally, it delved into the concepts and implementation of views and triggers in MySQL databases. This project provided a comprehensive understanding of these database management aspects and their practical applications.

## Resources:books:
***Read or watch:***
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Requirements:round_pushpin:
**General**
- All files will be executed on Ubuntu 18.04 LTS using `MySQL 5.7` (version 5.7.30)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT, WHERE…`)
- A mandatory [README.md](./README.md] file, at the root of the folder of the project.
- The length of files will be tested using `wc`

## More Info:information_source:

**Comments for the SQL file**
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Tasks:page_with_curl:
**0. We are all unique!**
- [0-uniq_users.sql](./0-uniq_users.sql): A script that creates a table `users` with these attributes:
  - `id`, integer, never null, auto increment and primary key
  - `email`, string (255 characters), never null and unique
  - `name`, string (255 characters)
  - If the table already exists, the script does not fail
  - the script can be executed on any database

**1. In and not out**
- [1-country_users.sql](./1-country_users.sql): A script that creates a table `users` with these attributes:
  - `id`, integer, never null, auto increment and primary key
  - `email`, string (255 characters), never null and unique
  - `name`, string (255 characters)
  - `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
  - If the table already exists, the script does not fail
  - the script can be executed on any database

**2. Best band ever!**
- [2-fans.sql](./2-fans.sql): A script that ranks country origins of bands, ordered by the number of (non-unique) fans
  - Column names must be: `origin` and `nb_fans`
  - the script can be executed on any database

**3. Old school band**
- [3-glam_rock.sql](./3-glam_rock.sql): A script that lists all bands with `Glam rock` as their main style, ranked by their longevity
  - Column names: `band_name` and `lifespan` (in years **until 2022** - it uses `2022` instead of `YEAR(CURDATE())`)
  - it usea attributes `formed` and `split` for computing the `lifespan`
  - the script can be executed on any database

**4. Buy buy buy**
- [4-store.sql](./4-store.sql): A script that creates a trigger that decreases the quantity of an item after adding a new order.

**5. Email validation to sent**
- [5-valid_email.sql](./5-valid_email.sql): A script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**6. Add bonus**
- [6-bonus.sql](./6-bonus.sql): A script that creates a stored procedure `AddBonus` that adds a new correction for a student.
  - It takes 3 inputs (in this order):
    - `user_id`, a `users.id` value (it is assume that `user_id` is linked to an existing `users`)
    - `project_name`, a new or already exists `projects` - if no projects.name found in the table, it creates it
    - `score`, the score value for the correction

**7. Average score**
- [7-average_score.sql](./7-average_score.sql): A script that creates a stored procedure that computes and stores the average score for a student. An average score can be a decimal
- It takes 1 input:
  - `user_id`, a `users.id` value (it is assume `user_id` is linked to an existing `users`)

**8. Optimize simple search**
- [8-index_my_names.sql](./8-index_my_names.sql): A script that creates an index on the table `names` and the first letter of `name`.
  - It indexes onnly the first letter of `name`.

**9. Optimize search and score**
- [9-index_name_score.sql](./9-index_name_score.sql): A script that creates an index on the table `names` and the first letter of `name` and the `score`.
  - It indexes only the first letter of `name` AND `score`.

**10. Safe divide**
- [10-div.sql](./10-div.sql): A script that creates a function that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
  - The function takes 2 arguments:
    - `a`, INT
    - `b`, INT
  - It returns `a / b` or 0 if `b == 0`

**11. No table for a meeting**
- [11-need_meeting.sql](./11-need_meeting.sql): A script that creates a view that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.
  - It returns all students name when:
    - They score are under (strict) to 80
    - **AND** no `last_meeting` date **OR** more than a month

**12. Average weighted score**
- [100-average_weighted_score.sql](./100-average_weighted_score.sql): A script that creates a stored procedure that computes and store the average weighted score for a student.
  - It takes 1 input:
    - `user_id`, a `users.id` value (it is assume `user_id` is linked to an existing `users`)
  - **Tips:**
    - [Calculate-Weighted-Average](https://www.wikihow.com/Calculate-Weighted-Average)
<<<<<<< HEAD
**
=======
**13. Average weighted score for all!**
- [101-average_weighted_score.sql](./101-average_weighted_score.sql): A script that creates a stored procedure that computes and store the average weighted score for all students.
  - It takes no input
  - **Tips:**
    - [Calculate-Weighted-Average](https://www.wikihow.com/Calculate-Weighted-Average)

:+1:
>>>>>>> de72e61 (Readme updated)
