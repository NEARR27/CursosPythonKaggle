x = True
print(x)
print(type(x))


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

print(3.0 == 3)
print('3' == 3)

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))