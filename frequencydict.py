test_dict = {"Codingal": 2, "is": 2, "the": 2, "best": 2, "for": 2, "coding": 1}

print("Original Dictionary:", test_dict)

K = 2

res = 0

for value in test_dict.values():
    if value == K:
        res += 1
  
print(f"Number of keys with value {K}:", res)
