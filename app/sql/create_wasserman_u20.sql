---------------------------------------------------------------
--  Creates table 'Wasserman undser 20'                      --
--                                                           --
--    id            - Primary key                            --
--    scale_id      - Foreign key                            --
--    raw_points    - raw values                             --
--    male_points   - Standard point values for mails        --
--    female_points - Standard point values for females      --
--                                                           --
--  16.11.2023  Rada Telyukova                               --
---------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Wasserman_u20 (
  id INTEGER PRIMARY KEY,
  scale_id INTEGER,
  raw_points INTEGER NOT NULL,
  male_points INTEGER NOT NULL,
  female_points INTEGER NOT NULL,
  FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
);

.print "\nTable 'Wasserman_u20' has been created with schema:"
.schema Wasserman_u20
