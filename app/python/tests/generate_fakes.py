#! /usr/bin/env python3

####################################################
#   Generates faked data for testing & debugging
#
#   18.11.2023  Rada Telyukova
####################################################
# import schools
# import scales
# import questionnaire
import wasserman
# import respondents
# import responses

def main():
    db_production = 'db/rgw.sqlite3'
    db_test = 'db/rgw_test.sqlite3'

    # schools.create(db_test)
    # scales.create(db_test)
    # questionnaire.copy(db_production, db_test)
    wasserman.copy(db_production, db_test)
    # respondents.create(db_test)
    # responses.create(db_test)

if __name__ == '__main__':
    main()
