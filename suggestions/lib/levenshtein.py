from __future__ import annotations


def min_edit_distance(word1: str, word2: str) -> int:
    """
    Calculates the edit distance between two words.
    More specifically, the number of operations (insert, replace, remove) 
    needed to convert word1 into word2.
    """

    word1_length = len(word1)
    word2_length = len(word2)

    # When any of the words are empty,
    # min required operations is
    # the length of the other word.
    if not word2 or not word1:
        return max(word1_length, word2_length)

    # Memoize previous operations
    dp = [[0 for i in range(word1_length + 1)] for j in range(2)]

    # Going from the first word to the second
    # one with max. edits.
    for i in range(0, word1_length + 1):
        dp[0][i] = i

    # Create the edit matrix
    for i in range(1, word2_length + 1):
        for j in range(word1_length + 1):
            if word1[j - 1] == word2[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                insert = dp[(i - 1) % 2][j]
                remove = dp[i % 2][j - 1]
                replace = dp[(i - 1) % 2][j - 1]
                dp[i % 2][j] = 1 + min(insert, remove, replace)

    # If the second word is of odd length
    # then the min. edit distance is in
    # the second row.
    return dp[word2_length % 2][word1_length]
