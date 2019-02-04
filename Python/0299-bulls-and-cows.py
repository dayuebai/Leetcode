# Time: O(N)
# Space: O(1)
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        size = len(guess)
        bull, cow = 0, 0
        tracker = [0 for i in range(10)]

        for i in range(size):
            if guess[i] == secret[i]:
                bull += 1
            else:
                s = int(secret[i])
                g = int(guess[i])
                if tracker[s] < 0:
                    cow += 1
                if tracker[g] > 0:
                    cow += 1
                tracker[s] += 1
                tracker[g] -= 1

        return str(bull) + "A" + str(cow) + "B"
