class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        arr=[]
        for cnt,num in count.items():
            arr.append([num,cnt])
        arr.sort()
        res=[]
        while len(res)<k:

            res.append(arr.pop()[1])
        return res
