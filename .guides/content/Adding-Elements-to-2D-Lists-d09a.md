----------

## Adding Elements to a 2D List

A common task for lists is to add an element to a list. You can use the `+` operator to concatenate 2D lists. 

```python
list_1 = [[1, 2, 3], [4, 5, 6]]
list_2 = [[7, 8, 9], [10, 11, 12]]

print(list_1 + list_2)
```

{try it}(python3 code/lists/add_element_2d_list.py 1)

|||challenge
## Try this variation:
* Change the `print` statement to `print(list_2 + list_1)`
* Change the `print` statement to `print(list_2 + [[13, 14, 15]])`
* Change the `print` statement to `print(list_2 + [13, 14, 15])`
* Change the `print` statement to `print(list_2 + 13)`
<details><summary>**Concatenating `[[13, 14, 15]]`, `[13, 14, 15]`, and `13`**</summary>The output from these list concatenations might be a little cofusing. Here is what Python is doing:<ul>
  <li><strong>[[13]]</strong> - This is a 2D list with one element that also only has one element. So the final result is a list of two lists. The first has three elements, while the second only has one.</li>
  <li><strong>[13]</strong> - This is a traditional list with one element. So the final result is a list with two elements. The first element is a list with three elements, while the second element is the integer <code>13</code>. In Python, a 2D list can have elements that are lists as well as elements that are not lists.</li>
  <li><strong>13</strong> - This causes an error because the concatenation operator expects to join two lists together. It can join two 2D lists or a 2D list and a traditional list. It cannot join a list and a non-list.</li>
  </ul><br><p>You can think of the concatenation process as removing a set of square brackets from the data being concatenated. So a 2D list becomes a traditional list (<code>[[13, 14, 15]]</code> becomes <code>[13, 14, 15]</code>), and a traditional list becomes a sequence of new elements (<code>[13, 14, 15]</code> becomes <code>13, 14, 15</code>). However, there are no square brackets to remove when trying to concatenate a non-list, which is why there is an error.</p></details>

|||

{try it}(python3 code/lists/add_element_2d_list.py 2)

## The `append` Method

The `append` method can be used with 2D lists to add another element to a list.

```python
my_list = [["a", "b", "c"], ["d", "e", "f"]]
another_list = ["g", "h", "i"]

my_list.append(another_list)
print(my_list)
```

{try it}(python3 code/lists/add_element_2d_list.py 3)

|||challenge
## Try this variation:
* Change the `append` statement to `my_list.append("g")`
* Change the `append` statement to `my_list.append(["g", "h", "i"])`
* Change the `append` statement to `my_list.append([["g", "h", "i"]])`
<details><summary>**Appending `"g"`, `["g", "h", "i"]`, and `[["g", "h", "i"]]`**</summary>The output from the `append` method might be a little cofusing. Here is what Python is doing:<ul>
  <li><strong>"g"</strong> - This creates a 2D list with three elements. The first two elements are lists of strings, while the third element is the string <code>"g"</code>.</li>
  <li><strong>["g", "h", "i"]</strong> - This creates a 2D list with three elements. The first two elements are lists of strings, while the third element is a list with <code>"g"</code> as its only element.</li>
  <li><strong>[["g", "h", "i"]]</strong> - This creates a 2D list with three elements. The first two elements are lists of strings, while the third element is another 2D list with the list of <code>"g"</code> as its only element.</li>
  </ul><br><p>You can think of the <code>append</code> method as adding its parameter to the list. Passing <code>append</code> a string (<code>"g"</code>) will add the string as a new element. Passing <code>append</code> a list (<code>["g", "h", "i"]</code>) will add the list as a new element. Passing <code>append</code> a 2D list (<code>[["g", "h", "i"]]</code>) will add the 2D list as a new element.</p></details>

|||

{try it}(python3 code/lists/add_element_2d_list.py 4)

{Check It!|assessment}(parsons-puzzle-788207901)

