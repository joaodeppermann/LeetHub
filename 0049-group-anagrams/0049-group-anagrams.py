class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            key_delimiter = ['#' + str(key[i]) for i in range(26)]
            anagrams[tuple(key_delimiter)].append(s)
            
        return anagrams.values()
    
    # Time complexity = O(m * n), where m = number of strings in the input list, and n = average length of the strings inside the list
    # Space complexity = O(m), where m is the number of strings 
        
        
        
        
        
        
        
        