# sql_inserter
This is a python script that generates random or custom insertions 
based on a provided wordlist to test your database.

Example of how to run it:

`python inserter.py client 5 Id,number Name,varchar adresse,varchar,adresses.txt`

<br><br>
in the above example the script will generate five lines of insertions for a table named 'client' that has three columns: <br>
1 - an Id of type number<br>
2 - a name of type varchar<br>
3 - an adresse of type varchar
<br><br><br>

for the Id column the script will generate random numbers between 1236 and 9932 
for the name column the script will generate random words from the file randomWords.txt
for the adresse column the script will generate random lines from the file
adresses.txt provided by the user

Syntax:<br>
`inserter.py [-h] table_name number_of_rows column_name1,[column_data_type1,column_wordlist1] [column_name1,
[column_data_type1,column_wordlist1]]`

Datatypes:
there are three datatypes supported: number, float and varchar
if the datatype wasn't specified, it's varchar per default

 


