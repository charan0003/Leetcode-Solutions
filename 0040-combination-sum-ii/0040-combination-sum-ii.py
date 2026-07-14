class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start_idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i]) 
                cur.pop()

        dfs(0, [], 0)
        return res
        