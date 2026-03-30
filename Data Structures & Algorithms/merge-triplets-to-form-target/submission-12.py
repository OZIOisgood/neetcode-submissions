class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        a = max([x if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets])
        b = max([y if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets])
        c = max([z if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets])
        return [a, b, c] == target