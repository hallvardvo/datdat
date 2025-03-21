# TDT4145 Project - Group 6

### Group Members:

* Hallvard Vatnar Olsen
* Erik Le Blanc Pleym
* Halvor Heien Førde

## Changes from first deliverable:

We realized that a few tweaks needed to be made to our initial ER-Model and structure of our database in order to fit the requirements.  

First, we needed to adjust how seating worked for different flight types due to te requirement of seat rows not always having the same number of seat, and for the option of mutliple emeregency exit rows.  

The second thing we made changes to was how flight tickets were handled due to some logical issues that occurred with our first rendition  

The new and improved model can be found in the attached .pdf file.

## Requirements:

In order to run the scripts and to view the sqlite file contents you need to have sqlite3 and python installed on your system.

## Generate base database:

Make sure your current directory is the one containing the fly.py script. Then run the following command to generate the base database:
```bash
python3 fly.py
```
You should now have a fly.sqlite file generated in your repository.


## Insert data into database:

In order to fill the database with the necessary data, run the following command:
```bash
python3 insert.py
```
fly.sqlite should now be filled with the required data from the task description.


## View database:

You should now have a fly.sqlite file generated in your repository filled with data from the insert.py script. In order to access this data, perform the following:  

If your .sqlite file has been generated in a different directory than the location of the .py scripts you need to navigate to this directory first from your terminal. When in the correct directory you can run this command to access the database:

```bash
sqlite3 fly.sqlite
```

From here you can run the command,
```bash
.help
```
to be prompted by all the optional commands. You can run these commands to confirm that your data has been added as it should:
```bash
.table
```
then
```bash
SELECT * FROM flyselskap;
```

If you're presented with relevant data your setup should be correct.

## SQL Queries:

Below are commands for testing the SQL queries described in task 5, 6 and 8. Make sure you are running the command from the directory where the .py scripts are located.  

Task 5:
```bash
python3 queries.py
```
  
Task 6:
```bash
python3 routes.py
```
  
Task 8:
```bash
python3 preview.py
```