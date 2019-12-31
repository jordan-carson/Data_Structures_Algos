def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)
    total_grants = sum(grantsArray)
    amount_to_raise = total_grants - newBudget
    N = len(grantsArray)
    grantsArray.append(0)

    if amount_to_raise == 0:
        return grantsArray[0]

    i = 0
    while i < N and amount_to_raise > 0:
        number_of_people = i + 1
        amount_to_raise -= (grantsArray[i] - grantsArray[i + 1]) * number_of_people

        if amount_to_raise <= 0:
            break
        i += 1

    cap = grantsArray[i + 1]
    # pass # your code goes here
    if amount_to_raise < 0:
        share_amount = abs(amount_to_raise / number_of_people)
        cap += share_amount

    return cap


print(find_grants_cap([2, 100, 50, 120, 1000], 190))
