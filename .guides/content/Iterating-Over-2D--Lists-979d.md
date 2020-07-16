----------

## Iterating with Indices

Using a traditional for loop to iterate over a 2D list works, but it does not allow access to all of the information stored in the 2D list. Below is a list of the tallest mountains in Asia, North American, and Africa. Assume you want to print its name if the mountain has six or fewer characters. Those mountains would be K2 and Denali.

```python
mountains = [
              ["Mount Everest", "K2", "Kangchenjunga"],
              ["Denali", "Mount Logan", "Pico de Orizaba"],
              ["Mount Kilimanjaro", "Mount Kenya", "Mount Ngaliema"]
            ]

for mountain in mountains:
  if len(mountain) <= 6:
    print(mountain)
```
[Code Visualizer](open_tutor code/lists/iterating_2d_list.py)

{try it}(python3 code/lists/iterating_2d_list.py 1)

The code above did not produce the desired result. That is because the for loop only looked at each of the three lists. It **did not** look inside each list. So the line of code `len(mountain)` was not calculating the length of each individual mountain. Instead it was calculating the length of each list of mountains. Since each list has three elements, all of the lists were printed.

To access each of the elements inside the inner lists, you need to use a nested loop.

```python
mountains = [
              ["Mount Everest", "K2", "Kangchenjunga"],
              ["Denali", "Mount Logan", "Pico de Orizaba"],
              ["Mount Kilimanjaro", "Mount Kenya", "Mount Ngaliema"]
            ]

for row in range(3):
  for column in range(3):
    if len(mountains[row][column]) <= 6:
      print(mountains[row][column])
```
[Code Visualizer](open_tutor code/lists/iterating_2d_list.py)

{try it}(python3 code/lists/iterating_2d_list.py 2)

The results of the program match our expectations. This is because the outer loop (`row`) indicates each list of mountains, while the inner loop (`column`) indicates each mountain in its list.

![Iterating Over a 2D List](.guides/images/2d_iterating.png)

|||challenge
## Try this variation:
Use the following 2D list to help you solve the coding problem below.

```python
numbers = [
            [11, 13, 22, 76, 54],
            [2, 65, 107, 112, 8],
            [33, 90, 34, 7, 804]
          ]
```

Iterate over the list `numbers` and for every element print `even` if it is an even number or print `odd` if it is an odd number.
<details><summary>**Solution**</summary><img src=".guides/images/2d_iterate_solution.png" /></details>

|||
[Code Visualizer](open_tutor code/lists/iterating_2d_list.py)

{try it}(python3 code/lists/iterating_2d_list.py 3)

## Iterating without Indices

The examples above show how to use a nested loop with indices to iterate over a 2D list. We saw in an earlier section how to iterate over a traditional list in a more pythonic way. The following code snippet iterates over the list `numbers` and prints each element. No indices (`number[1]`) were used.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
  print(number)
```

<details><summary>**What does pythonic mean?**</summary>Pythonic means using the features of the Python language to make your code simple, concise, and easy to read. In this case, use the pattern "for element in sequence" instead of the list name and an index.</details>

This same idea can be used on a 2D list. The code below uses the mountain example but without any indices. This code is a bit easier to read since `mountain` replaces `mountains[row][column]`.

```python
mountains = [
              ["Mount Everest", "K2", "Kangchenjunga"],
              ["Denali", "Mount Logan", "Pico de Orizaba"],
              ["Mount Kilimanjaro", "Mount Kenya", "Mount Ngaliema"]
            ]

for row in mountains:
  for mountain in row:
    if len(mountain) <= 6:
      print(mountain) 
```
[Code Visualizer](open_tutor code/lists/iterating_2d_list.py)

{try it}(python3 code/lists/iterating_2d_list.py 4)

|||challenge
## Try this variation:
Use the following 2D list to help you solve the coding problem below.

```python
numbers = [
            [11, 13, 22, 76, 54],
            [2, 65, 107, 112, 8],
            [33, 90, 34, 7, 804]
          ]
```

Iterate over the list `numbers` and for every element print `even` if it is an even number or print `odd` if it is an odd number. Write you loop such that no indices are needed.
<details><summary>**Solution**</summary><img src=".guides/images/pythonic_2d_iterate_solution.png" /></details>


|||
[Code Visualizer](open_tutor code/lists/iterating_2d_list.py)

{try it}(python3 code/lists/iterating_2d_list.py 5)

{Check It!|assessment}(multiple-choice-1034788956)

