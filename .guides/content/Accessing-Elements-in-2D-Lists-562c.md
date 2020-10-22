----------

## Accessing Elements in a 2D List

In a traditional list, square brackets and a number are used to denote a particular element. For example, `my_list[2]`. Python would return the third element in the list. The 2D list below has three color palettes (warm, cool, and neutral) in hexadecimal code. A visual representation of the colors can be found to the right of the 2D list.

![Color Palettes](.guides/images/hex_colors.png)

In a 2D list, `colors[2]` would return the third element in `colors` which is another list (the neutral color palette). 

```python
colors = [
            ["#de0c1c", "#fe2d2d", "#fb7830", "#fecf02", "#ffdd46"],
            ["#1db4d4", "#246fb4", "#100ab6", "#130976", "#110240"],
            ["#ebe9e7", "#c4bdb7", "#8a7b70", "#4f3928", "#3c2411"]
         ]
print(colors[2])
```
<details>
  <summary><strong>What is hexadecimal?</strong></summary>
  Hexadecimal is a way of representing numbers using a base of 16. The symbols "0 - 9" represent the values zero to nine, and the symbols "a - f" represent the values ten to fifteen. Hexadecimal is often used to denote colors on the web.
</details><br>

{try it}(python3 code/lists/accessing_elements_2d_lists.py 1)

|||challenge
## Try this variation:
* Print the first element (the warm color palette).
<details>
  <summary><strong>Solution</strong></summary>
  <pre><code>print(colors[0])</code></pre>
</details><br>

* Print the second element (the cool color palette).
<details><summary><strong>Solution</strong></summary>
  <pre><code>print(colors[1])</code></pre>
</details>

|||

{try it}(python3 code/lists/accessing_elements_2d_lists.py 2)

## Accessing a Color in a Specific Palette

To print a particular hexadecimal color from a particular color palette, you need to use two sets of square brackets. The first set references the color palette and the second set references the hexadecimal color. In the example below, you will see how `colors[0][1]` is resolved.

![Two Indexes](.guides/images/two_index.png)

```python
print(colors[0][1])
```

{try it}(python3 code/lists/accessing_elements_2d_lists.py 3)

|||challenge
## Try this variation:
* Print the hexadecimal color `#100ab6`.
<details>
  <summary><strong>Solution</strong></summary>
  <pre><code>print(colors[1][2])</code></pre>
</details><br>

* Print the hexadecimal color `#c4bdb7`.
<details>
  <summary><strong>Solution</strong></summary>
  <pre><code>print(colors[2][1])</code></pre>
</details><br>

* Print the hexadecimal color `#ffdd46`.
<details>
  <summary><strong>Solution</strong></summary>
  <pre><code>print(colors[0][4])</code></pre>
</details>

|||

{try it}(python3 code/lists/accessing_elements_2d_lists.py 4)

{Check It!|assessment}(parsons-puzzle-224390132)
