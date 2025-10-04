class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)  #counting frequency of each number

        arr = []
        
        #converting dictionary into lists
        for num, cnt in count.items():
            arr.append([cnt,num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])  #Here poping the actual number not the count
        return res

        

