import math

depth_limit = int(input("Enter depth of binary tree: "))

num_leaves = 2 ** depth_limit

print(f"\nEnter {num_leaves} leaf node values:")

values = []

for i in range(num_leaves):
    values.append(int(input(f"Leaf {i+1}: ")))

def alphabeta(depth, nodeIndex, maximizingPlayer,
              values, alpha, beta):

    if depth == depth_limit:
        print(f"Visited Leaf: {values[nodeIndex]}")
        return values[nodeIndex]

    if maximizingPlayer:

        best = -math.inf

        for i in range(2):

            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruned at depth {depth}")
                break

        return best

    else:

        best = math.inf

        for i in range(2):

            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruned at depth {depth}")
                break

        return best

result = alphabeta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf
)

print("\nOptimal Value =", result)