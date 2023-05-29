class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        chainTam = 1
        lastChainPair = pairs[0]
        for i in range(1,len(pairs)):
            if lastChainPair[1] < pairs[i][0]:
                lastChainPair = pairs[i]
                chainTam += 1
        return chainTam