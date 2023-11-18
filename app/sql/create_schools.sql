-------------------------------------------------
--  Creates and populates table Schools        --
--                                             --
--    id      - Primary key                    --
--    nick    - short name for FK reference    --
--    title   - Full name of school            --
--                                             --
--  16.11.2023  Rada Telyukova                 --
-------------------------------------------------

CREATE TABLE IF NOT EXISTS Schools (
  id INTEGER PRIMARY KEY,
  nick TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL
);
.print "\nTable 'Schools' has been created with schema:"
.schema Schools

INSERT INTO Schools (nick, title)
VALUES 
  ('liceum', 'Лицей НИУ ВШЭ'),
  ('1570',   'ГБОУ Школа № 1570 г. Москвы');

.print "\nTable 'Schools' has been populated:"
.mode columns
.header on
SELECT * FROM Schools;
