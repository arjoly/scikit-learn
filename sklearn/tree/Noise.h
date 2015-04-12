#ifndef NOISE_H
#define NOISE_H

#include <random>

float generate_noise (float mu, float sigma);

/*
class Noise
{
    public:

        float generate_noise (float mu, float sigma)
        {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::normal_distribution<> d(mu,sigma);
            return d(gen);
        }

        Noise();
        virtual ~Noise();
    protected:
};
*/

#endif // NOISE_H
