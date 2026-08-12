class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #there are 26 chars as all are in lowercase 
        #now we've to calculate frequency of each char/letter
        result = defaultdict(list)
        for word in strs:
            hashMap = [0] * 26
            for s in word:
                hashMap[ord(s) - ord('a')] += 1
            result[tuple(hashMap)].append(word)
        return list(result.values())        

        