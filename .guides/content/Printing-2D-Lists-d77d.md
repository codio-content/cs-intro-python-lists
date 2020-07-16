----------

## Printing a 2D List

You previously saw how a single `print` statement can print a 2D list. For smaller lists, this works alright. As the 2D list grows in length and complexity, printing a 2D list on a single line becomes harder to read.

```python
import random

numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
print(numbers)
```
<details><summary>**What is going on with the variable `numbers`?**</summary>The variable `numbers` is declared using something called a list comprehension. A list comprehension is a very concise (some would say difficult to understand) way of creating a list. `numbers` is a 2D list with ten columns and ten rows. Each element is a random integer between 1 and 100. Every time you run the code, the 2D list will be populated with different numbers.</details>

{try it}(python3 code/lists/printing_2d_list.py 1)

One way to increase readability is to use a single for loop and print each inner list.

```python
import random

numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
for row in numbers:
  print(row)
```
{try it}(python3 code/lists/printing_2d_list.py 2)

|||challenge
## Try this variation:
Rewrite the following code such that each inner list is printed on its own line.

```python
symbols = [["*" for columns in range(5)] for rows in range(7)]
print(symbols)
```
<details><summary>**Solution**</summary><img src=".guides/images/print_2d_solution_1.png" /></details>

|||

{try it}(python3 code/lists/printing_2d_list.py 3)

## Printing Just the Data

Using a single for loop to print each inner list on its own line helps with readability. However, you still see the square brackets and commas. Using a nested loop can remove these extra symbols.

```python
import random

numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
for row in numbers:
  for number in row:
    print(f"{number} ", end="")
  print()
```

{try it}(python3 code/lists/printing_2d_list.py 4)

![Just the Data](.guides/images/just_the_data.png)

|||challenge
## Try this variation:
Rewrite the following code such that each inner list is printed on its own line and there are no square brackets or commas.

```python
symbols = [["*" for columns in range(5)] for rows in range(7)]
print(symbols)
```
<details><summary>**Solution**</summary><img src=".guides/images/print_2d_solution_2.png" /></details>

|||

{try it}(python3 code/lists/printing_2d_list.py 4)

## Formatting the Data

The output can be refined a further step by making the spacing between the numbers more consistent. There is a space between each number, but when a number can be one, two, or three digits the overall alignment does not look that good. Instead of printing a space between each number, print a tab (this requires the escape character (`\t`).

```python
import random

numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
for row in numbers:
  for number in row:
    print(f"{number}\t", end="")
  print()
```

{try it}(python3 code/lists/printing_2d_list.py 5)

{Check It!|assessment}(fill-in-the-blanks-3273804598)

