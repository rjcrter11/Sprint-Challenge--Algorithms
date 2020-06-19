#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    Runtime of a single loop is O(n). The runtime will scale linearly with the size of n


b)  O(n^2)
    Nested loop complexity is equal to the number of times the inner loop's statement is run(n^c). In this case twice for a single nesting.  


c)  O(n)
    Recursive functions are like loops. In this case, the function is being called n times before it hits its base case

## Exercise II

The strategy I would take is finding f through a binary search. Assuming the list is sorted, each pass, in choosing the middle value,  would eliminate half of the choices everytime. 

    - First and last index / 2 gives middle value
    - the two indices saved in variables move towards eachother on the 
    - given side of the list
    - basecase: when the last index  is == or < than the first
    - called recursively, subracting or adding to the needed index 
    - until the base case is reached.


Runtime complexity: O(log n)
