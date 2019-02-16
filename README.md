# sql_inserter
This is a python script that generates random or custom insertions 
based on a provided wordlist to test your database.
<br/><br/><br/>
Example of how to use it:
      
    python inserter.py client 5 Id,number Name,varchar adresse,varchar,frenchNames.txt

in the above example the script will generate five lines of insertions for a table named 'client' that has three columns: <br>
-an Id of type number<br/>
-a name of type varchar<br/>
-an adresse of type varchar<br/>

    INSERT INTO client(Id, Name, adresse) VALUES(7705, 'disastrous', 'dubois');
    INSERT INTO client(Id, Name, adresse) VALUES(9875, 'adjustment', 'sartre');
    INSERT INTO client(Id, Name, adresse) VALUES(7046, 'bury', 'mullins');
    INSERT INTO client(Id, Name, adresse) VALUES(4560, 'grateful', 'fabian');
    INSERT INTO client(Id, Name, adresse) VALUES(3364, 'wrathful', 'bonhomme');

Syntax:
<br/>

    inserter.py [-h] table_name number_of_rows column_name1[,column_data_type1,column_wordlist1] [column_name2,[column_data_type2,column_wordlist2]]

Datatypes:
<br/>
there are three datatypes supported: number, float and varchar. If the datatype wasn't specified, it's varchar per default.<br/>
1 - number: generate a random number between 1236 and 9932 if no wordlist was specified.<br/>
2 - float: generate a random float between 1236 and 9932 if no wordlist was specified.<br/>
3 - varchar: get a random line from the randomWords.txt if no wordlist was specified.<br/>
<br/><br/>
Wordlists:
<br/>
you can specify the wordlist after specifying the column datatype, if no wordlist was specified and the datatype was varchar then the script will generate random lines from the randomWords.txt.

