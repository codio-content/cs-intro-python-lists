----------

## Lists Exercise 5

**Problem**
Write a program that accepts a 2D list of zeros. Print the 2D list in rows and columns without the square brackets and commas. Moving diagonally from the top-left to the bottom right, replace each 0 with a 1.

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
Do not alter the code in the top section of the IDE as this could negatively affect the auto-grader.

<details><summary>**Where is the code visualizer?**</summary>Unfortunately, the code visualizer does not work with the statement `import sys`. Since importing the `sys` module is required for this problem, the code visualizer will not be available for this problem.</details>
{test with 3 rows}(python3 code/lists/2d_exercise.py 3)
{test with 4 rows}(python3 code/lists/2d_exercise.py 4)

{Check It!|assessment}(code-output-compare-3411556562)

