import random

def anomalous(normal, rate, *anomaly):
    """
    Returns normal value or anomaly values based on rate percentage.
    
    Args:
        normal: The normal value
        rate: Percentage (0-100) of times to return normal value
        *anomaly: One or more anomaly values to return for the remaining rate%
    
    Returns:
        normal value with 'rate'% probability, or a random anomaly value otherwise.
        If no anomaly values provided, always returns normal value.
    
    Raises:
        ValueError: If rate is not between 0 and 100
    """
    
    if not 0 <= rate <= 100:
        raise ValueError(f"rate must be between 0 and 100, got {rate}")
    
    if not anomaly:
        return normal
    
    if random.random() * 100 < rate:
        return normal
    else:
        return random.choice(*anomaly)
    