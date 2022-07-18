# A person can go alone or go in a pair

def persons_going_to_a_party(n):
    if n == 1 or n == 2:
        return n

    return persons_going_to_a_party(n-1) + n-1*persons_going_to_a_party(n-2)

print(persons_going_to_a_party(3))

