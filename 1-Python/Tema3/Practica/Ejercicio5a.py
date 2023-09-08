def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup & mustard & onion
    pass

# Check your answer
q5.a.check()