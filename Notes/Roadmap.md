# DSA Roadmap: Python + Rust (Feb 28, 2025 - Apr 25, 2025)

## Overview
- **Goal**: Master Data Structures and Algorithms (DSA) by solving 5 LeetCode problems daily, implementing each in both Python and Rust.
- **Background**: Comfortable with Python for DSA; no Rust syntax knowledge yet.
- **Strategy**: Solve in Python first (fast), then port to Rust (learning). Same 5 problems/day in both languages.
- **Duration**: 8 weeks, starting Feb 28, 2025.

## Goals
1. Build DSA fluency through Python repetition.
2. Learn Rust syntax by mirroring Python solutions.
3. Stay consistent with 5 problems/day to beat procrastination.

## Setup
- **Python**: Any editor (e.g., VS Code, PyCharm). Run with `python script.py`.
- **Rust**: 
  - Install via `rustup` (rust-lang.org).
  - Create project: `cargo new dsa_practice`.
  - Use VS Code + Rust extension.
  - Run with `cargo run`.

## Week-by-Week Plan

### Weeks 1-2: Rust Foundations + Easy DSA (Feb 28 - Mar 13)
- **Rust Learning (1-2 hours/day)**:
  - "The Rust Book" (Ch. 1-6): Variables, functions, ownership, borrowing, structs.
  - Practice: Translate small Python snippets (e.g., loops, conditionals) to Rust.
- **Daily Problems**: 5 problems, same in both languages.
  - **Focus**: Easy (arrays, strings, basic logic).
  - **Problems**:
    1. *Two Sum* (LeetCode #1) - Hash maps.
    2. *Reverse String* (LeetCode #344) - Iteration.
    3. *Contains Duplicate* (LeetCode #217) - Sets/maps.
    4. *Valid Anagram* (LeetCode #242) - Hashing.
    5. *Palindrome Number* (LeetCode #9) - Math.
- **Workflow**: Solve in Python first, then Rust. Google Rust syntax (e.g., `Vec`, `HashMap`) as needed.
- **Time**: 2-3 hours/day (Python ~15-20 min/problem, Rust ~30-40 min).

### Weeks 3-4: Core DSA + Rust Momentum (Mar 14 - Mar 27)
- **Rust Learning**:
  - "The Rust Book" (Ch. 7-10): Collections (`Vec`, `HashMap`), error handling.
  - Implement a linked list or stack in Rust.
- **Daily Problems**: 5 problems, same in both.
  - **Focus**: Easy + medium (stacks, queues, linked lists).
  - **Problems**:
    1. *Valid Parentheses* (LeetCode #20) - Stack.
    2. *Merge Two Sorted Lists* (LeetCode #21) - Linked lists.
    3. *Min Stack* (LeetCode #155) - Stack design.
    4. *Implement Queue using Stacks* (LeetCode #232) - Queue basics.
    5. *First Unique Character* (LeetCode #387) - Hashing.
- **Workflow**: Python first, then Rust. Note ownership differences.

### Weeks 5-6: Scaling Up (Mar 28 - Apr 10)
- **Rust Learning**: "Rust by Example" for DSA patterns (e.g., recursion, trees).
- **Daily Problems**: 5 problems, same in both.
  - **Focus**: Medium + intro to hard (trees, two pointers).
  - **Problems**:
    1. *Binary Tree Inorder Traversal* (LeetCode #94) - Trees.
    2. *Maximum Subarray* (LeetCode #53) - Arrays, Kadane’s.
    3. *Trapping Rain Water* (LeetCode #42) - Two pointers.
    4. *Reverse Linked List* (LeetCode #206) - Linked lists.
    5. *Group Anagrams* (LeetCode #49) - Hashing.
- **Workflow**: Python for speed, Rust to solidify. Rust time should drop.

### Weeks 7-8: Advanced DSA (Apr 11 - Apr 25)
- **Rust Learning**: Study LeetCode Rust solutions for elegance.
- **Daily Problems**: 5 problems, same in both.
  - **Focus**: Medium + hard (graphs, DP).
  - **Problems**:
    1. *Course Schedule* (LeetCode #207) - Graphs, DFS.
    2. *Longest Palindromic Substring* (LeetCode #5) - Strings, DP.
    3. *Word Break* (LeetCode #139) - DP.
    4. *Clone Graph* (LeetCode #133) - Graphs.
    5. *Top K Frequent Elements* (LeetCode #347) - Heap/hash.
- **Workflow**: Solve in either language first, then port. Rust should feel smooth.

## Tips
- **Time Management**: 3-4 hours/day total. Cap at 60 min/problem (check hints if stuck).
- **Syntax Bridge**:
  - Python `list` → Rust `Vec`.
  - Python `dict` → Rust `HashMap`.
  - Rust errors (e.g., "borrowed value") are normal—read them!
- **Tracking**: Log progress in a notebook/spreadsheet (e.g., "Day 1: 5/5").
- **Flexibility**: If 5 feels too much, drop to 3 and scale up.

## Day 1 Starter (Feb 28, 2025)
- **Problems**: *Two Sum*, *Reverse String*, *Contains Duplicate*, *Valid Anagram*, *Palindrome Number*.
- **Python Example (Two Sum)**:
  ```python
  def twoSum(nums, target):
      seen = {}
      for i, num in enumerate(nums):
          if target - num in seen:
              return [seen[target - num], i]
          seen[num] = i

