loot: dict = {
    "Sword": 1,
    "Shield": 1,
    "Potion": 2,
}

inv: dict = {
    "Sword": 1,
    "Potion": 4,
}

new_inv: dict = {
    k: inv.get(k, 0) + loot.get(k, 0) for k in set(inv | loot)
}
print(new_inv)

old = ["a", "c", "a", "c", "b", "a"]
new = list(dict.fromkeys(old).keys())
print(new)

x = [1, 2, 1, 3, 4, 1, 2, 4, 1]
most = max(x, key=x.count)
print(most)
