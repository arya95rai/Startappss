

from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

dq = deque()
answer = []

for i in range(len(nums)):

    # Remove indices outside current window
    while dq and dq[0] <= i - k:
        dq.popleft()

    # Remove smaller elements from back
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()

    # Add current index
    dq.append(i)

    # Store maximum once window size becomes k
    if i >= k - 1:
        answer.append(nums[dq[0]])

print(answer)