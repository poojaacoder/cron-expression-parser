# Cron Expression Parser

1. A simple cron expression parser written in python that translates cron expression and send output in table format.

2. validates cron expression and able to handle errors. 

2. Handles setp values(`/`), range values(`-`) and comma(`,`) separated values.

3. It accepts string input which has following  five paramters 
- minute
- hour
- day of month
- month
- day of week
- command


## Steps to create and upload pypi package 

- create project 
- create setup.py
- run ` python3 setup.py sdist bdist_wheel`
- it will create dist folder in ur code folder incusing wheel files
- register and create account on pypi library
- run `twine upload dist/*`


## System Requirements

- Python >=3.12
- `pipenv` 

## Steps to use

follow these steps, to use this program:

1. Open a terminal or command prompt in the root folder.

2. Install all dependencies and active the virtual environment:
   ```shell
   pip3 install pipenv
   pipenv install
   pipenv install -r requirements.txt
   pipenv shell
   pipenv install pytest
   ```

3. Install the package as a binary name `cron-parser`.
   ```shell
   pip3 install --editable .
   ```

4. Run the program with a cron expression as an argument. For example:

   ```shell
   cron-parser "<expression>"
   ```

   expression should be including minutes, hours, day of month, months, day of week and command

   Example :  `"*/10 0 2,12 * 2-6 /usr/bin/find"`

5. The program will output the formatted cron expression as a table, like this:

   ```
   minute        0 10 20 30 40 50
   hour          0
   day of month  2 12
   month         1 2 3 4 5 6 7 8 9 10 11 12
   day of week   2 3 4 5 6
   command       /usr/bin/find
   ```

7. To run the tests , run following command:
   ```shell
   pytest
   ```

* * * * * /usr/bin/find -v foo
