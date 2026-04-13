from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===

    #track keys mapped to values, s1 = { value: original_key }
    values_s1 = {}

    for key, value in mapping.items():
        if value in values_s1: #check for a collision, return the original key and the current key
            return (values_s1[value], key)
        
        values_s1[value] = key #stores the value produced by the key

    return None

    # === END TODO ===
#values_s1 is created as an empty dict so that we can loop through every key and value pair from the input mapping
#collision check to find the non-injective pair, record the new value and return None if the mapping is injective without duplicates

def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===

    #collect values reached by the mapping
    values_r1 = set(mapping.values())

    #iterate through to find elements not in values_r1
    for elem in target:
        if elem not in values_r1:
            return elem

    return None #if all elems in target are found via values_r1, it's surjective
    # === END TODO ===
#similar logic to injective pair, converted to a set, then check target against values_r1, then return None if every elem was successfully mapped

def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
