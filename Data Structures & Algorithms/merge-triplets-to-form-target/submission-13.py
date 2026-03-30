class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        return [
            max([x if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets]),
            max([y if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets]),
            max([z if (x <= ta and y <= tb and z <= tc) else 0 for x, y, z in triplets])
        ] == target