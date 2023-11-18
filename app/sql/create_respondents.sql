------------------------------------------------
-- Creates table Respondents                  --
--                                            --
--    id          - Primary key               --
--    school_id   - Foreign key               --
--    email                                   --
--    sex         - enumerated  {'F' | 'M'}   --
--    age                                     --
--    form        - enumerated  {9 | 11}      --
--                                            --
--  17.11.2023  Rada Telyukova                --
------------------------------------------------
CREATE TABLE IF NOT EXISTS Respondents (
  id INTEGER PRIMARY KEY,
  school_id INTEGER,
  email TEXT UNIQUE,
  sex TEXT CHECK(sex IN ('F', 'M')) NOT NULL DEFAULT 'F',
  age INTEGER NOT NULL DEFAULT 15,
  form INTEGER CHECK(form IN (9, 11)) NOT NULL DEFAULT 9,
  FOREIGN KEY(school_id) REFERENCES Schools(id) ON DELETE CASCADE
);
.print "\nTable 'Respondents' has been created with schema:"
.schema Respondents
