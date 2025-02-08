def modify_string(S):
    result = []
    i = 0
    n = len(S)

    while i < n:
        count = 1

        # Count the consecutive occurrences of the current character
        while i + 1 < n and S[i] == S[i + 1]:
            count += 1
            i += 1

        # Append the result in the (X,c) format
        result.append(f"({count}, {S[i]})")
        i += 1

    # Join the result with spaces and return
    return " ".join(result)


# Input string
S = input().strip()
# Get the modified string and print the result
print(modify_string(S))
