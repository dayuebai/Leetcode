# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
import math

class Solution:

	def shortestDistance(self, words, word1, word2):
		result = math.inf
		w1, w2 = -1, -1
		size = len(words)

		for i in range(size):
			word = words[i]
			if word == word1:
				w1 = i
			elif word == word2:
				w2 = i
			if w1 != -1 and w2 != -1:
				result = min(result, abs(w1 - w2))

		return result

# Test
sol = Solution()
assert(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") == 3)
assert(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1)