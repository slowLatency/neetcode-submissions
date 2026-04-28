class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_map = defaultdict(list)

        for s in strs:
            ch_list = [0]*26
            for ch in s:
                ch_list[ord(ch) - ord('a')] += 1
            anagram_map[tuple(ch_list)].append(s)
        
        return list(anagram_map.values())