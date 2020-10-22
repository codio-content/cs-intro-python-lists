----------

## List Repetition

You can use the repetition operator (`*`) to a list. This is similar to string repetition from the lesson on data types.

```python
list_1 = ["Hi!"]

print(list_1 * 4)
```

{try it}(python3 code/lists/list-repeat.py 1)

|||challenge
## What happens if you:
* Change the `print` statement to be `print(list_1 * 100)`?
* Change the `print` statement to be `print(list_1 * 0)`?
* Change the `print` statement to be `print(list_1 * -1)`?

|||

<details>
  <summary><strong>What does <code>[]</code> mean?</strong></summary>
  The <code>[]</code> is called an empty list. This is a list that has no elements. If you use the <code>*</code> operator and 0 or a negative integer on a list, it will produce an empty list.
</details><br>

{try it}(python3 code/lists/list-repeat.py 2)

{Check It!|assessment}(parsons-puzzle-592043842)

