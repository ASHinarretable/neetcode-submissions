class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MapS = {}
        MapT = {}
        for c in s:
            #stroing val n its index
            MapS[c] = MapS.get(c,0) +1
        for b in t:
            #stroing val n its index
            MapT[b] = MapT.get(b,0) +1
        return MapS == MapT