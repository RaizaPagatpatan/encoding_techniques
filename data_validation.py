def is_binary_string(data):
    """
    Validates if the input string consists only of '0's and '1's.
    
    Args data (str): The input string to validate.
    
    Returns bool: True if the string is binary, False otherwise.
    """
    return all(bit in '01' for bit in data)
