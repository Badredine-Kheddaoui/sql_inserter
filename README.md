# sql_inserter
This is a python script that generates random or custom insertions 
based on a provided wordlist to test your database.

Example of how to run it:

`python inserter.py client 5 
Id,number Name,varchar adresse,varchar,adresses.txt`

in the above example the script will generate five lines of insertions for a table
named 'client' that has three columns: 
an Id of type number
a name of type varchar
an adresse of type varchar

for the Id column the script will generate random numbers between 1236 and 9932 
for the name column the script will generate random words from the file randomWords.txt
for the adresse column the script will generate random lines from the file
adresses.txt provided by the user


Datatypes:
there are three datatypes supported: number, float and varchar

 


