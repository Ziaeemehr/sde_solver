#include <iostream>
#include <valarray>
#include <vector>
#include <random>
#include <cmath>

using std::cout;
using std::endl;

typedef std::valarray<double> dim1;

//-------------------------------------------------------//
double f(const double &x, const double alpha)
{
    return (alpha * x);
}
double g(const double &x, const double beta)
{
    return (beta * x);
}

//-------------------------------------------------------//
double EM(const double y,
        const double dt,
        const double alpha,
        const double beta)
{
    std::random_device rd;
    std::mt19937 mt_rand(rd());
    std::normal_distribution<> dist(0, 1);

    double dW = dist(mt_rand) * sqrt(dt);
    return (y + f(y, alpha) * dt + g(y, beta) * dW);
}

int main(int argc, const char **argv)
{

    int N = 2098;
    double T = 1.0;
    double dt = 1.0 / (double)N;
    double alpha = 2.0;
    double beta = 1.0;
    double y = 1.0;

    for (unsigned long i = 1; i < N; ++i)
    {
        y = EM(y, dt, alpha, beta);
        printf("%.6f\n", y);
    }

    return 0;
}