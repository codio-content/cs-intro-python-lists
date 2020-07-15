----------

## Manipulating 2D Lists with Methods

This page is not about one particular method used with a 2D list. Instead, this page is about how 2D list **do not** respond to methods the same way traditional lists do. Look at the 2D list `numbers` below. It contains all numbers from 1 to 20. There are four inner lists with five numbers each. Pay attention to how Python sorts `numbers`.

```python
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]
numbers.sort()
# loop to print the 2D list
for row in numbers:
  print(row)
```

{try it}(python3 code/lists/manipulate_2d_list.py 1)

Python sorted `numbers` based on the inner lists, but it did not sort the inner lists themselves. In order to use list methods or function on the inner lists, use a for loop.

```python
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]
numbers.sort()
# loop to sort and print the 2D list
for row in numbers:
  row.sort()
  print(row)
```

{try it}(python3 code/lists/manipulate_2d_list.py 2)

|||challenge
## Try this variation:
* Comment out the first `numbers.sort()` and run the program
```python
# numbers.sort()
# loop to sort and print the 2D list
for row in numbers:
  row.sort()
  print(row)
```
<details><summary>**Why are the lists out of order?**</summary>The first `sort` method sorts the four inner lists, while the second `sort` method sorts the inner lists themselves. Since the first `sort` method has been commented out, the elements of each inner list are in order, the but lists themselves are not in order.</details>

|||

{try it}(python3 code/lists/manipulate_2d_list.py 3)

## Manipulating a 2D Lists of Numbers

The 2D list `numbers` is a list of lists of numbers. Which means `sum(numbers)` would return an error because the `sum` function expects a list of numbers. To use `sum`, `max` or `min` you need to use a for loop.

```python
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]

# loop to print the sum of each inner list
for row in numbers:
  print(sum(row))
```

{try it}(python3 code/lists/manipulate_2d_list.py 4)

Notice, however, that this does not print the sum of all four inner lists. Instead is prints the sum of each individual list. To find the total of all of the lists, declare the `total` with an initial value of 0. Add the sum of each inner list to `total`. Then print `total`

```python
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]
total = 0

# loop to add the sum of each inner list to total
for row in numbers:
  total += sum(row)
print(total)
```

{try it}(python3 code/lists/manipulate_2d_list.py 5)

|||challenge
## Try this variation:
* Use the variable `numbers` and write a program that finds the largest number in the 2D list. **Hint:** use the `max` function.
```python
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]
```
<details><summary>**Solution**</summary><img src=".guides/images/manipulating_solution.png" /></details>

|||

{try it}(python3 code/lists/manipulate_2d_list.py 6)

{Check It!|assessment}(multiple-choice-4263263146)

