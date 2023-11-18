--------------------------------------------------------------------------------
--  Creates table Scales and populates it with CSV file data                   --
--                                                                            --
--    id   - Primary key                                                      --
--    rus  - Name of the Scale in Russian                                     --
--    eng  - Name of the Scale in English                                     --
--                                                                            --
--    English terms:                                                          --
--    https://openpublichealthjournal.com/VOLUME/15/ELOCATOR/e187494452209210/FULLTEXT/
--                                                                            --
--  16.11.2023  Rada Telyukova                                                --
--------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Scales (
  id INTEGER PRIMARY KEY,
  rus TEXT NOT NULL UNIQUE,
  eng TEXT NOT NULL UNIQUE
);
.print "\nTable 'Scales' has been created with schema:"
.schema Scales

INSERT INTO Scales (rus, eng)
VALUES 
  ('Конфронтационный копинг', 'Confrontive coping'),
  ('Дистанцирование', 'Distancing'),
  ('Самоконтроль', 'Self-controlling'),
  ('Поиск социальной поддержки', 'Seeking social support'),
  ('Принятие ответственности', 'Accepting responsibility'),
  ('Бегство-избегание', 'Escape-avoidance'),
  ('Планирование решения проблемы', 'Planful problem solving'),
  ('Положительная переоценка', 'Positive reappraisal');

.mode columns
.header on
.print "\nTable 'Scales' has been populated:"
SELECT * FROM Scales;
