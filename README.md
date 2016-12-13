# Binary Plateau Task

## USAGE

```
python3 bynaryp.py < input.txt
```

Or:

```
>>> from bynaryp import solution
>>> solution(125)
5
```

## Input

* positive N integer
* within the range [1 .. 2,147,483,647].

## Logic

Example: number 14 has binary representation 1110 and contains a binary plateau of length 3. The number 758 has binary representation 1011110110 and contains two binary plateaus: one of length 4 and one of length 2.

## Output

* Longest plateau
* 0 if no binary plateau

## Complexity

* O(log(N))
* O(1) worst case
