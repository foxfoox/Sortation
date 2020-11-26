# Sortation
 This class built by python3 for sort data which resulted from searching.

### SYNOPSIS

    Sortation( data , fulcrum, selection , priority)

### CONSTRAINTS
  - *Data* shall be a list of uniform sublists, all sublists shall compatible with each other in the list-length and data types of each element.
  - *Dulcrum* shall be a string or int data type.
  - *Selection* shall be a list of numbers, the length of the list shall be less than or equal to the list-length of the *data* lists, and every number is less than the list-length of data lists.
### FUNCTIONS
 #### sort()
  This function shall be utilized to obtaining the sortation.
 #### failed()
  This function shall be utilized to check  the entries validation.
 #### data()
  This function shall be utilized to bring the data whether the sortation is acted upon or not.
### EXAMPLE

```
from Sortation import Sortation

sortation = Sortation([["Hello, World!",1,"Hello, Word!",5],
                       ["Hello, Wood!",2,"Holly, Wood",6],
                       ["Hell, food",3,"Hell,is good",7],
                       ["Hello, my World",4,"helly, this is world",8]],"Hello, World",[0,2],attribute = {"priority":False,"exact":False,"precise":False,"order":False})
if not sortation.failed():
    sortation.sort()
    data = sortation.data()
    data.reverse()
    print(data)
else:
    print("Failed")
```
**Output**
```
[['Hello, my World', 4, 'helly, this is world', 8], ['Hello, World!', 1, 'Hello, Word!', 5], ['Hello, Wood!', 2, 'Holly, Wood', 6], ['Hell, food', 3, 'Hell,is good', 7]]
