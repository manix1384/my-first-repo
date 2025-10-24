EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time (in minutes) based on the expected bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time in minutes for the given number of layers."""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed time (prep + bake so far) in minutes."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
