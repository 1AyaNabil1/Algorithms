
# Binary Search

Welcome to the **Binary Search** section of the Algorithms repository! 🚀

## Overview

Binary Search is a classic algorithm used to efficiently locate a target value within a sorted array. This section includes:

- **Basic Binary Search**: Implementation and explanation of the fundamental binary search algorithm.
- **Variants and Optimizations**: Explore different variations and optimizations of the binary search algorithm.

## 📂 Files

- **`binary_search.py`**: The basic implementation of binary search.
- **`optimized_binary_search.py`**: Advanced techniques and optimizations for binary search.

## 📜 Usage

To use the binary search implementation, ensure you have a sorted list. Then, call the function with the target value to find its index.

```python
from binary_search import binary_search

arr = [1, 2, 3, 4, 5]
target = 3
index = binary_search(arr, target)
print(f"Index of {target} is {index}")
