# distutils: language = c++
# distutils: sources = Noise.cpp

cimport cwrapper_noise

cdef float generate_noise(float mu, float sigma) nogil:
    return cwrapper_noise.generate_noise(mu, sigma)

