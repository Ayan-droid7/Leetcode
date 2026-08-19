import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        k = len(primes)
        idx = [0] * k
        heap = [(primes[i], i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(1, n):
            ugly[i] = heap[0][0]
            while heap[0][0] == ugly[i]:
                val, p_idx = heapq.heappop(heap)
                idx[p_idx] += 1
                heapq.heappush(heap, (primes[p_idx] * ugly[idx[p_idx]], p_idx))

        return ugly[-1]