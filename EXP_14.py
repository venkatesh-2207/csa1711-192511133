
def minimax(depth, node, maximizing, alpha, beta, scores):
    if depth == 2:
        return scores[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False,
                            alpha, beta, scores)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True,
                            alpha, beta, scores)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

scores = [3, 5, 2, 9]

result = minimax(0, 0, True, float('-inf'),
                 float('inf'), scores)

print("Leaf Scores:", scores)
print("Best Score:", result)
