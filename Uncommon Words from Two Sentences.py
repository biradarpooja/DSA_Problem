class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]"""
    
 
        cnt = Counter(s1.split()) + Counter(s2.split())
        return [s for s, v in cnt.items() if v == 1
