class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            answer.append(word1[i])
            answer.append(word2[j])
            i += 1
            j += 1
        answer.append(word1[i:])
        answer.append(word2[j:])
        return ''.join(answer)