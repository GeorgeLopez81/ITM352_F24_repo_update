for number in range(1, 11):
    if number == 5:
        continue  # Skip the rest of the code in this iteration when number is 5

    if number == 8:
        print("Reached 8, stopping the loop.")
        break  # Stop the loop entirely when number is 8

    print(number)  # Print the number if the above conditions are not met
