class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        filtered_triplets = [[a, b, c] for a, b, c in triplets if a <= ta and b <= tb and c <= tc]
        return [
            max([a for a, b, c in filtered_triplets], default=0),
            max([b for a, b, c in filtered_triplets], default=0),
            max([c for a, b, c in filtered_triplets], default=0),
        ] == target