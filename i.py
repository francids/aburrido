loot: dict = {
    "sword": 1,
    "shield": 1,
    "potion": 2,
}

inv: dict = {
    "sword": 1,
    "potion": 4,
}

new_inv: dict = {k: inv.get(k, 0) + loot.get(k, 0) for k in set(inv | loot)}
print(new_inv)

# ...

old = ["a", "c", "a", "c", "b", "a"]
new = list(dict.fromkeys(old).keys())
print(new)

x = [1, 2, 1, 3, 4, 1, 2, 4, 1]
most = max(x, key=x.count)
print(most)
