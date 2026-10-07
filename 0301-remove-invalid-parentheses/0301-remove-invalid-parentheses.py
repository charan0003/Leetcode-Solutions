class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            balance = 0

            for c in s:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}

        while queue:
            ans = []

            for _ in range(len(queue)):
                current = queue.popleft()

                if isValid(current):
                    ans.append(current)
                    continue

                for i in range(len(current)):
                    if current[i] not in "()":
                        continue

                    new_s = current[:i] + current[i + 1:]

                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)

            if ans:
                return ans

        return [""]