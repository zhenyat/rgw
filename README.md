# Project RGW

## IDE
* OS:     macOS
* DB:     SQLite3
* Editor: VS Code

#### DB GUI:
  - DB Browser for SQLite
  - Valentina Studio
  - DBeaver
  
## Commands to create and populate DB:
```sh
  % rm db/rgw.sqlite3
  % sqlite3 db/rgw.sqlite3
    > .read app/sql/create_schools.sql
    > .read app/sql/create_scales.sql
    > .read app/sql/create_questionnaire.sql
    > .read app/sql/create_respondents.sql
    > .read app/sql/create_responses.sql
    > .read app/sql/create_wasserman_u20.sql
  % app/python/populate_wasserman_u20.py 
  % app/python/populate_survey_data.py 
  % app/python/tests/generate_fakes.py
```

## backup / dump
```
  % sqlite3 db/rgw.sqlite3 .dump > db/sql/rgw_dump.sql
```
