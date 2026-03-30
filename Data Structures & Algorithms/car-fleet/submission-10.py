class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [
            (p, s) for p, s in zip(position, speed)
        ]
        pair.sort(
            reverse=True
        )
        print(pair)

        stack = []

        for p, s in pair:
            stack.append(
                (target - p) / s
            )
            print(f"(p, s): ({p}, {s}); t: {(target - p) / s}")

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

            print(
                f"stack: {stack}"
            )

        return len(stack)

# S/V=[km/(km/h)=(km*h)/km=h]=T