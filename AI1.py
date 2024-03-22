import numpy as np
# Define the triangular membership function
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))
# Define the fuzzy sets A and B using triangular membership functions
x = np.linspace(0, 5, 1000)  # Define the universe of discourse
mA = triangular(x, 1, 2, 3) * 0.5 + triangular(x, 3, 4, 5) * 0.4 + triangular(x, 0, 1, 2) * 0.6 + triangular(x, 2, 3, 4) * 0.2
mB = triangular(x, 2, 3, 4) * 0 + triangular(x, 1, 2, 3) * 0.2 + triangular(x,
0, 1, 2) * 0.2 + triangular(x, 3, 4, 5) * 0.8
# Union of fuzzy sets A and B
union = np.maximum(mA, mB)
# Intersection of fuzzy sets A and B
intersection = np.minimum(mA, mB)
# Difference of fuzzy sets A and B
difference = np.maximum(mA - mB, 0)
# Complement of fuzzy set A
complementA = 1 - mA
# Complement of fuzzy set B
complementB = 1 - mB

# Verify De Morgan&#39;s law: ~(A ∪ B) = ~A ∩ ~B
demorgan_lhs = 1 - np.maximum(mA, mB)
demorgan_rhs = np.minimum(1 - mA, 1 - mB)
# Check if the two sides of De Morgan&#39;s law are equal
demorgan_verified = np.allclose(demorgan_lhs, demorgan_rhs)
# Print the results
print("Union of A and B:&quot", union)
print("Intersection of A and B:", intersection)
print("Difference of A and B:", difference)
print("Complement of A:", complementA)
print("Complement of B:", complementB)
print("De Morgans Law Verified", demorgan_verified)