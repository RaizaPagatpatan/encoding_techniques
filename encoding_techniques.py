import numpy as np

def nrz_l(data):
    """Non-Return-to-Zero Level (NRZ-L) encoding."""

    return [1 if bit == '1' else -1 for bit in data]

def nrz_i(data):
    """Non-Return-to-Zero Inverted (NRZ-I) encoding."""
    output, last = [], 1

    for bit in data:
        if bit == '1':
            last = -last
        output.append(last)

    return output

def bipolar_ami(data):
    return 0

def pseudoternary(data):
    return 0

def manchester(data):
    return 0

def differential_manchester(data):
    return 0