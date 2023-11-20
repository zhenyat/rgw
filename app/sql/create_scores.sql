--------------------------------------------------------------
--  Creates table Scores                                    --
--                                                          --
--    id                - Primary key                       --
--    respondent_id     - Foreign key                       --
--    v0                - Raw score value                   --
--    v1 ... v8         - Std Score values for Scales 1...8 --
--                                                          --
--  20.11.2023  Rada Telyukova                              --
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Scores (
  id INTEGER PRIMARY KEY,
  respondent_id INTEGER,
  v0 INTEGER NOT NULL,
  v1 INTEGER NOT NULL,
  v2 INTEGER NOT NULL,
  v3 INTEGER NOT NULL,
  v4 INTEGER NOT NULL,
  v5 INTEGER NOT NULL,
  v6 INTEGER NOT NULL,
  v7 INTEGER NOT NULL,
  v8 INTEGER NOT NULL,
  FOREIGN KEY(respondent_id) REFERENCES Respondents(id) ON DELETE CASCADE
);        

.print "\nTable 'Scores' has been created with schema:"
.schema Scores
