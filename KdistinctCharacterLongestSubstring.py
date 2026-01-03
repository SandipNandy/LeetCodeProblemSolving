# Longest Substring with At Most K Distinct Characters
"""
 Problem: Longest Substring with At Most K Distinct Characters
Question:
Given a string s and an integer K, find the length of the longest substring T that contains at most K distinct characters.
Constraints:
1≤length of s≤5×10 
4
 
1≤K≤26 (Typically, K is constrained to a small, positive integer)
s consists of English letters, digits, symbols, and spaces.

Key Definition:
A substring is a contiguous sequence of characters within a string. The "distinct characters" in the substring T must be ≤K.

Test Cases
Example

Input s

Input K

Output

Explanation

Example 1

"eceba"

2

3

The longest substring with ≤2 distinct characters is "ece" (distinct chars: 'e', 'c').

Example 2

"ccaabbb"

3

7

The entire string "ccaabbb" is the longest substring, containing 'c', 'a', 'b' (3 distinct chars).

Example 3

"aaabbcceeeff"

2

5

The longest substrings are "aaabb" ('a', 'b') and "eeeff" ('e', 'f').

Example 4

"abc"

1

1

Any single character is the longest valid substring (e.g., "a", "b", "c").

Example 5

"abacccb"

3

7

The whole string is valid as it contains 'a', 'b', 'c' (3 distinct chars).

Example 6 (Edge Case)

"zyxw"

4

4

The longest substring is the whole string, which has 4 distinct characters, satisfying 4≤4.

Example 7 (Edge Case)

"abacacac"

1

1

The longest substring is any single character (e.g., "a" or "b").
"""







