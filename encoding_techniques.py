import numpy as np

def nrz_l(data):
    """Non-Return-to-Zero Level (NRZ-L) encoding."""

    return [1 if bit == '1' else 0 for bit in data]

def nrz_i(data, initial_state):
    """Non-Return-to-Zero Inverted (NRZ-I) encoding."""
    
    current_state = 1 if initial_state.lower() == 'high' else 0
    output = [current_state]  # Start with the initial state
    
    for bit in data:
        if bit == '1':
            # Toggle the state on '1'
            current_state = 1 - current_state
        # Keep the state on '0'
        output.append(current_state)
    
    return output[1:]

    return output

def bipolar_ami(data):
    """Bipolar Alternate Mark Inversion (AMI) encoding."""
    output, last = [], 1

    for bit in data:
        if bit == '1':
            output.append(last)
            last = -last
        else:
            output.append(0)
            
    return output

def pseudoternary(data, initial_state):
    """Pseudoternary encoding with initial state."""
    last = -1 if initial_state.lower() == 'low' else 1
    output = []
    
    for bit in data:
        if bit == '0':  # Only '0' toggles polarity
            last = -last
            output.append(last)
        else:
            output.append(0)  # '1' stays neutral
    return output


def manchester(data):
    """Manchester encoding."""
    output = []
    for bit in data:
        if bit == '0':
            # 0 = High to Low
            output.extend([1, 0])
        else:
            # 1 = Low to High
            output.extend([0, 1])

    return output

def differential_manchester(data, initial_state):
    """Differential Manchester encoding with initial state."""
    # Initial state represents the mid-bit starting polarity
    current_state = 1 if initial_state.lower() == 'high' else 0
    output = []
    
    for bit in data:
        if bit == '1':
            # '1': Start with transition at the mid
            output.extend([1 - current_state, current_state])
        else:
            # '0': No mid transition, transition at start
            current_state = 1 - current_state
            output.extend([1 - current_state, current_state])
    
    return output
