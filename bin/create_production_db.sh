#!/bin/zsh

########################################
#   Creates and populates production DB
#       Parameter $1 - DB filename
#########################################

if [ -f "$1" ]; 
then
    rm "$1"
fi

sqlite3 "$1" <<'END_SQL'
.read app/sql/create_schools.sql
.read app/sql/create_scales.sql
.read app/sql/create_questionnaire.sql
.read app/sql/create_respondents.sql
.read app/sql/create_responses.sql
.read app/sql/create_wasserman_u20.sql
END_SQL
app/python/populate_wasserman_u20.py
app/python/populate_survey_data.py