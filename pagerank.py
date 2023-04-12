import numpy as np

def pagerank(M, p, N, num_iterations=100):
    """
    Computes the PageRank vector for a given web graph represented by the Google matrix M,
    with teleportation probability p, and total number of websites N.
    """
    # Initialize the PageRank vector with equal probabilities for all websites
    P = np.ones(N) / N

    # Iterate for a fixed number of iterations
    for i in range(num_iterations):
        # Compute the teleportation factor (1-p) * Mp
        teleportation = (1 - p) * np.dot(M, P)

        # Update the PageRank vector with the teleportation factor
        P = teleportation + (p / N)

    return P

# Example usage
# Define the size of the web graph (number of websites)
N = 5

# Generate a random Google matrix M with transition probabilities
M = np.random.rand(N, N)
M /= M.sum(axis=1, keepdims=True)  # Normalize rows to sum to 1

# Define the teleportation probability
p = 0.15

# Compute the PageRank vector
P = pagerank(M, p, N)

# Print the PageRank scores
print("PageRank scores: ", P)
