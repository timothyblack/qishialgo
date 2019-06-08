"""
LC 544 Output Contest Matches
Time Complexity: O(Nlog N)   Space Complexity:  O(NlogN).
"""


class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """

    def findContestMatch(self, n):
        s = [str(num) for num in range(1, n + 1)]
        print(s)

        while n > 1:

            for i in range(n // 2):
                #  print(i)
                #  print("(" + s[i] + "," + s[n - i - 1] + ")")
                s[i] = "(" + s[i] + "," + s[n - i - 1] + ")"
                # print(s)
            n = n // 2
        return s[0]

