def separate_duplicates(player_hand: list[int]):
    separated_hand = None
    for potential_duplicate in player_hand:
        # here remainder is just the player's hand minus the current card we're iterating over
        remainder = player_hand.copy()
        remainder.remove(potential_duplicate)  # remainder = 3 cards

        # if the removed value is still present in remainder then we have a duplicate
        if potential_duplicate in remainder:
            remainder.remove(potential_duplicate)  # remove it again to remain with your two unique cards
            separated_hand = {
                "duplicates": [potential_duplicate, potential_duplicate],
                "unique": remainder
            }
            # break  # we break out of the loop as soon as we find the first value with a duplicate
            return separated_hand  # alternatively we could return separated_hand right inside the if block,
            # that would also break the loop
    return separated_hand


a = separate_duplicates([1, 2, 3, 4])
b = separate_duplicates([3, 3, 5, 8])
c = separate_duplicates([8, 8, 8, 10])
d = separate_duplicates([7, 7, 7, 7])
e = separate_duplicates([2, 6, 4, 2])
f = separate_duplicates([10, 4, 10, 10])
print(f"""
    {a}
    {b}
    {c}
    {d}
    {e}
    {f}
""")


