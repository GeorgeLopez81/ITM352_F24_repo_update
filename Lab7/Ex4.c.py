def check_fares(fares):
    results = []
    for fare in fares:
        if fare > 12:
            results.append(f"This fare {fare} is high!")
        else:
            results.append(f"This fare {fare} is low!")
    return results

# Test cases
def test_check_fares():
    assert check_fares([8.60, 5.75, 13.25, 21.21]) == [
        "This fare 8.6 is low!",
        "This fare 5.75 is low!",
        "This fare 13.25 is high!",
        "This fare 21.21 is high!"
    ]
    
    assert check_fares([12, 12, 12]) == [
        "This fare 12 is low!",
        "This fare 12 is low!",
        "This fare 12 is low!"
    ]
    
    assert check_fares([15, 20, 5, 10]) == [
        "This fare 15 is high!",
        "This fare 20 is high!",
        "This fare 5 is low!",
        "This fare 10 is low!"
    ]
    
    assert check_fares([]) == []  # Testing with an empty list

# Run test cases
test_check_fares()
print("All tests passed!")
