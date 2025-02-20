#include <iostream>
#include <complex>
#include <random>
#include <chrono>
#include <cblas.h>
#include <algorithm>

int main() {
	//Вариант решения 1
	std::default_random_engine re(std::chrono::system_clock::now().time_since_epoch().count());
	std::uniform_real_distribution<double> di(-1., 1.);

	std::size_t size = 2048;
	std::size_t sizeSquare = size * size;

	auto randomComplexNumber = [&]() { return std::complex<double>{di(re), di(re)}; };

	auto* a = new std::complex<double>[sizeSquare] {};
	std::generate(a, a + sizeSquare, randomComplexNumber);

	auto* b = new std::complex<double>[sizeSquare] {};
	std::generate(b, b + sizeSquare, randomComplexNumber);

	auto* result = new std::complex<double>[sizeSquare] {};
	for (std::size_t i = 0; i < size; ++i) {
		for (std::size_t j = 0; j < size; ++j) {
			for (std::size_t k = 0; k < size; ++k) {
				result[i * size + j] += a[i * size + k] * b[k * size + j];
			}
		}
	}
	//Вариант решения 2

	// Размер матриц
	const int N = 2048;

	// Определяем матрицы A, B и C
	std::complex<double> A[N][N], B[N][N], C[N][N];

	// Инициализация матриц A и B случайными значениями
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			A[i][j] = std::complex<double>(rand() % 10, rand() % 10); // Случайные комплексные числа
			B[i][j] = std::complex<double>(rand() % 10, rand() % 10);
			C[i][j] = std::complex<double>(0, 0); // Инициализация C нулями
		}
	}

	// Параметры для cblas_zgemm
	const double alpha = 1.0; // Коэффициент для A*B
	const double beta = 0.0;   // Коэффициент для C

	// Умножение матриц
	cblas_zgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
		N, N, N,
		&alpha,
		(const void*)A, N,
		(const void*)B, N,
		&beta,
		(void*)C, N);

	//Вариант решения 3
	double A[2048][2048], B[2048][2048], C[2048][2048];


	for (int i = 0; i < 2048; ++i)
		for (int j = 0; j < 2048; ++j)
		{
			C[i][j] = 0.0;
			for (int k = 0; k < 2048; ++k)
				C[i][j] += A[i][k] * B[k][j];
		}
	return 0;
}