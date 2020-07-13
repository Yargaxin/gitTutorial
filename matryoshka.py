def matr(n):
	if n == 1:
		print("Матрёшечка")

	else:
		print("Вверх матрёшки n=", n)
		matr(n-1)
		print("Низ матрёшки n=", n)
matr(5)	