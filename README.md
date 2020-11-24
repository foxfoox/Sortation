# Sortation
 This class built by python3 for sort data which resulted from searching.

### SYNOPSIS

    Sortation( data , fulcrum, selection , priority)

### CONSTRAINTS
  - *Data* shall be a list of uniform sublists, all sublists shall compatible with each other in the list-length and data types of each element.
  - *Dulcrum* shall be a string or int data type.
  - *Selection* shall be a list of numbers, the length of the list shall be less than or equal to the list-length of the *data* lists, and every number is less than the list-length of data lists.
  - Priority shall be a boolean data type.
### FUNCTIONS
 #### sort()
  This function shall be utilized to obtaining the sortation.
 #### failed()
  This function shall be utilized to check  the entries validation.
 #### data()
  This function shall be utilized to bring the data whether the sortation is acted upon or not.
### EXAMPLE

```from Sortation import Sortation

sortation = Sortation([["Hello, World!",66,"Hello, Word!",93],
                       ["Hello, Wood!",2,"Holly, Wood",4],
                       ["Hell, food",23,"Hell,is good",2],
                       ["Hello, my World",55,"helly, this is world",45]],"Hello, World",[0,2])
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
[['Hello, World!', 66, 'Hello, Word!', 93], 
  ['Hello, Wood!', 2, 'Holly, Wood', 4], 
  ['Hello, my World', 55, 'helly, this is world', 45], 
  ['Hell, food', 23, 'Hell,is good', 2]]
