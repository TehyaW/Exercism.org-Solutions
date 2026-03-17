#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :return: expected bake time - time remaining.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time



#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param preparation_time: number of layers time 2.
    :return: prep time in minutes.

    Function that takes the number of layers the lasagna has as
    an argument and returns how many minutes of preparation the lasagna needs.
    """
    return (number_of_layers)*2    

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param elasped_time_in_minutes: number of layers time 2 plus elapsed bake time.
    :return: elapsed time in minutes.

    Function that takes the number of layers the lasagna has and the elapsed bake time as
    arguments and returns how many minutes you have already been in the kitchen making the lasagna.
    """
    return (number_of_layers)*2 + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
