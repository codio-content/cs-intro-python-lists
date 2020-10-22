----------

## Lists Exercise 5

**Problem**
Write a program that accepts a 2D list of zeros. Print the 2D list in rows and columns without the square brackets and commas. Moving diagonally from the top-left to the bottom right, replace each 0 with a 1. The IDE already declares the variable `number` and the 2D list `data`. Use `number` to represent the number of rows and columns, and `data` to represent the 2D list of zeros.

<details>
  <summary><strong>What does `sys.argv[1]` mean?</strong></summary>
  You are expected to iterate over a 2D list with a specific number of rows and columns. However, we do not want you to know what that number is. Using <code>sys.argv[1]</code> allows us to send your program a "hidden" number. That number is the used to make a 2D list of zeros. Your code will be tested three times, each time with a different number of rows and columns.
</details><br>

**Expected Output**
<table>
  <tr>
    <th><center>Input</center></th>
    <th><center>Output</center></th>
  </tr>
  <tr>
    <td>
      <pre>
        <code>
          [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
          ]
        </code>
      </pre>
    </td>
    <td>
      <pre>
        1 0 0
        0 1 0
        0 0 1
      </pre>
    </td>  
  </tr>
  <tr>
    <td>
      <pre>
        <code>
          [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
          ]
        </code>
      </pre>
    </td>
    <td>
      <pre>
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1
      </pre>
    </td>  
  </tr>
</table>

**Important**
Do not edit the code in the top section. This code is necessary for the auto-grader to work. Add your code in the section below.

**Testing Your Code**
The `TEST 1` button will test your code with three rows. The `TEST 2` button will test your code with four rows.

{test 1}(python3 code/lists/2d_exercise.py 3)
{test 2}(python3 code/lists/2d_exercise.py 4)

<details>
  <summary><strong>Where is the code visualizer?</strong></summary>
  Unfortunately, the code visualizer does not work with the statement <code>import sys</code>. Since importing the <code>sys</code> module is required for this problem, the code visualizer will not be available for this problem.
</details><br>

{Check It!|assessment}(code-output-compare-3411556562)

