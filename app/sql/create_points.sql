--------------------------------------------------------------------------------
--  Creates table 'Points'                                                    --
--    Includes:                                                               --
--        original points                                                     --
--        standard (Wassermanet et al.) points for age 'under 20'             --
--     https://psylab.info/Опросник_«Способы_совладающего_поведения»_Лазаруса --
--                                                                            --
--    id              - Primary key                                           --
--    scale_id        - Foreign key                                           --
--    original_points - Original values                                       --
--    male_points     - Standard values for males                             --
--    female_points   - Standard values for females                           --
--                                                                            --
--  16.11.2023  Rada Telyukova                                                --
--------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Points (
  id INTEGER PRIMARY KEY,
  scale_id INTEGER,
  original_points INTEGER NOT NULL,
  male_points INTEGER NOT NULL,
  female_points INTEGER NOT NULL,
  FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
);

.print "\nTable 'Points' has been created with schema:"
.schema Points
