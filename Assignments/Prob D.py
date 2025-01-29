def minimal_wastage(tokens, claim, k, items):
    n = len(tokens)
    min_wastage = float('inf')
    selected_item = None

    for i in range(n - k + 1):
        current_wastage = 0
        current_claimed = claim[i:i+k]

        for j in range(k):
            if not current_claimed[j]:
                current_wastage += tokens[i + j]

        if current_wastage < min_wastage:
            min_wastage = current_wastage
            selected_item = items[i]

    # Find all items with minimal wastage
    selected_items = [selected_item]
    for i in range(n - k + 1):
        current_wastage = 0
        current_claimed = claim[i:i+k]

        for j in range(k):
            if not current_claimed[j]:
                current_wastage += tokens[i + j]

        if current_wastage == min_wastage and items[i] not in selected_items:
            selected_items.append(items[i])

    return selected_items

# Example usage:
tokens = [8,32,27,37,45,34,3,100]
claim = [1, 0, 1, 0, 1,0,1,0]
k = 4

items = ["Fan", "Gas", "Geyser", "Chair", "Cooker","Cot","Bucket","Mug","Ac","Bulb"]

result = minimal_wastage(tokens, claim, k, items)
print("Selected item(s):", result)