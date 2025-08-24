def partition(s: str):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                backtrack(end, path + [substring])

    backtrack(0, [])
    return result

# Example
print("Palindrome Partitions:", partition("aab"))
