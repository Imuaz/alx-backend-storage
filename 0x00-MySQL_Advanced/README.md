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


