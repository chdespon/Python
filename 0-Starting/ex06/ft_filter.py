# Recode your own ft_filter, it should behave like the original built-in
# function (it should return the same thing as "print(filter.__doc__)"),
# you should use list comprehensions to recode your ft_filter.

def ft_filter(function_to_apply, list_of_inputs):
    """
    Apply a function to all the elements of a list

    Parameters:
        function_to_apply (function): function to apply
        list_of_inputs (list): list of inputs
    Returns:
        list
    """
    if not callable(function_to_apply):
        raise TypeError(f"Expected a callable, got "
                        f"{type(function_to_apply).__name__}")
    return [i for i in list_of_inputs if function_to_apply(i)]
