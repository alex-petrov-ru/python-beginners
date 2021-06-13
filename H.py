def dot_product(N, vector1, vector2):
	scalar_product_of_vector = 0
	for i in range(len(A)):
		scalar_product_of_vector += B[i]*A[i]
	return scalar_product_of_vector
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]
print(dot_product(A, B))