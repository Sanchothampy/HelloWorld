#User function Template for python3
class solution:
    def __init__(self):
        pass

    def reverseWords(self, S):
        words = S.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string

S = 'i like this program very much'
Solution = solution()
reversed_string = Solution.reverseWords(S)
print(reversed_string)
