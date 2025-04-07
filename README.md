#Lab test getDest program
By **nixkj** and **morisscofield**
Modified by **Jesse Schroder**-**2597626**
##Description
getbest.py is a program that takes in a file containing student's student numbers, marks, and comments and finds the student with the highest mark and outputs their student number and mark

An example of the contents of the file is such:

**Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-**

You are able to add new entries in the data with this format

##Tests

In `lt/test` is the tests and the input file.

`test_getbest_1.py` tests `getCols(f)`  with inpu data f and checks if the indexes of the studen number column and mark column are correct.

`test_getbest_2.py` tests `findTop(f, num_col, mark_col)` with input data f and checks if the returned student number and mark are correct.

f refers to `myData.csv` which is in the same directory as the tests and is only used to check whether the methods work.

In the `lt` directory running this line in command line will run the tests:

```
python3 -m unittest discover
``` 

## Using the program

In `lt/getbest_code` running this line in command line will rin the program:

```
python3 -m getbest.py bestDat0.csv 
```

with `bestDat0.csv` being in the same directory as getbest.py.

