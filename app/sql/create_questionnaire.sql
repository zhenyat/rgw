----------------------------------------------------------------------
--  Creates table Questionnaire and populates it with CSV file data  --
--                                                                  --
--    id        - Primary key                                       --
--    scale_id  - Foreign key                                       --
--    item  - Text of Lazarus 'thoughts or behavior'                --
--                                                                  --
--  16.11.2023  Rada Telyukova                                      --
----------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Questionnaire (
  id INTEGER PRIMARY KEY,
  scale_id INTEGER,
  item TEXT NOT NULL UNIQUE,
  FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
);

.print "\nTable 'Questionnaire' has been created with schema:"
.schema Questionnaire

.mode csv
.import db/input/questionnaire.csv Questionnaire

.mode columns
.header on
.print "\nTable 'Questionnaire' has been populated"
.print "\nNumber of rows:"
SELECT count(*) FROM Questionnaire;
.print "\nFirst and last rows:"
SELECT * FROM Questionnaire WHERE (id=1 OR id=50);
