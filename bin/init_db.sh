#!/usr/bin/env zsh

####################################
#   Shell procedure to initiate DB
#################################### 
#!/bin/zsh

########################################
#   Initiates DB (production or test)
#       Parameter $1 - {production | test}}
########################################
set +xv

if [ -z "$1" ]; 
then 
    echo "command format: bin/init_db.sh {production | test}"
else
    if [ "$1" = "test" ]; 
    then
        bin/create_test_db.sh 'db/rgw_test.sqlite3'

    elif  [ "$1" = "production" ]; then
        bin/create_production_db.sh 'db/rgw.sqlite3'

    else
        echo "Parameter must be either 'test' or 'production'"
        exit()
    fi
fi
