class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        answer = []

        for num, freq in sorted(
            count.items(), key = lambda x:x[1],
            reverse = True):
            
            answer.append(num)

            if len(answer) == k:
                break
        return answer