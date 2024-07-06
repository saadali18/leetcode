class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # optimization
        if (n - 1) * 2 < time:
            complete_cycle = (n - 1) * 2
            reduced_cycles = time // complete_cycle
            time = time - (complete_cycle * reduced_cycles)

        iterator = 0
        target = 1
        reverse = False
        while iterator < time:
            iterator += 1

            if reverse:
                target -= 1
            else:
                target += 1

            if target == n:
                reverse = True
            elif target == 1:
                reverse = False

        return target


if __name__ == '__main__':
    s = Solution()
    s.passThePillow(4, 5)
