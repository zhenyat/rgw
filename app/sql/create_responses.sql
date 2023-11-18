------------------------------------------
--  Creates table Responses             --
--                                      --
--    id                - Primary key   --
--    respondent_id     - Foreign key   --
--    questionnaire_id  - Foreign key   --
--    answer            - enumerated    --
--                                      --
--  16.11.2023  Rada Telyukova          --
------------------------------------------

CREATE TABLE IF NOT EXISTS Responses (
  id INTEGER PRIMARY KEY,
  respondent_id INTEGER,
  questionnaire_id INTEGER,
  answer TEXT CHECK(answer IN ('never', 'rarely', 'sometimes', 'regularly')) NOT NULL DEFAULT 'never',
  FOREIGN KEY(respondent_id) REFERENCES Respondents(id) ON DELETE CASCADE,
  FOREIGN KEY(questionnaire_id) REFERENCES Questionnaire(id) ON DELETE CASCADE
);        

.print "\nTable 'Responses' has been created with schema:"
.schema Responses
