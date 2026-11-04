
import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        small = []
        large = []
        delayed = {}

        small_size = large_size = 0
        small_sum = large_sum = 0

        def prune(heap, is_small):
            while heap:
                val = -heap[0] if is_small else heap[0]

                if delayed.get(val, 0) == 0:
                    break

                heapq.heappop(heap)
                delayed[val] -= 1

        def rebalance():
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            prune(small, True)
            prune(large, False)

            while small_size > large_size + 1:
                val = -heapq.heappop(small)
                small_size -= 1
                small_sum -= val

                heapq.heappush(large, val)
                large_size += 1
                large_sum += val

                prune(small, True)

            while small_size < large_size:
                val = heapq.heappop(large)
                large_size -= 1
                large_sum -= val

                heapq.heappush(small, -val)
                small_size += 1
                small_sum += val

                prune(large, False)

        def add(num):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            prune(small, True)

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
                small_sum += num
            else:
                heapq.heappush(large, num)
                large_size += 1
                large_sum += num

            rebalance()

        def remove(num):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            prune(small, True)
            prune(large, False)

            delayed[num] = delayed.get(num, 0) + 1

            if num <= -small[0]:
                small_size -= 1
                small_sum -= num

                if -small[0] == num:
                    prune(small, True)
            else:
                large_size -= 1
                large_sum -= num

                if large and large[0] == num:
                    prune(large, False)

            rebalance()

        def get_cost():
            median = -small[0]

            return (
                median * small_size - small_sum
                + large_sum - median * large_size
            )

        costs = []
        total = 0

        for i in range(x):
            add(nums[i])

        for i in range(len(nums) - x + 1):
            costs.append(get_cost())

            if i + x < len(nums):
                remove(nums[i])
                add(nums[i + x])

        n = len(nums)
        INF = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
