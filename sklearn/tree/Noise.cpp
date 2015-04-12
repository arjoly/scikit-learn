#include "Noise.h"

float generate_noise (float mu, float sigma)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<> d(mu,sigma);
    return d(gen);
}

/*
Noise::Noise()
{

}

Noise::~Noise()
{
    //dtor
}
*/
