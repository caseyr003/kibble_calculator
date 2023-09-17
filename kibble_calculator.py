from functools import wraps

# Constants for the amount of kibble needed per dog size
SMALL_AMOUNT = 10
MEDIUM_AMOUNT = 20
LARGE_AMOUNT = 30
# Constant for the multiplier for extra kibble to order
EXTRA_MULT = 1.2


def validate_input(function):
    """ Decorator to validate input for the kibble_amount function. """
    @wraps(function)
    def wrapper(dogs, leftover):
        # Return ValueError if leftover is negative
        if leftover < 0:
            raise ValueError("Leftover must be greater >= 0.")
        # Return ValueError if any dog counts are negative or not whole numbers
        if (not all(isinstance(count, int) for count in dogs.values())
            or any(count < 0 for count in dogs.values())):
              raise ValueError("Dog counts must be integers >= 0.")
        return function(dogs, leftover)

    return wrapper


@validate_input
def kibble_amount(dogs: dict, leftover: float) -> float:
    """
    Calculates the amount of dog food in lbs to order for a given number of
    dogs and leftover kibble.

    Args:
        dogs (dict): A dictionary for the number of dogs of each size.
        leftover (float): The amount of leftover dog food in lbs.

    Returns:
        float: The calculated dog food in lbs to order for next month.
    """
    return (
        max((dogs['small'] * SMALL_AMOUNT
            + dogs['medium'] * MEDIUM_AMOUNT
            + dogs['large'] * LARGE_AMOUNT
            - leftover)
            * EXTRA_MULT,
            0)
    )
