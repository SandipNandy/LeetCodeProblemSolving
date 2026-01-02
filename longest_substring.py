class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring in 's' without duplicate characters.

        The solution uses the Sliding Window pattern, which provides an efficient O(n)
        time complexity.

        Example 1:
            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

        Example 2:
            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

        Example 3:
            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
            0 <= s.length <= 5 * 10^4
            s consists of English letters, digits, symbols and spaces.

        Args:
            self: Required for a class method (instance method).
            s: The input string consisting of English letters, digits, symbols, and spaces.

        Returns:
            The length of the longest substring without repeating characters.
        """
        if not s:
            return 0

        # max_length: Stores the maximum length of a non-repeating substring found so far.
        max_length = 0
        
        # char_map: A dictionary (hash map) to store the last seen index of each character.
        # Key: character, Value: index in the string where it was last seen.
        char_map = {}
        
        # start: The starting index (left pointer) of the current sliding window.
        start = 0

        # Iterate through the string using 'end' as the right pointer of the window.
        for end in range(len(s)):
            char = s[end]

            # 1. Check for duplicate:
            # If the current character 'char' is already in the map AND 
            # its last seen index (char_map[char]) is within the current window (>= start),
            # we have found a repeating character.
            if char in char_map and char_map[char] >= start:
                # Move the start of the window immediately after the last occurrence of the duplicate.
                start = char_map[char] + 1

            # 2. Update the character map:
            # Store the current index of the character.
            char_map[char] = end

            # 3. Update max length:
            # The length of the current window is (end - start + 1).
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length

if __name__ == "__main__":
    # Instantiate the Solution class to access the method
    solver = Solution()
    
    print("--- Longest Substring Without Duplicate Characters Finder ---")
    
    # Get user input from the console
    user_input = input("Enter a string: ")
    
    # Calculate the result by calling the method on the solver instance
    result_length = solver.lengthOfLongestSubstring(user_input)
    
    # Display the result to the user
    print(f"\nInput String: \"{user_input}\"")
    print(f"Length of the longest substring without repeating characters: {result_length}")

    # Display standard examples
    print("\n--- Example Results ---")
    print(f"Input: 'abcabcbb', Output: {solver.lengthOfLongestSubstring('abcabcbb')}")
    print(f"Input: 'pwwkew', Output: {solver.lengthOfLongestSubstring('pwwkew')}")
    print(f"Input: 'bbbbb', Output: {solver.lengthOfLongestSubstring('bbbbb')}")    
    