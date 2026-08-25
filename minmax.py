
def minimax(depth, node_index, maximizing_player, values, height):
    # Base case: leaf node
    if depth == height:
        return values[node_index]

    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Calculate height of the game tree
import math
height = int(math.log2(len(values)))

# MAX player starts the game
optimal_value = minimax(0, 0, True, values, height)

print("Optimal value:", optimal_value)