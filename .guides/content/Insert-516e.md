----------

## The Insert Method

The `insert` method allows you to add any object to an array. This method has two parameters, the index of the insertion and object to be inserted. The order is also import. The index should come first, the object second.

![List Insert](.guides/images/list-insert.png)

<details>
  <summary><strong><code>append</code> versus <code>insert</code></strong></summary>
  The <code>append</code> method will always add the object to the <strong>end</strong> of the list. The <code>insert</code> method gives you the ability to use <strong>any index</strong> you want.
</details>

```python
my_list = [1, 2, 3, 4]
my_list.insert(2, "Hi")
print(my_list)
```

{try it}(python3 code/lists/list-insert.py 1)

|||challenge
## What happens if you:
* Change `insert` to `my_list.insert(3, "Hi")`?
* Change `insert` to `my_list.insert(4, "Hi")`?
* Change `insert` to `my_list.insert("Hi", 1)`?
* Change `insert` to `my_list.insert("Hi")`?

|||

{try it}(python3 code/lists/list-insert.py 2)

{Check It!|assessment}(fill-in-the-blanks-3805979875)

