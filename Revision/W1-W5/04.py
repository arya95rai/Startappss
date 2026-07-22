# "You're given a list of integers representing daily stock prices.
#  Write a function that returns the second largest distinct number in the list.
# Example:
# prices = [15, 20, 10, 20, 8, 17]
# Expected output:
# 17
# Constraints:
# Do not use sort() or sorted().
# Do not convert the list to a set.
# The solution should work in a single pass if possible.
prices = [15, 20, 10, 20, 8, 17]
largest=prices[0]
second_largest=None
for current in prices:
    if current>largest:
        second_largest=largest
        largest=current 
    elif current!=largest  and (second_largest is None or current>second_largest):
        second_largest=current
print(f"Second largest: {second_largest}")
        
    
   

    
    

        
        
