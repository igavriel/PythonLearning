def from_roman_numeral(roman_numeral):
    # Define a dictionary for Roman numeral values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0

    # Iterate through the Roman numeral from right to left
    for char in reversed(roman_numeral):
        current_value = roman_values[char]
        
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add it to the total
            total += current_value
        
        # Update the previous value for the next iteration
        prev_value = current_value

    return total

if __name__ == "__main__":
    # *assert* enable you to test your code and get feedback on several examples.
    # Keeping or removing this code has no effect on your submission.
    assert from_roman_numeral("IV") == 4
    assert from_roman_numeral("V") == 5
    assert from_roman_numeral("IX") == 9
    assert from_roman_numeral("XI") == 11
    assert from_roman_numeral("XX") == 20
    assert from_roman_numeral("DCCC") == 800
    assert from_roman_numeral("MMMM") == 4000