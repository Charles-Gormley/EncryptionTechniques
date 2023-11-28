def can_reach_target(target, weights):
    if target == 0:
        return True
    if target < 0 or not weights:
        return False
    
    # Try using the first weight and recursively check if it's possible to reach the target
    return can_reach_target(target - weights[0], weights[1:]) or can_reach_target(target, weights[1:])

# List of available weights
weights = [0.5] * 2 + [1] * 4 + [7.5] *2 + [6] * 2 + [10] * 2 + [25] * 2

# Check if each integer from 0 to 100 can be reached
for i in range(101):
    if can_reach_target(i, weights):
        print(f"You can make {i} lbs.")
    else:
        print(f"You cannot make {i} lbs.")
