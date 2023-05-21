class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        freq = [[] for _ in range(len(words)+1)]
        ans=[]
        for word in words:
            d[word] = 1 + d.get(word,0)
        for word,count in d.items():
            freq[count].append(word)
        for words_lst in range(len(freq)-1,0,-1):
            freq[words_lst] = sorted(freq[words_lst])
            for words in freq[words_lst]:
                ans.append(words)
                if len(ans) == k:
                    return ans
                else:
                    continue
