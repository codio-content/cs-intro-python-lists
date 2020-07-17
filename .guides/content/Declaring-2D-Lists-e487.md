----------

## Declaring a 2D List

A 2D list is a list whose individual elements are other lists; sometimes referred to as a list of lists.

![2D List](.guides/images/2d_lists.png)

To declare a 2D list, start as normal with a pair of square brackets (`[]`). For each element, declare another list with more square brackets. Be sure to use commas when separating each internal list.

```python
my_2d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_2d_list)
```

{try it}(python3 code/lists/declare_2d_lists.py 1)

|||challenge
## Try this variation:
* Create a 2D list comprised of empty lists. Print this 2D list.
<details><summary>**Solution**</summary><img src=".guides/images/empty_2d_list.png" /></details>

|||

{try it}(python3 code/lists/declare_2d_lists.py 2)

## Declaring 2D Lists in a Human Readable Way

2D lists are useful for when you want a group of data where each group is itself a group of data. Imagine that you are going to list the three most populous cities for America, France, China, and India. Declaring the list as described above, would make for a long line of code. While Python will not have trouble understanding this line of code, some humans might. It is a good idea to write your code in a way that is easy for humans to read. This will make debugging your code easier. 

```python
populous_cities = [
                    ["USA", "New York City", "Los Angeles", "Chicago"],
                    ["France", "Paris", "Marseille", "Lyon"],
                    ["China", "Shanghai", "Beijing", "Chongqing"],
                    ["India", "Mumbai", "Delhi", "Bangalore"]
                  ]
print(populous_cities)
```

{try it}(python3 code/lists/declare_2d_lists.py 3)

<details><summary>**Printing a 2D list**</summary>The standard `print` statement does not print a 2D list in a human readable way. However, it is possible to print a 2D list in a more readable way. This will be covered on a later page.</details>

|||challenge
## Try this variation:
* Create a 2D list in a human readable way based on the information in the table below. Print the list when done.
### Popular Breeds
|Pet|Popular Breeds|
|:-:|:------------:|
|Dogs|Labrador Retriever, German Shepherd, Golden Retriever|
|Cats|Siamese, Persian, Maine Coon|
<details><summary>**Solution**</summary><img src=".guides/images/human_readable_2d_list.png" /></details>

|||

{try it}(python3 code/lists/declare_2d_lists.py 4)

{Check It!|assessment}(multiple-choice-1967016213)

