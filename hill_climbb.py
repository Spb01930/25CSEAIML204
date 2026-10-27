def objective(x):
    return -(x-3)**2+9
def hill_climbing(start):
    current=start
    
    while True:
        left=current-1
        right=current+1
        
        current_value=objective(current)
        left_value=objective(left)
        right_value=objective(right)
        
        #find the better neighbour
        if left_value > current_value:
            current=left
        elif right_value > current_value:
            current=right
        else:
            return current,current_value
        
#starting point
start=0
best_state,best_value=hill_climbing(start)

print("Best State:",best_state)
print("Best Value:",best_value)             

"""
output:Best State: 3
       Best Value: 9
"""       
