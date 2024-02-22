# 0x07. Rotate 2D Matrix (Algorithm | Python)

By Benard Ronoh

This project involves the creation of a Python function that rotates a 2D matrix 90 degrees clockwise.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` style (version 2.8.0)
- Importing any module is not allowed
- All modules and functions must be documented
- All files must be executable

## Tasks

### 0. Rotate 2D Matrix

Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

Here is an example of how the function works:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

```

When you run this code, the output will be:

```
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

```
