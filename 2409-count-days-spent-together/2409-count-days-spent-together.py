class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_number(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        a1 = day_number(arriveAlice)
        a2 = day_number(leaveAlice)
        b1 = day_number(arriveBob)
        b2 = day_number(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)